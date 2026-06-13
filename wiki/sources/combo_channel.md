---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/combo_channel.md]]"
tags: [组合Channel, ParallelChannel, SelectiveChannel, PartitionChannel, DynamicPartitionChannel, CallMapper, ResponseMerger, SubCall, PartitionParser, brpc::ChannelBase, fail_limit和success_limit, 容量计算规则, NamingService（命名服务）, 负载均衡算法（Load Balancer）, ChannelOwnership, 文件命名服务（File Naming Service）]
aliases: ["brpc组合通道文档", "brpc Combo Channel Documentation"]
---

# brpc组合Channel文档 - Summary

## 来源
- Original file: [[brpc/combo_channel.md]]
- Ingested: 2026-06-12

## 核心内容

本文档介绍了[[concepts/组合channel|组合Channel]]在[[entities/brpc|brpc]]框架中的设计与实现，旨在解决复杂RPC调用组合中代码难以同步/异步兼容、不易取消、无法继续组合等问题。brpc提供了四种组合Channel：[[concepts/parallelchannel|ParallelChannel]]（同时访问多个sub channel并合并结果）、[[concepts/selectivechannel|SelectiveChannel]]（按负载均衡算法选择一个sub channel访问）、[[concepts/partitionchannel|PartitionChannel]]（根据命名服务tag自动建立分库sub channel）以及[[concepts/dynamicpartitionchannel|DynamicPartitionChannel]]（支持多种分库方案共存与流量平滑切换）。这些组合Channel统一支持同步/异步、取消、超时等操作，并可通过[[concepts/callmapper|CallMapper]]自定义请求映射、通过[[concepts/responsemerger|ResponseMerger]]自定义结果合并。任何[[concepts/brpcchannelbase|brpc::ChannelBase]]的子类都可参与组合，使得访问模式可以递归嵌套，极大简化了复杂RPC流程的开发。

## 关键实体
- [[entities/brpc|brpc]]：高性能通用RPC框架，提供了组合Channel机制。

## 关键概念
- [[concepts/组合channel|组合Channel]]：将多个Channel以不同方式组合，提供统一接口。
- [[concepts/parallelchannel|ParallelChannel]]：并行访问多个sub channel并合并结果。
- [[concepts/selectivechannel|SelectiveChannel]]：按负载均衡算法从多个sub channel中选择一个访问。
- [[concepts/partitionchannel|PartitionChannel]]：根据tag自动建立分库sub channel。
- [[concepts/dynamicpartitionchannel|DynamicPartitionChannel]]：支持多种分库方案共存和流量平滑切换。
- [[concepts/callmapper|CallMapper]]：将ParallelChannel的请求映射为对sub channel的调用。
- [[concepts/responsemerger|ResponseMerger]]：合并sub channel的响应到总响应。
- [[concepts/subcall|SubCall]]：描述对单个sub channel的调用，含特殊值Bad()和Skip()。
- [[concepts/partitionparser|PartitionParser]]：从命名服务tag解析分区信息。
- [[concepts/brpcchannelbase|brpc::ChannelBase]]：所有Channel类型的基类。
- [[concepts/fail_limit和success_limit|fail_limit和success_limit]]：控制ParallelChannel提前结束的选项。
- [[concepts/容量计算规则|容量计算规则]]：DynamicPartitionChannel用于动态分配流量的递归算法。
- [[concepts/namingservice命名服务|NamingService（命名服务）]]：动态获取服务端地址列表的机制。
- [[concepts/负载均衡算法load-balancer|负载均衡算法（Load Balancer）]]：在多个后端节点间分配请求的策略。
- [[concepts/channelownership|ChannelOwnership]]：指定组合Channel是否拥有sub channel的所有权。
- [[concepts/文件命名服务file-naming-service|文件命名服务（File Naming Service）]]：基于文件的服务发现方式。

## 要点
- 组合Channel抽象统一了同步和异步编程模型，并天然支持取消和继续组合。
- ParallelChannel通过CallMapper和ResponseMerger支持高度自定义的请求分发和结果合并。
- SelectiveChannel实现了机器组间的负载均衡，重试机制独立于sub channel内部重试。
- PartitionChannel和DynamicPartitionChannel简化了分库场景的并行访问。
- DynamicPartitionChannel通过递归容量计算实现多种分库方案的流量平滑切换。
- 所有组合Channel均基于[[concepts/brpcchannelbase|brpc::ChannelBase]]，支持嵌套组合。