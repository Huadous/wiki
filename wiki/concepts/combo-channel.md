---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/combo_channel]]"
  - "[[brpc/bthread_or_not.md]]"
tags:
  - "term"
aliases:
  - "组合通道"
  - "combo channels"
  - "组合Channel"
  - "组合通道"
  - "combo channels"
  - "DynamicPartitionChannel"
  - "组合通道"
  - "combo channels"
  - "组合Channel"
  - "组合通道"
  - "combo channels"
  - "组合访问"
  - "组合通道"
  - "combo channels"
  - "组合Channel"
  - "组合通道"
  - "combo channels"
  - "DynamicPartitionChannel"
  - "组合通道"
  - "combo channels"
  - "组合Channel"
  - "组合通道"
  - "combo channels"
---

## Description
组合访问是 brpc 中用于简化和组织复杂 RPC 客户端调用模式的核心机制。由于异步代码编写难度较大，brpc 提供了组合访问来简化问题：通过组合不同的 channel，开发者可以声明式地执行复杂的访问，而不用太关心其中的细节。该机制涵盖了多种具体实现：[[concepts/parallel-channel|ParallelChannel]]（同时访问其包含的 sub channel，并合并它们的结果）、[[concepts/selective-channel|SelectiveChannel]]（按负载均衡算法在多个 sub channel 间分配流量）、[[concepts/partition-channel|PartitionChannel]]（处理单一分库方法）以及 [[concepts/dynamic-partition-channel|DynamicPartitionChannel]]（支持多种分库方法共存并平滑切换，按每种分库方式的容量动态切分流量）。除基于 channel 的组合外，brpc 还提供了 [[concepts/execution-queue|ExecutionQueue]] 作为基于 bthread 的线程池替代方案，进一步丰富了组合访问的并行控制能力。开发者可以根据业务场景选择同步、异步、半同步访问方式，或使用组合 channel 来声明式地简化分片或并行访问。

## Related Concepts
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/rpc|RPC]]
- [[concepts/parallel-channel|ParallelChannel]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/partition-channel|PartitionChannel]]
- [[concepts/dynamic-partition-channel|DynamicPartitionChannel]]
- [[concepts/call-mapper|CallMapper]]
- [[concepts/response-merger|ResponseMerger]]
- [[concepts/execution-queue|ExecutionQueue]]
- [[concepts/bthread|bthread]]
- 异步接口（Async Interface）
- 分片（Sharding）
- 并行访问

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "or use combo channels to simplify sharded or parallel accesses declaratively."
> - "Clients can access servers synchronously, asynchronously, semi-synchronously, or use combo channels to simplify sharded or parallel accesses declaratively."

> **Source: [[sources/combo_channel|combo_channel]]**
> - "这种channel在brpc中被称为组合channel。"
> - "ParallelChannel（有时被称为"pchan"）同时访问其包含的sub channel，并合并它们的结果。"
> - "SelectiveChannel（有时被称为"schan"）按负载均衡算法访问其包含的Channel，相比普通Channel它更加高层：把流量分给sub channel，而不是具体的Server。"
> - "ParititonChannel只能处理一种分库方法，当用户需要多种分库方法共存，或从一个分库方法平滑地切换为另一种分库方法时，可以使用DynamicPartitionChannel。"
> - "DynamicPartitionChannel的使用方法和PartitionChannel基本上是一样的，先定制PartitionParser再初始化，但Init时不需要num_partition_kinds，因为DynamicPartitionChannel会为不同的分库方法动态建立不同的sub PartitionChannel。"
> - "DynamicPartitionChannel的容量等于它其中Sub PartitionChannel的容量之和。"
> - "在真实的线上环境中，我们会逐渐地增加4分库的server，同时下掉3分库中的server。DynamicParititonChannel会按照每种分库方式的容量动态切分流量。"

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "不过异步代码还是很难写的，所以我们提供了组合访问来简化问题，通过组合不同的channel，你可以声明式地执行复杂的访问，而不用太关心其中的细节。"