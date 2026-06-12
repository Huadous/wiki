---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [method]
aliases:
  - "分区解析器"
  - "分区解析接口"
---


# PartitionParser

## 定义

PartitionParser 是 [[concepts/PartitionChannel|PartitionChannel]] 和 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]] 使用的接口，用于从命名服务的 tag 中解析出分区信息。用户必须实现 `ParseFromTag` 方法，将字符串格式的 tag 转换为 `Partition` 结构体（包含 `index` 和 `num_partition_kinds`），例如将 tag `"0/3"` 解析为表示共 3 个分库中的第 0 个分区。定制 `PartitionParser` 是使用 [[concepts/PartitionChannel|PartitionChannel]] 或 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]] 的前置必要步骤。

## 关键特征

- **接口定义**：包含 `bool ParseFromTag(const std::string& tag, brpc::Partition* out)` 纯虚方法，用户需实现自定义解析逻辑。
- **输入输出**：输入为字符串 `tag`（来自命名服务），输出为 `brpc::Partition` 结构体（包含 `index` 和 `num_partition_kinds` 字段）。
- **灵活性**：支持任意 tag 格式，典型模式如 `"N/M"`（N 为分库索引，M 为分库总数）。
- **前提性**：在使用 [[concepts/PartitionChannel|PartitionChannel]] 或 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]] 之前必须先完成 `PartitionParser` 的定制。
- **与 DynamicPartitionChannel 的区别**：使用 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]] 时，`PartitionParser` 的初始化不需要 `num_partition_kinds` 参数，分区数量可动态变化。

## 应用

- **水平分库场景**：当后端服务通过命名服务返回分库 tag（如 `"0/3"`）时，`PartitionParser` 解析出具体分区信息，使客户端能够准确路由到对应的分库实例。
- **动态分区调整**：结合 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]]，可在分区数量动态变化（如扩缩容）时自动适配，无需重启客户端。
- **自定义分区策略**：用户可根据业务需求定制 tag 解析规则，例如支持 `"shard_2_of_8"` 或 `"zone=3;total=5"` 等复杂格式。

## 相关概念

- [[concepts/PartitionChannel|PartitionChannel]]
- [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]]

## 相关实体

- [[entities/brpc|brpc]]

## 来源提及

- "首先定制PartitionParser。这个例子中tag的形式是N/M，N代表分库的index，M是分库的个数。比如0/3代表一共3个分库，这是第一个。" — [[sources/combo_channel|combo_channel]]
- "bool ParseFromTag(const std::string& tag, brpc::Partition* out) { ... }" — [[sources/combo_channel|combo_channel]]
- "DynamicPartitionChannel的使用方法和PartitionChannel基本上是一样的，先定制PartitionParser再初始化，但Init时不需要num_partition_kinds" — [[sources/combo_channel|combo_channel]]