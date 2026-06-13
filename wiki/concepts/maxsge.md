---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "Maximum Scatter-Gather Entries"
  - "最大SGE数量"
---


# MaxSge

## 定义

MaxSge是RDMA网卡硬件支持的最大散聚条目（Scatter-Gather Entries，简称SGE）数量。SGE是RDMA数据传输的基本单元，描述一个非连续的内存片段。MaxSge表示在一次send或RDMA写/读操作中，发送描述符（Work Request）可以包含的最大SGE个数，即一次操作最多可以聚合的非连续内存缓冲区的数量上限。

在brpc的RDMA配置中，`rdma_max_sge`参数允许用户设置发送SG列表（SGList）的长度上限，默认值为0，表示采用硬件原生支持的最大长度。

## 关键特征

- **硬件特性参数**：MaxSge值由RDMA网卡硬件决定，在设备初始化阶段通过ibv_query_device或rdma_get_device_info等API从网卡查询获得。
- **影响数据组织能力**：决定了在一次传输操作中可以将多少个物理上不连续的内存块组合成一个逻辑数据包，从而避免额外的数据拷贝。
- **上限约束**：软件层（如brpc）设置的`rdma_max_sge`不能超过硬件报告的MaxSge值，否则请求可能被硬件拒绝或产生未定义行为。
- **传输类型相关性**：不同传输类型（RC、UC、UD等）可能支持不同的MaxSge值，需分别查询。
- **性能权衡**：较大的MaxSge允许更灵活的内存布局，但可能会增加Work Request的处理开销，且硬件实现中SGE数量存在固有限制。

## 应用

- **RPC框架配置**：在brpc等RPC框架中，通过`rdma_max_sge`参数优化RDMA通道的性能，匹配应用层的内存使用模式，减少不必要的内存拼接操作。
- **零拷贝数据传输**：MaxSge足够大时，应用可以直接将分散在不同用户态缓冲区中的数据通过RDMA Wire Protocol发送，无需通过CPU拷贝到连续内存中。
- **大数据块传输**：当传输的数据由多个不连续的子缓冲区组成时，高MaxSge值可以避免将数据重新排列为连续内存块。

## 相关概念

- [[concepts/GID|GID]]
- [[concepts/LID|LID]]
- [[concepts/内存注册|内存注册]]
- [[concepts/solicited标志|solicited标志]]

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/block-pool|block-pool]]
- [[entities/iobuf|iobuf]]

## 来源提及

- "RDMA是硬件相关的通信技术，有很多独特的概念，比如device、port、GID、LID、MaxSge等。" — [[sources/rdma]]
- "rdma_max_sge: 允许的最大发送SGList长度，默认为0，即采用硬件所支持的最大长度。" — [[sources/rdma]]