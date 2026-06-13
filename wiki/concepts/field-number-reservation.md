---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-stricter-schemas-with-editions]]"]
tags: [method]
aliases:
  - "字段号预留"
  - "Field number reservation"
  - "Reserved field numbers"
---


# Field number reservation

## 定义
Field number reservation(字段号预留)是 [[sources/editions-stricter-schemas-with-editions|Editions 收紧 Schema 备忘录]]所建议引入的一种强制性做法:要求每个 message 的第一条 production 必须是 `reserved N to max;`,其中 `N` 表示下一个尚未被使用的字段号。该做法将目前由 `// Next ID: N` 等 linter 惯例所强制执行的"预留下一个未用字段号"规则,提升为 Protobuf 语言层面的硬性约束。文档同时表明,这一机制对 message field 与 enum value 一视同仁地适用。

## 关键特征
- **语言级强制约束**:不再依赖 linter 习惯(如 `// Next ID: N`),而是要求 schema 文本本身显式声明预留区间。
- **固定语法形态**:每个 message 必须以 `reserved N to max;` 作为第一条 production,`N` 为下一个从未被使用过的字段号。
- **统一适用于 message field 与 enum value**:两类需要连续编号的声明均被纳入同一约束。
- **可选的进一步收紧**:文档还讨论了两种可叠加的约束:
  - 要求每一个字段号要么已被使用,要么被显式 `reserved`(即不允许出现"既未使用又未预留"的空洞编号);
  - 要求最大已用字段号之前的所有号码均被 `reserved`(封闭区间预留)。
- **迁移路径明确**:通过 `features.allow_unused_numbers` 这一 edition feature 来完成从现有写法到强制预留写法的迁移,从而在过渡期保持兼容性。

## 应用
- **消除 `// Next ID: N` 的隐性约定**:在没有 linter 介入的项目中,开发者需要手写或维护 Next ID 注释;强制 `reserved N to max;` 之后,该信息被编码进 schema 自身,所有读取 schema 的工具(包括 linter、IDE、文档生成器)都能一致地理解下一个可用号。
- **为 Editions 提供更严格的演进纪律**:在 [[sources/editions|Editions]] 体系下,字段号一旦使用便不应再被复用,且删除字段时必须 `reserved` 旧号。该提案进一步要求把"下一个空号"也一并显式声明,避免多人协作时误用已删除或尚未规划的号。
- **防止 enum 编号的隐式跳跃**:与 message field 类似,enum value 也要求首条 production 为 `reserved N to max;`,从而避免 value 号被静默跳过而不自知。
- **为后续的 feature 切换铺路**:借助 `features.allow_unused_numbers`,旧 schema 可以逐步迁移到新约束,不必一次性改写整个仓库。

## 相关概念
- [[concepts/feature-gating|Feature gating]]
- [[concepts/reserved-keywords|Reserved keywords]]

## 相关实体
- [[entities/protocol-buffers-v3-15-0|protocol-buffers-v3-15-0]]
- [[entities/protocol-buffers-v3-12-0|protocol-buffers-v3-12-0]]
- [[entities/descriptorpool|descriptorpool]]
- [[entities/fieldmask|fieldmask]]

## 来源提及
- There's a few idioms for this checked by linters, such as `// Next ID: N`. We should codify this in the language by rewriting that every message begin with `reserved N to max;`, with the intent that `N` is the next never-used field number. — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]