---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [term]
aliases:
  - "SubCall"
---


# SubCall

## 定义
SubCall是[[concepts/CallMapper|CallMapper]]的Map方法返回的对象，用于描述对单个sub channel的调用。它封装了method、request、response以及一个flag（如`DELETE_REQUEST`、`DELETE_RESPONSE`等），指示[[concepts/ParallelChannel|ParallelChannel]]在RPC结束后是否需要删除这些对象。SubCall是[[concepts/ParallelChannel|ParallelChannel]]实现的关键数据结构。

## 关键特征
- **方法封装**：包含对sub channel调用的method、request和response对象
- **生命周期标志**：通过flag（如`DELETE_REQUEST`、`DELETE_RESPONSE`）控制资源释放
- **特殊值**：
  - `Bad()`：使本次访问立刻失败，`Controller.ErrorCode()`为`EREQUEST`
  - `Skip()`：跳过该sub channel，如果所有sub channel都被跳过，本次访问失败，`Controller.ErrorCode()`为`ECANCELED`
- **工厂方法**：通常由`CallMapper::Map()`返回，用于构造SubCall实例

## 应用
- **平行通道分发**：在[[concepts/ParallelChannel|ParallelChannel]]中，为每个sub channel创建SubCall对象，实现并行RPC调用
- **错误处理**：通过Bad()和Skip()机制实现条件性的sub channel跳过或快速失败
- **资源管理**：利用flag自动管理request和response对象的生命周期，避免内存泄漏

## 相关概念
- [[concepts/CallMapper|CallMapper]]
- [[concepts/ParallelChannel|ParallelChannel]]

## 相关实体
无

## 来源提及
- "返回的SubCall被用于访问对应sub channel，SubCall有两个特殊值：返回SubCall::Bad()则对ParallelChannel的该次访问立刻失败，Controller.ErrorCode()为EREQUEST。返回SubCall::Skip()则跳过对该sub channel的访问，如果所有的sub channel都被跳过了，该次访问立刻失败，Controller.ErrorCode()为ECANCELED。" — [[sources/combo_channel|combo_channel]]
- "return SubCall(method, request, response->New(), DELETE_RESPONSE);" — [[sources/combo_channel|combo_channel]]