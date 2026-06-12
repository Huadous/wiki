---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_rdma]]"
  - "[[sources/rdma]]"
  - "[[sources/en_overview]]"
tags:
  - "field"
aliases:
  - "远程直接内存访问"
  - "Remote Direct Memory Access"
---

## Description
RDMA（Remote Direct Memory Access）是一种网络通信技术，允许计算机在不经过操作系统内核及CPU参与的情况下，直接访问远程计算机的内存。该技术通过专门的硬件（如InfiniBand或RoCE网卡）实现零拷贝、内核旁路的数据传输，显著降低了网络通信延迟和CPU负载。由于RDMA对驱动与硬件有要求，目前仅支持在Linux系统编译并运行RDMA功能。RDMA与TCP不同，不使用socket接口进行通信，而是通过Verbs API（如ibv_post_send、ibv_post_recv）进行数据收发。RDMA是硬件相关的通信技术，包含许多独特概念，如device、port、GID、LID、MaxSge等。brpc框架中的RDMA实现基于RC（可靠连接）模式，利用QP（队列对）、CQ（完成队列）等核心概念，并通过握手过程建立连接。此外，RDMA要求数据收发所使用的内存空间必须被注册（memory register），这一特性与[[concepts/零拷贝|零拷贝]]密切相关。在brpc文档中，RDMA被列为计划支持的协议之一（will be opensourced），其极低的延迟和高吞吐量特别适合高性能计算和低延迟网络环境。RDMA广泛应用于高性能计算和存储系统，如InfiniBand和RoCE。

## Related Concepts
- [[concepts/qp|QP]]
- [[concepts/零拷贝|零拷贝]]
- [[concepts/握手|握手]]
- [[concepts/延迟|延迟]]
- [[concepts/cq|CQ]]
- [[concepts/rc|RC]]
- [[concepts/内存注册|内存注册]]
- [[concepts/事件驱动模式|事件驱动模式]]
- [[concepts/轮询模式|轮询模式]]
- [[concepts/tcp|TCP/IP]]
- [[concepts/序列化|Serialization]]
- [[concepts/高性能计算|高性能计算]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/rdmaendpoint|RdmaEndpoint]]
- [[entities/blockpool|BlockPool]]
- [[entities/iobuf|IOBuf]]

## Mentions in Source
> **Source: [[sources/en_rdma]]**
> - "Since RDMA requires driver and hardware support, only the build on linux is verified."
> - "RDMA does not use socket API like TCP."
> - "brpc uses RDMA RC mode. Every RdmaEndpoint has its own QP."

> **Source: [[sources/rdma]]**
> - "由于RDMA对驱动与硬件有要求，目前仅支持在Linux系统编译并运行RDMA功能。"
> - "RDMA与TCP不同，不使用socket接口进行通信。"
> - "RDMA要求数据收发所使用的内存空间必须被注册（memory register）。"
> - "RDMA是硬件相关的通信技术，有很多独特的概念，比如device、port、GID、LID、MaxSge等。"

> **Source: [[sources/en_overview]]**
> - "rdma support (will be opensourced)"