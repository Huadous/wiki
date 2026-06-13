---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "is_edition 标志位"
  - "is_edition flag"
---


# is_edition bit

## 定义
is_edition bit 是 [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]] 提案中为 `RawMessageInfo` 编码新引入的标志位。该标志位占用 flags 中当前未被使用的位（`flags & 0x4`），用于标识消息是否采用 Editions 语法，对应 [[concepts/ProtoSyntax|ProtoSyntax]] 枚举中新增的 `EDITIONS` 选项。

## 关键特征
- 占据 flags 字段中原先未使用的位 `0x4`（即 `flags & 0x4`）。
- 用于在 `RawMessageInfo` 编码层面区分消息使用的是 Editions 语法还是传统的 proto2/proto3 语法。
- 与现有的 `is_proto2` 位（`flags & 0x1`）和 `is_message` 位（`flags & 0x2`）并列存在，扩展 flags 的语义表达。
- 是将 [[concepts/Editions|Editions]] 引入 Java Lite 运行时迁移方案中的关键新增项，使现有 [[concepts/RawMessageInfo|RawMessageInfo]] 编码能够与 [[concepts/Editions|Editions]] 兼容。

## 应用
- 在 Java Lite 运行时解析 `RawMessageInfo` 时，通过检查 `is_edition` 位决定走 Editions 解析路径还是传统 proto2/proto3 解析路径。
- 作为[[concepts/Editions|Editions]]与[[concepts/Editions Zero Features|Editions Zero Features]]等迁移策略在编码层面的基础支持，使得旧式 `MessageInfo` 编码在不做破坏性变更的前提下能够表达新的语法版本。
- 为[[entities/Java Lite|Java Lite]]在保持向后兼容的同时支持 [[concepts/Editions|Editions]] 语法提供判别依据。

## 相关概念
- [[concepts/is_proto3 bit|is_proto3 bit]]
- [[concepts/ProtoSyntax|ProtoSyntax]]
- [[concepts/RawMessageInfo|RawMessageInfo]]
- [[concepts/Editions|Editions]]
- [[concepts/Editions Zero Features|Editions Zero Features]]

## 相关实体
- [[entities/Java Lite|Java Lite]]

## 来源提及
- `RawMessageInfo` should be augmented with an additional `is_edition` bit in flags' unused bits. — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- `flags & 0x1 = is proto2?`, `flags & 0x2 = is message?`, `flags & 0x4 = is edition?` — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]