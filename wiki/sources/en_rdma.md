---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_rdma.md]]"
tags: [RDMA, 零拷贝, 滑动窗口流控, 事件抑制, 握手, AppConnect, RC模式, QP, CQ, 内存注册]
aliases: ["brpc RDMA指南", "brpc远程直接内存访问支持"]
---

# brpc RDMA支持 - Summary

## 来源
- Original file: [[brpc/en_rdma.md]]
- Ingested: 2026-06-12

## 核心内容
本文档详细介绍了在 [brpc](entities/brpc) 框架中集成 [RDMA](concepts/rdma)（远程直接内存访问）的构建方法、核心实现原理及可配置参数。构建部分提供了使用 `config_brpc`、cmake 和 bazel 三种工具启用 RDMA 的步骤。实现部分阐述了 brpc 如何通过 [RdmaEndpoint](entities/rdmaendpoint) 类利用 RDMA 替代传统 TCP，主要依赖三大关键特性：[零拷贝](concepts/零拷贝)、[滑动窗口流控](concepts/滑动窗口流控) 和 [事件抑制](concepts/事件抑制)。文档还详细说明了 [握手](concepts/握手) 过程（通过 [AppConnect](concepts/appconnect) 方式交换 GID 和 QPN）、[QP](concepts/qp) 与 [CQ](concepts/cq) 的管理机制，以及 [内存注册](concepts/内存注册) 的优化方案——即通过 [Block Pool](entities/block-pool) 内存池统一管理 [IOBuf](entities/iobuf) 的内存。文档列出了20余个可调参数及其默认值，帮助开发者根据实际场景调整 RDMA 行为。

## 关键实体
- [brpc](entities/brpc) — 高性能 RPC 框架，本文档聚焦其 RDMA 集成
- [RdmaEndpoint](entities/rdmaendpoint) — 封装 RDMA 通信的核心类，管理 QP 和 CQ
- [IOBuf](entities/iobuf) — 缓冲区管理类，其 Block 块直接用于零拷贝传输
- [Block Pool](entities/block-pool) — RDMA 内存池，接管 IOBuf 内存以避免频繁注册

## 关键概念
- [RDMA](concepts/rdma) — 远程直接内存访问技术，本文档主题
- [零拷贝](concepts/零拷贝) — 数据在 IOBuf 块间直接传输，避免内核态拷贝
- [滑动窗口流控](concepts/滑动窗口流控) — 通过接收端 ACK 防止发送端过快
- [事件抑制](concepts/事件抑制) — 根据条件设置 solicited 标志，减少 CPU 中断
- [握手](concepts/握手) — 通过 TCP 交换 GID 和 QPN 建立 RDMA 连接
- [AppConnect](concepts/appconnect) — brpc 的应用层连接方式，用于握手
- [RC模式](concepts/rc模式) — RDMA 的可靠连接模式，brpc 默认采用
- [QP](concepts/qp) — 队列对，RDMA 通信的基本端点
- [CQ](concepts/cq) — 完成队列，存放 RDMA 操作完成事件
- [内存注册](concepts/内存注册) — 将内存区域注册到 RDMA 设备以获得 L_Key

## 要点
- brpc 在 Linux 上通过三种构建方式（config_brpc、cmake、bazel）启用 RDMA 支持
- 三大关键特性（零拷贝、滑动窗口流控、事件抑制）共同实现高性能 RDMA 通信
- RDMA 采用 RC 模式，每个端点拥有独立 QP，握手后 TCP 连接不再用于数据传输
- 内存注册开销通过 Block Pool 统一管理 IOBuf 内存来优化
- 支持用户自定义内存注册，通过 `IOBuf::append_user_data_with_meta` 传递 lkey
- 提供 20 余个可调参数，覆盖接收块大小、QP 深度、CQE 轮询数、内存池大小等