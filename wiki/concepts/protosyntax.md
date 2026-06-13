---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"]
tags: [term]
aliases:
  - "ProtoSyntax 枚举"
  - "ProtoSyntax enum"
---


# ProtoSyntax

## 定义
`ProtoSyntax` 是 Java Lite 中用于表示 `.proto` 文件所声明的协议语法的枚举类型。当前已包含 `PROTO2` 与 `PROTO3` 两项。提案建议在该枚举中新增 `EDITIONS` 选项，以便运行时在解析 `MessageInfo` 时能够正确选择与 Editions 兼容的代码路径。

## 关键特征
- 是 Java Lite 中表达 `.proto` 文件所声明协议语法的枚举类型
- 现有取值：`PROTO2`、`PROTO3`
- 提案新增取值：`EDITIONS`，由 `RawMessageInfo` flags 中的 `is_edition` 位（`flags & 0x4`）决定
- 新增的 `EDITIONS` 选项用于替代现有依赖 `is_proto3` 推导 PROTO2/PROTO3 的方式
- 在 Editions Zero 阶段，无需在 `RawMessageInfo` 中显式编码原始 editions 字符串或 features 列表，resolved features 已在字段条目中以独立位表示

## 应用
- 用于在运行时区分 `.proto` 文件声明的协议语法版本（PROTO2、PROTO3 或 Editions）
- 在 Java Lite 解析 `MessageInfo` 时，根据 `is_edition` 位正确选择与 Editions 兼容的解析代码路径
- 为 Java Lite 引入 Editions 支持提供基础的语法类型判定机制

## 相关概念
- [[concepts/Editions|Editions]]
- [[concepts/RawMessageInfo|RawMessageInfo]]
- [[concepts/is_edition-bit|is_edition bit]]
- [[concepts/is_proto3-bit|is_proto3 bit]]

## 相关实体
- No related entities

## 来源提及
- The decoded `ProtoSyntax` should add a corresponding Editions option based on this bit. — [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]
- ```
public enum ProtoSyntax
  PROTO2;
  PROTO3;
  EDITIONS;
— [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]