---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [term]
aliases:
  - "ChannelBase"
  - "brpc Channel 基类"
---


# brpc::ChannelBase

## 定义
brpc::ChannelBase 是 brpc 框架中所有 Channel 类型的抽象基类，定义了统一的 RPC 访问接口 `CallMethod`，支持同步、异步、取消和超时等基本操作。任何继承自 brpc::ChannelBase 的子类均可作为组合 Channel 的 sub channel。

## 关键特征
- 提供统一的 `CallMethod` 接口，是所有 RPC 调用的入口点
- 支持同步调用、异步调用、取消操作和超时设置
- 作为组合 Channel（如 ParallelChannel、SelectiveChannel）的可添加子类基础
- 继承机制允许无限嵌套组合 Channel，实现复杂访问模式
- 与普通 Channel 不同，组合 Channel 的 `Init` 方法通常不需要指定命名服务

## 应用
- 作为 ParallelChannel 的 sub channel，实现并行 RPC 调用
- 作为 SelectiveChannel 的 sub channel，实现动态选择后端服务器的访问逻辑
- 与 PartitionChannel、DynamicPartitionChannel 配合，实现数据分片访问
- 支持用户自定义 Channel 类型，扩展 brpc 的通信能力

## 相关概念
- [[concepts/CallMapper|CallMapper]]
- [[concepts/ResponseMerger|ResponseMerger]]
- [[concepts/SubCall|SubCall]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/SelectiveChannel|SelectiveChannel]]
- [[entities/PartitionChannel|PartitionChannel]]
- [[entities/DynamicPartitionChannel|DynamicPartitionChannel]]

## 来源提及
- "任何brpc::ChannelBase的子类都可以加入ParallelChannel，包括ParallelChannel和其他组合Channel。" — [[sources/combo_channel|combo_channel]]
- "任何brpc::ChannelBase的子类都可加入SelectiveChannel，包括SelectiveChannel和其他组合Channel。" — [[sources/combo_channel|combo_channel]]
- "SelectiveChannel的初始化和普通Channel基本一样，但Init不需要指定命名服务，因为SelectiveChannel通过AddChannel动态添加sub channel，而普通Channel通过命名服务动态管理server。" — [[sources/combo_channel|combo_channel]]