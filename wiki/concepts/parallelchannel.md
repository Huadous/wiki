---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/combo_channel]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bthread_or_not.md]]"
tags:
  - "method"
aliases:
  - "并行 Channel"
  - "组合 Channel"
  - "Parallel Channel"
  - "PartitionChannel"
  - "并行 Channel"
  - "组合 Channel"
  - "Parallel Channel"
---

## Related Concepts
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/redis协议|Redis 协议]]
- [[concepts/bthread|bthread]]
- [[concepts/combo-channel组合通道|组合Channel]]
- [[concepts/selectivechannel|SelectiveChannel]]
- [[concepts/callmapper|CallMapper]]
- [[concepts/responsemerger|ResponseMerger]]
- [[concepts/subcall|SubCall]]
- [[concepts/partitionchannel|PartitionChannel]]
- [[concepts/partitionparser|PartitionParser]]
- [[concepts/dynamicpartitionchannel|DynamicPartitionChannel]]
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/异步调用|异步调用]]
- [[concepts/异步接口|异步接口]]
- [[concepts/组合访问|组合访问]]
- [[concepts/半同步|半同步]]
- [[concepts/channel|Channel]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-channel|brpc::Channel]]

## Mentions in Source
> **Source: [[sources/en_redis_client|en_redis_client]]**
> - "Support ParallelChannel etc to define access patterns declaratively."

> **Source: [[sources/combo_channel|combo_channel]]**
> - "ParallelChannel（有时被称为"pchan"）同时访问其包含的sub channel，并合并它们的结果。用户可通过CallMapper修改请求，通过ResponseMerger合并结果。"
> - "任何brpc::ChannelBase的子类都可以加入ParallelChannel，包括ParallelChannel和其他组合Channel。"
> - "用户可以设置ParallelChannelOptions.fail_limit来控制访问的最大失败次数，当失败的访问达到这个数目时，RPC会立刻结束而不等待超时。"
> - "一个sub channel可多次加入同一个ParallelChannel。当你需要对同一个服务发起多次异步访问并等待它们完成的话，这很有用。"
> - "PartitionChannel是特殊的ParallelChannel，它会根据命名服务中的tag自动建立对应分库的sub channel。"
> - "ParititonChannel只能处理一种分库方法，当用户需要多种分库方法共存，或从一个分库方法平滑地切换为另一种分库方法时，可以使用DynamicPartitionChannel。"
> - "首先定制PartitionParser。这个例子中tag的形式是N/M，N代表分库的index，M是分库的个数。比如0/3代表一共3个分库，这是第一个。"
> - "如果分库在不同的命名服务内，那么用户得自行用ParallelChannel组装，即每个sub channel对应一个分库（使用不同的命名服务）。"

> **Source: [[sources/en_client|en_client]]**
> - "NOTE: ParallelChannel is probably more convenient to launch multiple RPCs in parallel."

> **Source: [[sources/client|client]]**
> - "注意：当你需要发起多个并发操作时，可能[ParallelChannel](combo_channel.md#parallelchannel)更方便。"

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "启动多个bthread各自执行同步RPC后挨个join bthreads。"
> - "这儿是为了和bthread对比，实现中我们建议你使用ParallelChannel，而不是自己Join"
> - "如果仅仅是为了并发RPC，别用bthread。"