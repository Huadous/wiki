---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [method]
aliases:
  - "Edition 宣告"
  - "Edition announcement"
  - "Proclamation"
---


# Edition Proclamation

## 定义
Edition Proclamation（Edition 宣告）是 protobuf-team 发布新 edition 的标准化流程。该流程规定了从预告到正式生效的完整路径，确保开源社区与各语言后端能够协调一致地支持新版本的 edition。

## 关键特征
- **两步骤流程**：第一步提前数月向开源社区宣告即将到来的 edition，并给出 protoc 接受新 edition 的非破坏性发布日期；第二步在该发布日附近，希望更改默认值的各后端发布添加新 edition 支持的版本。
- **承诺性节奏**：protobuf-team 承诺每个日历年度至少宣告一个 edition，即使第一方后端不使用该 edition。
- **发布后含义稳定**：edition 的含义在发布后通常不应有大的变化；若含义需调整，应通过后续的 Y.1、Y.2 等次版本进行处理。
- **非破坏性接入**：protoc 接受新 edition 的版本被设计为非破坏性变更，以降低上游集成的风险。
- **多后端协调**：宣告面向所有希望更改默认值的后端，后端在该发布日附近自行发布支持版本。

## 应用
- **Protobuf 语言后端协调**：用于 C++、Java、Python、Go 等各语言官方运行时，使其在约定时间窗口内统一跟进新 edition 的支持。
- **开源社区预告**：为社区贡献者、第三方工具维护者提供提前规划与适配的时间窗口。
- **默认值演进管理**：作为调整 edition 行为默认值（如字段存在性、字段默认值等）的标准化引入机制。
- **Edition 迭代节奏保障**：保证即使在某些年份第一方后端无明确需求时，Edition 体系也能持续向前演进。

## 相关概念
- [[concepts/edition|Edition]]
- [[concepts/total-ordering-of-editions|Total Ordering of Editions]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protoc|protoc]]

## 来源提及
- "Proclamation" is done via a two-step process: first, we announce an upcoming edition some months ahead of time to OSS, and give an approximate date on which we plan to release a non-breaking version that causes protoc to accept the new edition. — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]