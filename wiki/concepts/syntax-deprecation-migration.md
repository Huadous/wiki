---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]"]
tags: [method]
aliases:
  - "syntax() migration"
  - "syntax() deprecation"
---


# syntax() deprecation migration

## 定义
syntax() 弃用迁移是提案中提出的从旧的 `FileDescriptor::syntax()` 用法向新聚焦 API 迁移的整体策略与流程。其目标是在保留 proto2/proto3 区分语义的同时，逐步淘汰对 `syntax()` 的直接调用，将调用方引导至语义更精确的替代 API。

## 关键特征
- **三步迁移流程**：(1) 搜索 `syntax()` 的所有调用点；(2) 识别所依赖的 proto2/proto3 区分语义，覆盖四类——UTF-8 验证、封闭/开放枚举、packed 编码、hasbits；(3) 迁移到对应的目标 API（`has_zero_default_value()`、`enforces_utf8()`、`is_closed()` 或已有的 `has_presence()`/`is_packed()`）。
- **显式破坏调用方预期**：迁移完成后，`syntax()` 将被标记为 `ABSL_DEPRECATED` 并返回新的 `Syntax::EDITIONS` 值，以显式破坏那些仍依赖旧语义的调用方。
- **以大型变更（giant CL）配合 Rosie 拆分工具执行**：提案建议通过一个覆盖所有误用实例的大型变更（giant CL）配合 Rosie 拆分工具来执行迁移，以确保迁移的一致性与可追溯性。
- **保留语义而非语法**：迁移不简单地将 `syntax()` 转换为字面值判断，而是先解析出底层真正依赖的语义维度，再映射到等价的聚焦 API。

## 应用
- 在 Protocol Buffers / [[concepts/edition-zero|Edition Zero]] 的 C++ 运行时中，针对 `FileDescriptor::syntax()` 的所有调用点进行系统性替换。
- 帮助 protobuf 的 schema 演进从基于语法（syntax-based）判断过渡到基于特性（feature-based）判断。
- 作为 [[concepts/editions-readme|Protobuf Editions 设计文档索引]]中 C++ API 迁移的具体执行策略的一部分。

## 相关概念
- [[concepts/syntax-editions|Syntax::EDITIONS]]
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/proto3-syntax|proto3 syntax]]
- [[concepts/file-descriptor-copy-heading-to|FileDescriptor::CopyHeadingTo]]
- [[concepts/field-descriptor-has-zero-default-value|FieldDescriptor::has_zero_default_value]]
- [[concepts/field-descriptor-enforces-utf8|FieldDescriptor::enforces_utf8]]
- [[concepts/enum-descriptor-is-closed|EnumDescriptor::is_closed]]
- [[concepts/field-presence|FieldDescriptor::has_presence]]
- [[concepts/is-packed|FieldDescriptor::is_packed]]

## 相关实体
- [[entities/edition-zero|Edition Zero]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/google|Google]]
- [[entities/mcy|mcy]]

## 来源提及
- Once all the "easy" usages are migrated, we will mark `syntax()` as `ABSL_DEPRECATED`. — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]