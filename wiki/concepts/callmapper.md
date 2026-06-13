---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [method]
aliases:
  - "CallMapper接口"
  - "调用映射器"
---


# CallMapper

## 定义

CallMapper是brpc框架中[[concepts/ParallelChannel|ParallelChannel]]用于将对ParallelChannel的调用转化为对sub channel调用的接口。用户需实现`Map`方法，返回[[concepts/SubCall|SubCall]]对象。若`call_mapper`为NULL，则sub channel直接使用ParallelChannel的请求和响应。

## 关键特征

- **接口化设计**：用户通过实现`Map`方法自定义调用映射逻辑
- **引用计数机制**：CallMapper内含引用计数，一个CallMapper可与多个sub channel关联
- **生命周期管理**：在ParallelChannel析构时，若`call_mapper`不为NULL则自动删除
- **灵活的映射逻辑**：支持广播、请求修改、字段提取等常见模式
- **与ResponseMerger协作**：CallMapper负责修改请求，ResponseMerger负责合并结果

## 应用

- **广播请求（Broadcaster）**：将同一个请求广播到多个sub channel
- **请求修改（ModifyRequest）**：修改请求的某些字段后发送到不同sub channel
- **字段提取（UseFieldAsSubRequest）**：从原始请求中取出某个字段作为子请求发送

## 相关概念

- [[concepts/ParallelChannel|ParallelChannel]]
- [[concepts/ResponseMerger|ResponseMerger]]
- [[concepts/SubCall|SubCall]]

## 相关实体

- [[entities/baidu|baidu]]
- [[concepts/brpc|brpc]]

## 来源提及

- "用户可通过CallMapper修改请求，通过ResponseMerger合并结果。" — [[sources/combo_channel|combo_channel]]
- "CallMapper用于把对ParallelChannel的调用转化为对sub channel的调用。" — [[sources/combo_channel|combo_channel]]
- "如果call_mapper不为NULL，则会在ParallelChannel析构时被删除。call_mapper内含引用计数，一个call_mapper可与多个sub channel关联。" — [[sources/combo_channel|combo_channel]]