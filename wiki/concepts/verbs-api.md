---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/rdma]]"]
tags: [standard]
aliases:
  - "RDMA verbs API"
  - "InfiniBand verbs"
  - "verbs API"
---


# verbs API

## 定义

verbs API是RDMA（远程直接内存访问）的底层编程接口，由InfiniBand规范定义。它提供对RDMA网卡（HCA，主机通道适配器）的直接操作能力，允许用户态应用程序通过内存注册、发送/接收请求提交、完成队列轮询等操作实现零拷贝数据传输。在brpc框架的RDMA实现中，verbs API替代了传统socket接口，作为数据收发的核心机制。

## 关键特征

- **直接硬件访问**：verbs API允许用户态程序绕过操作系统内核，直接与RDMA网卡通信。
- **零拷贝数据传输**：通过内存注册（MR）机制，verbs API支持数据在网卡与应用程序内存之间的直接传输，无需中间缓冲区拷贝。
- **异步操作模型**：verbs API采用Work Request（WR）提交任务，并通过Completion Queue（CQ）异步通知完成状态。
- **队列对（QP）通信**：数据收发基于QP（Queue Pair）模型，包括Send Queue和Receive Queue。
- **内存注册机制**：应用程序在发起RDMA操作前，必须将内存区域注册到网卡，获取本地和远程内存密钥（lkey/rkey）。

## 应用

- **高性能RPC框架**：在[[entities/brpc|brpc]]中，[[entities/rdmaendpoint|RdmaEndpoint]]利用verbs API实现RDMA数据收发，替代传统socket系统调用，降低延迟并提升吞吐量。
- **零拷贝数据传输**：调用verbs API中的`ibv_post_send`将数据提交到QP，并通过`ibv_poll_cq`从CQ获取完成事件，实现高效的零拷贝网络通信。
- **事件驱动I/O复用**：verbs API的CQ事件可通过独立的文件描述符（fd）与[[concepts/EventDispatcher|EventDispatcher]]（如brpc的IO线程模型）集成，实现高效的事件驱动处理。

## 相关概念

- [[concepts/QP|QP]]（队列对）
- [[concepts/CQ|CQ]]（完成队列）
- [[concepts/内存注册|内存注册]]（Memory Registration, MR）
- [[concepts/零拷贝|零拷贝]]

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]

## 来源提及

- "当RDMA被使能时，写入Socket的数据会通过RdmaEndpoint提交给RDMA QP（通过verbs API），而非拷贝到fd。" — [[sources/rdma|rdma]]
- "对于数据读取，RdmaEndpoint中则调用verbs API从RDMA CQ中获取对应完成信息（事件获取有独立的fd，复用EventDispatcher，处理函数采用RdmaEndpoint::PollCq）。" — [[sources/rdma|rdma]]