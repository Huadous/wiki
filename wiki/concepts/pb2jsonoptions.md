---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/json2pb|json2pb]]"]
tags: [term]
aliases:
  - "Pb2JsonOptions.enum_options"
  - "json2pb配置选项"
---


# Pb2JsonOptions

## 定义
Pb2JsonOptions 是 brpc 的 json2pb 模块中用于控制 protobuf 到 JSON 转换行为的配置对象/选项集合。它通过提供多项可调选项来影响序列化过程，使开发者能够根据服务需求调整输出格式与可读性之间的平衡。

## 关键特征
- 作为 json2pb 模块中的配置接口，集中管理 protobuf → JSON 序列化时的各项行为选项
- 最核心的子选项为 `enum_options`，用于决定 enum 类型字段的转换形式
- 默认行为：将 enum 转换为其名字对应的字符串（如 `"ENUM_VALUE"`），提升输出可读性
- 可配置行为：通过选项切换为直接将 enum 转换为对应的整数值
- 提供灵活且可定制的 JSON 序列化策略，是 brpc 实现可调序列化行为的关键配置入口

## 应用
- 在 brpc 服务中需要以 JSON 形式对外暴露 protobuf 消息时，控制序列化输出格式
- 当下游消费者更易于处理数字时，将 enum 序列化为整数值以减小负载、简化解析
- 当调试、日志可读性或人工排查为首要诉求时，保留 enum 字符串形式的默认行为
- 在同一系统中为不同接口/服务定制差异化的 JSON 输出策略

## 相关概念
- [[concepts/json-protobuf-conversion-rules|JSON-protobuf转换规则]]
- [[concepts/enum-conversion|enum转换]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/json2pb|json2pb]]

## 来源提及
- "enum可转化为整数或其名字对应的字符串，可由Pb2JsonOptions.enum_options控制。默认后者。" — [[sources/json2pb|json2pb]]