---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [method]
aliases:
  - "Response合并器"
  - "响应合并器"
  - "ResponseMerger接口"
---


# ResponseMerger

## 定义
ResponseMerger是ParallelChannel中用于将各个sub channel的响应合并到总响应中的接口。当该接口为NULL时，使用默认的MergeFrom行为（除repeated字段合并外，其余字段覆盖）。用户可通过自定义实现以达到更复杂的合并逻辑。ResponseMerger内含引用计数，在ParallelChannel析构时被自动删除。

## 关键特征
- **合并接口**：作为ParallelChannel的核心组件，负责将多个sub channel的response合并到总的response中。
- **默认行为**：当ResponseMerger为NULL时，使用`response->MergeFrom(*sub_response)`，即除了repeated字段合并外，其余字段覆盖。
- **自定义扩展**：用户可实现自定义的ResponseMerger以支持复杂的合并策略。
- **执行模型**：ResponseMerger是逐个执行的，因此无需考虑并发合并问题。
- **返回值语义**：合并结果包括`MERGED`（成功合并）、`FAIL`（sub_response合并失败，计入一次失败计数）、`FAIL_ALL`（直接结束整个RPC调用）。
- **引用计数与生命周期**：内含引用计数管理，一个ResponseMerger可与多个sub channel关联，并在ParallelChannel析构时被自动删除。

## 应用
- **组合服务调用**：在ParallelChannel中，将多个下游服务的响应合并为一个统一响应，适用于扇出（fan-out）调用场景。
- **自定义合并策略**：当默认的MergeFrom行为不满足业务需求（如需要聚合统计、过滤重复数据等）时，通过实现自定义ResponseMerger来定制合并逻辑。
- **错误处理**：通过`FAIL`和`FAIL_ALL`返回值控制合并过程中的错误处理策略，实现部分失败容忍或快速失败。

## 相关概念
- [[concepts/ParallelChannel|ParallelChannel]]
- [[concepts/CallMapper|CallMapper]]
- [[concepts/SubCall|SubCall]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "用户可通过CallMapper修改请求，通过ResponseMerger合并结果。" — [[sources/combo_channel|combo_channel]]
- "response_merger把sub channel的response合并入总的response，其为NULL时，则使用response->MergeFrom(*sub_response)，MergeFrom的行为可概括为'除了合并repeated字段，其余都是覆盖'。" — [[sources/combo_channel|combo_channel]]
- "response_merger在ParallelChannel析构时被删除。response_merger内含引用计数，一个response_merger可与多个sub channel关联。" — [[sources/combo_channel|combo_channel]]
- "Result的取值有：MERGED: 成功合并。FAIL: sub_response没有合并成功，会被记作一次失败。" — [[sources/combo_channel|combo_channel]]