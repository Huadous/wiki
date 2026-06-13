---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/rdma]]"]
tags: [term]
aliases:
  - "Global Identifier"
  - "全局标识符"
---


# GID

## 定义
GID（全局标识符，Global Identifier）是RDMA网络中每个端口和端节点的128位唯一标识符，类似于IP地址，用于在InfiniBand或RoCE（RDMA over Converged Ethernet）网络中进行端点寻址。在brpc的RDMA握手过程中，通信双方需要交换GID、QPN（队列对编号）等参数来建立RDMA连接。

## 关键特征
- **128位长度**：GID是128位的全局唯一标识符，通常基于IPv6地址格式。
- **唯一性**：每个RDMA端口和端节点具有唯一的GID，确保网络中的精确端点识别。
- **层次结构**：GID通常包含子网前缀（Subnet Prefix）和接口ID（Interface ID）两部分。
- **多索引支持**：一个RDMA设备可能拥有多个GID索引（GID Index），可通过参数`rdma_gid_index`指定使用哪个索引，默认为-1即选用最大可用GID Index。

## 应用
- **RDMA连接建立**：在brpc的RDMA握手过程中，通信双方通过已建立的TCP连接交换GID、QPN等参数，然后使用这些参数发起RDMA连接，实现高效的数据传输。
- **网络端点寻址**：在InfiniBand或RoCE网络中，GID作为端点的网络层地址，路由数据包到正确的目的端节点。
- **多路径通信**：当RDMA设备具有多个端口或多个GID时，可支持多路径通信和负载均衡。

## 相关概念
- [[concepts/握手|握手]]
- [[concepts/QP|QP]]
- [[concepts/LID|LID]]
- [[concepts/MaxSge|MaxSge]]

## 相关实体
- [[entities/rdmaendpoint|RdmaEndpoint]]

## 来源提及
- "RDMA连接建立依赖于前置TCP建连，TCP建连后双方交换必要参数，如GID、QPN等，再发起RDMA连接并实现数据传输。" — [[sources/rdma|rdma]]
- "RDMA是硬件相关的通信技术，有很多独特的概念，比如device、port、GID、LID、MaxSge等。" — [[sources/rdma|rdma]]