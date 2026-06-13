---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/implementing_proto3_presence|implementing_proto3_presence]]"
  - "[[protobuf/field_presence.md]]"
tags:
  - "term"
aliases:
  - "proto3 optional"
  - "proto3 可选字段"
  - "`optional` label"
  - "proto3 optional"
  - "proto3 可选字段"
---

## Description
proto3 optional fields 是 protobuf 在 proto3 语法中提供的一种字段存在性（field presence）控制机制。当为 singular 基本类型字段添加 `optional` 标签时，该字段会从默认的无存在（no presence）语义切换为显式存在（explicit presence）语义，与 proto2 中对应的 optional 字段行为完全等价，包括自动生成 `has_foo`、`clear_foo` 等 hazzer 与 clear 方法。实现层面，`optional` 字段在内部被改写为单字段 oneof（synthetic oneof），从而保持与基于反射的算法的向后兼容性，并允许所有代码生成器以与 proto2 一致的方式识别和处理此类字段，同时需抑制合成 oneof 在生成代码中的直接暴露。该特性的演进路径为：v3.12.0 以实验性特性引入（需 `--experimental_allow_proto3_optional` 标志），v3.15.0 起转为默认启用，为稀疏字段、可选配置项、增量更新等需要区分"未设置"与"零值"的场景提供了比 `google.protobuf.*Value` wrapper 类型更高效、更易用的替代方案。

## Related Concepts
- [[concepts/synthetic-oneof|Synthetic Oneof]]
- [[concepts/field-presence|Field Presence]]
- [[concepts/explicit-presence-discipline|Explicit Presence Discipline]]
- [[concepts/no-presence-discipline|No Presence Discipline]]
- [[concepts/hazzer-methods|Hazzer Methods]]
- [[concepts/proto2|proto2]]
- [[concepts/proto3|proto3]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/codegeneratorresponse|CodeGeneratorResponse]]
- [[entities/protoc|protoc]]
- [[entities/protocol-buffers-v3-15-0|protobuf v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|protobuf v3.12.0]]

## Mentions in Source
> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "When a user adds an `optional` field to proto3, this is internally rewritten as a one-field oneof, for backward-compatibility with reflection-based algorithms."
> - "Give `optional` fields like `foo` normal field presence, as described in docs/field_presence."

> **Source: [[sources/field_presence|field_presence]]**
> - "Singular proto3 fields of basic types (numeric, string, bytes, and enums) which are defined with the `optional` label have _explicit presence_, like proto2 (this feature is enabled by default as release 3.15)."
> - "The generated code for proto3 fields with _explicit presence_ (the `optional` label) will be the same as it would be in a proto2 file."