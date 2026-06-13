---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [term]
aliases:
  - "synthetic nested message"
  - "synthetic message"
---


# Synthetic message

## 定义
A synthetic message is a protoc-generated nested message that proto2 automatically creates to represent a group field. The generated message type name matches the capitalized group name, and the corresponding field name is fully lowercased. This generation was implicit in the proto2 compilation pipeline and underlay the standard group behavior in that syntax.

## 关键特征
- Generated automatically by protoc during proto2 compilation; the user does not declare it directly.
- Type name is equivalent to the capitalized group name; field name is the fully lowercased form of the group name, so type and field names are guaranteed to be synchronized.
- The transformation from a group field to its synthetic message form is irreversible in the general case — only single-word group names can be unambiguously recovered from the synthetic message.
- In Edition 2023, the language has removed synchronized synthetic message generation: users now explicitly define messages and mark any field as DELIMITED instead.
- Codegen tools and text-format parsing tools relied on this mechanism for years; removing it breaks long-standing assumptions about how group fields appear in generated code.

## 应用
- Describing the historical proto2 behavior where every group field was internally compiled into a nested message, so generated code and text-format parsers can be understood in terms of that internal model.
- Analyzing the migration impact when moving proto2 schemas to Edition 2023, where the absence of automatic synthetic message generation changes how group fields are represented.
- Supporting the new DELIMITED-based workflow, in which the user declares the message explicitly and opts any field into delimited encoding without an implicit companion message being synthesized.

## 相关概念
- [[concepts/group-fields|Group fields]]
- [[concepts/delimited-encoding|Delimited encoding]]
- [[concepts/group-like-fields|Group-like fields]]
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/proto2|Proto2]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "Proto2 splits groups into a synthetic nested message with a type name equivalent to the group specification (required to be capitalized), and a field name that's fully lowercased." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- "The problem under edition 2023 is that we've removed the generation of synchronized synthetic messages from the language." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]