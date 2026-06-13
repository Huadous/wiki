---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/rdma.md]]"
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
  - "brpc RDMA实现与配置"
  - "brpc RDMA Documentation"
---

## 来源
- Original file: [[brpc/rdma.md]]
- Ingested: 2026-06-13

## 核心内容
本文档详细介绍了 [[entities/brpc|brpc]] 框架中 RDMA（远程直接内存访问）功能的编译、核心实现原理及可配置参数。[[entities/brpc|brpc]] 仅在 Linux 系统上支持 RDMA，提供了 config_brpc、cmake 和 bazel 三种构建方式，并附带 [[entities/rdma_performance|rdma_performance]] 示例程序。

核心实现上，[[entities/brpc|brpc]] 通过 [[entities/rdmaendpoint|RdmaEndpoint]] 类将 RDMA QP 与 Socket 类结合，复用 EventDispatcher 进行事件处理、InputMessenger 完成 RPC 消息解析。[[concepts/rdma|RDMA]] 采用 [[concepts/rc模式|RC]] 模式，每个 [[entities/rdmaendpoint|RdmaEndpoint]] 对应一个 [[concepts/qp|QP]]，建连依赖前置 TCP 握手交换 GID、QPN 等参数。

数据传输具备三大特性：基于 [[concepts/iobuf|IOBuf]] Block 的 [[concepts/零拷贝数据传输|零拷贝机制]]、通过 [[concepts/立即数|立即数]] 形式的 ACK 实现的 [[concepts/滑动窗口流控|滑动窗口流控]]、以及通过 [[concepts/solicited标志|solicited标志]] 控制的 [[concepts/事件聚合|事件聚合]]。内存管理方面，[[entities/brpc|brpc]] 通过 [[entities/block_pool|block_pool]] 统一内存池接管 IOBuf 内存，并支持用户通过 `rdma::RegisterMemoryForRdma` 自行注册应用内存。

## 关键实体
- [[entities/brpc|brpc]]：百度开源的工业级 C++ RPC 框架
- [[entities/rdmaendpoint|RdmaEndpoint]]：brpc 中负责 RDMA 通信的核心类
- [[entities/rdma_performance|rdma_performance]]：brpc 官方提供的 RDMA 性能测试示例程序
- [[entities/block_pool|block_pool]]：brpc 中负责 RDMA 内存管理的统一内存池实现
- [[entities/spdk|SPDK]]：用户态存储驱动框架，可与 brpc 轮询模式配合
- [[entities/io_uring|io_uring]]：Linux 内核异步 I/O 接口框架

## 关键概念
- [[concepts/rdma|RDMA]]：远程直接内存访问技术
- [[concepts/零拷贝数据传输|零拷贝数据传输]]：通过 IOBuf Block 直接收发数据
- [[concepts/滑动窗口流控|滑动窗口流控]]：通过 ACK 避免发送速度超过接收端处理能力
- [[concepts/事件聚合|事件聚合]]：通过 solicited 标志控制 CQ 事件触发
- [[concepts/memory-registration|Memory Registration]]：RDMA 通信必备的内存注册操作
- [[concepts/内存池|内存池]]：用于加速内存注册、减少重复注册开销
- [[concepts/rdma握手|RDMA握手]]：基于 TCP 交换 RDMA 参数的建连过程
- [[concepts/verbs-api|verbs API]]：RDMA 用户态编程接口标准
- [[concepts/qp|QP]]：Queue Pair，RDMA 通信的基本单元
- [[concepts/cq|CQ]]：Completion Queue，完成事件通知机制
- [[concepts/rc模式|RC模式]]：Reliable Connected，可靠连接传输模式
- [[concepts/iobuf|IOBuf]]：brpc 中管理网络数据收发的核心数据结构
- [[concepts/立即数|立即数]]：RDMA 发送时可附带的短数据，用于 ACK 传递
- [[concepts/solicited标志|Solicited标志]]：控制接收端是否生成完成事件的标志
- [[concepts/轮询模式|轮询模式]]：持续轮询 CQ 而非等待事件的低延迟模式

## 要点
- brpc 的 RDMA 功能仅在 Linux 系统上可用，且需要特定的网卡驱动与硬件支持
- [[entities/rdmaendpoint|RdmaEndpoint]] 是 brpc RDMA 的核心类，每个对应一个 [[concepts/qp|QP]]，复用 Socket 的 fd 但通过 [[concepts/verbs-api|verbs API]] 收发数据
- RDMA 连接建立必须先完成 TCP 连接，再通过 AppConnect 逻辑交换 GID、QPN 等参数
- brpc RDMA 的三大数据传输特性：基于 IOBuf Block 的 [[concepts/零拷贝数据传输|零拷贝]]、基于 ACK 的 [[concepts/滑动窗口流控|滑动窗口流控]]、通过 [[concepts/solicited标志|solicited标志]] 的 [[concepts/事件聚合|事件聚合]]
- [[entities/block_pool|block_pool]] 统一内存池接管所有 [[concepts/iobuf|IOBuf]] 内存以加速 [[concepts/memory-registration|内存注册]]，应用也可自行通过 `rdma::RegisterMemoryForRdma` 注册自有内存
- RDMA 支持事件驱动（默认）和 [[concepts/轮询模式|轮询]] 两种模式，轮询模式可配合 SPDK/io_uring 等使用
- 接收端预提交 Block 大小 recv_block_size（默认 8KB）限制了发送端单个请求的最大尺寸