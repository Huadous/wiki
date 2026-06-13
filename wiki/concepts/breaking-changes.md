---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "term"
aliases:
  - "Schema Breaking Changes"
  - "破坏性变更"
  - "API breaking change"
  - "Schema Breaking Changes"
  - "破坏性变更"
---

## Description
"破坏性变更"（Breaking Changes）在 Protobuf Schema 演进体系中具有多层含义。最狭义且最具操作性的定义是：任何会**抬高 schema 最低必需版本（Minimum Required Edition）**的 schema 改动。这一约束基于"最低版本门控"（minimum-version gate）机制——基于更新后 schema 编译得到的 descriptor 在运行时将无法被那些支持的最高版本低于该最低必需版本的旧 runtime 所加载。因此，schema 生产者应将任何提高最低必需版本号的改动视为破坏性变更，因为该改动会阻断已编译 descriptor 的运行时加载。该定义可推广到所有采用"最低版本门控"作为兼容性约束的 schema 演进机制。

除上述"版本门控式"破坏性变更外，"破坏性变更"还涵盖**API 层面的破坏**。一份针对 Proto2 groups 迁移到 Edition 2023 的讨论指出，API breaking change 指对生成语言 API（如方法名、类名或属性拼写）的修改，可能导致已有客户端代码在升级后无法编译或行为异常。即便 Edition 2023 升级的设计初衷是对旧 proto2 groups 保持非破坏性，但跨语言代码生成的不一致性仍可能让生成的 API 出现意外拼写。因此，部分备选方案被批评为"将 2023 升级变成了破坏性变更"，其迁移路径对用户而言不清晰——一旦覆盖某个全局特性（Global Feature）的值，由于该特性同时影响线缆格式与生成 API，便会同时构成"wire-breaking"和"API-breaking"变更，使用户难以平滑升级。这两类破坏性变更虽触发机制不同，但在工程实践中往往需要被一并评估与治理。

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition-total-order|Edition Total Order]]
- [[concepts/wire-format|Wire Format]]
- [[concepts/codegen|Codegen]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/smooth-extension|Smooth Extension]]
- [[concepts/global-feature|Global Feature]]

## 相关实体
- [[entities/descriptor-proto|descriptor.proto]]
- [[entities/file-descriptor-proto|FileDescriptorProto]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及

> **Source: [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]**
> - "Schema producers should consider changes to their schemas that increase the minimum required edition to be breaking changes, since it will stop compiled descriptors from being loaded at runtime."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Turns 2023 upgrade into a breaking change for many languages"
> - "The migration story for users is unclear. Overriding the value of this feature is both a \"wire\"-breaking and API-breaking change they may not be able to do easily."