---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [term]
aliases:
  - "失败限制与成功限制"
  - "fail_limit and success_limit"
---


# fail_limit 和 success_limit

## 定义

`fail_limit` 和 `success_limit` 是 [[entities/ParallelChannel|ParallelChannel]]、[[entities/PartitionChannel|PartitionChannel]] 等组合 Channel（Combo Channel）的选项参数，用于控制 RPC 调用的提前结束条件。`fail_limit` 指定允许的最大失败次数，`success_limit` 指定达到目标成功次数即可提前返回。`fail_limit` 的优先级高于 `success_limit`。

## 关键特征

- **提前终止机制**：当失败的 sub channel 访问次数达到 `fail_limit` 时，RPC 会立即终止，不再等待其他 sub channel 的超时。
- **提前成功返回**：当成功的访问次数达到 `success_limit` 时，RPC 也会提前返回，无需等待所有 sub channel 完成。
- **优先级规则**：`fail_limit` 的优先级高于 `success_limit`；只有未设置 `fail_limit` 时，`success_limit` 才会生效。
- **适用场景**：适用于需要组合多个下游服务结果的场景，如并行查询、分片访问、冗余请求等。

## 应用

- **容错性控制**：在 ParallelChannel 中设置 `fail_limit`，可以在部分子请求失败时快速终止整个 RPC 操作，避免不必要的等待和资源浪费。
- **效率优化**：通过 `success_limit` 参数，当足够多的子请求成功返回后即可提前结束，减少等待时间，提升响应速度。
- **灵活调优**：根据不同业务对容错和延迟的容忍度，动态调整 `fail_limit` 和 `success_limit` 的值，以平衡系统可靠性与性能。
- **动态分区降级**：在 PartitionChannel 或 DynamicPartitionChannel 中，通过限定最大失败次数来避免局部故障扩散，提升整体可用性。

## 相关概念

- [[concepts/rpc|RPC]] (远程过程调用)
- [[concepts/timeout|超时控制]]

## 相关实体

- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/PartitionChannel|PartitionChannel]]
- [[entities/DynamicPartitionChannel|DynamicPartitionChannel]]

## 来源提及

- "用户可以设置ParallelChannelOptions.fail_limit来控制访问的最大失败次数，当失败的访问达到这个数目时，RPC会立刻结束而不等待超时。" — [[sources/combo_channel|combo_channel]]
- "用户可以设置ParallelChannelOptions.success_limit来控制访问的最大成功次数，当成功的访问达到这个数目时，RPC会立刻结束。" — [[sources/combo_channel|combo_channel]]
- "ParallelChannelOptions.fail_limit的优先级高于ParallelChannelOptions.success_limit，只有未设置fail_limit时，success_limit才会生效。" — [[sources/combo_channel|combo_channel]]