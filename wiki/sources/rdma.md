---
type: source
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/rdma]]"
  - "[[sources/en_overview]]"
tags:
  - "RDMA"
  - "零拷贝"
  - "滑动窗口流控"
  - "事件聚合"
  - "内存注册"
  - "内存池"
  - "事件驱动模式"
  - "轮询模式"
  - "QP"
  - "CQ"
  - "RC"
  - "握手"
  - "AppConnect"
  - "verbs API"
  - "GID"
  - "LID"
  - "solicited标志"
  - "MaxSge"
aliases:
  - "RDMA Support in BRPC"
  - "brpc RDMA文档"
---

## 关键实体

- [[entities/brpc|brpc]] — 高性能 RPC 框架，本文档描述在其内集成 RDMA 功能
- [[entities/rdmaendpoint|rdmaendpoint]] — RDMA 数据收发核心类，负责通过 verbs API 与 QP/CQ 交互
- [[entities/blockpool|blockpool]] — 统一内存池，管理 IOBuf 的注册内存
- [[entities/iobuf|iobuf]] — 数据缓冲区，其内存由 BlockPool 统一管理以实现零拷贝

## 关键概念

- [[concepts/rdma|rdma]] — 远程直接内存访问技术，允许绕过内核直接访问远程内存，通过 InfiniBand 或 RoCE 实现
- [[concepts/零拷贝|零拷贝]] — 通过 Block 引用和接收端预提交减少数据拷贝
- [[concepts/滑动窗口流控|滑动窗口流控]] — 通过显式 ACK 控制发送端速度
- [[concepts/事件聚合|事件聚合]] — 通过 solicited 标志减少事件通知
- [[concepts/内存注册|内存注册]] — RDMA 必须的内存页表注册操作
- [[concepts/内存池|内存池]] — 预注册大块内存以避免逐次注册开销
- [[concepts/qp|qp]] — 队列对，由 SQ 和 RQ 组成，每个 RdmaEndpoint 对应一个 QP
- [[concepts/cq|cq]] — 完成队列，存放完成事件
- [[concepts/rc|rc]] — 可靠连接传输服务
- [[concepts/握手|握手]] — 通过 TCP 交换 GID、QPN 等参数建立连接
- [[concepts/verbs-api|verbs-api]] — RDMA 底层编程接口
- [[concepts/gid|gid]] — 全局标识符，用于端点寻址
- [[concepts/lid|lid]] — 本地标识符，用于子网路由
- [[concepts/solicited标志|solicited标志]] — 控制事件通知的发送标志
- [[concepts/maxsge|maxsge]] — 最大散聚条目数量

## 要点

- RDMA 仅支持在 Linux 系统编译和运行，需要硬件和驱动支持
- 支持三种构建方式：config_brpc、cmake 和 bazel
- 每个 RdmaEndpoint 对应一个 QP，使用 RC 可靠连接模式通信
- 数据传输三大特性：零拷贝、滑动窗口流控和事件聚合
- 通过 BlockPool 统一内存池管理注册内存，避免频繁内存注册
- 支持事件驱动和轮询两种工作模式
- 可配合 spdk/io_uring 驱动使用，需设置对应参数
- 连接建立依赖 TCP 握手交换硬件参数
- 提供丰富的可配置参数优化性能
- RDMA 技术通过内核旁路机制实现高带宽、低延迟的数据传输，适用于高性能计算和分布式存储场景
- 在生产环境中部署 RDMA 需要确保网卡、驱动和固件版本的兼容性
- 调试 RDMA 问题时常用的工具包括 ibv_devinfo、ibstat 和 perfquery 等
- brpc 计划将 RDMA 作为协议支持（will be opensourced），以进一步提升在高性能场景中的表现
- RDMA 通常通过 InfiniBand 或 RoCE（RDMA over Converged Ethernet）实现
- RDMA 支持多种传输协议层次：InfiniBand（原生架构）、RoCEv1/RoCEv2（基于以太网）以及 iWARP（基于 TCP），不同协议在部署复杂度和性能特征上存在差异
- 通过内核旁路机制，RDMA 允许用户在用户态直接操控网卡寄存器，显著降低网络延迟和 CPU 负载