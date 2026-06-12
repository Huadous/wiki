---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/style]]"]
tags: [term]
aliases:
  - "蛇形命名法"
  - "小写加下划线"
---


# lower_snake_case

## 定义

lower_snake_case 是一种标识符命名风格，使用全小写字母、下划线（`_`）和数字，单词之间用单个下划线分隔。在 [Protocol Buffers](https://protobuf.dev) 样式指南中，包名、字段名（包括扩展字段和 oneof 字段）以及文件名均应使用此命名风格。例如：`package my_package`、字段 `song_name`、文件名 `my_proto.proto`。该命名风格在 C/C++、Python 等编程语言的标准库和社区约定中极为常见。

## 关键特征

- **全小写**：所有字母均为小写（a-z），不使用大写字母。
- **单词分隔**：用单个下划线（`_` 或称为 `snake`）分隔多个单词。
- **允许数字**：可包含数字（0-9）以避免歧义或表达版本、索引等。
- **一致性**：每个单词之间严格使用一个下划线，且首尾不能用下划线（除非表示内部标识符等特殊情况）。
- **与编程语言绑定**：在 C++、Python、Rust、Go 等语言中内置为推荐或强制风格；在 Protobuf 中用于字段名、包名、文件名、oneof 名、扩展名。
- **自动代码生成友好**：由 `.proto` 文件编译生成时可直接对应目标语言的命名风格，无需额外转换。

## 应用

- **Protocol Buffers 模式定义**：定义 `.proto` 文件中的包名、消息字段名、oneof 名、扩展名以及文件名。
- **编程语言标识符**：Python 标准库、C++ STL 以及 Go 语言的变量和函数命名惯例均推荐使用 `lower_snake_case`。
- **数据库与数据模型**：在 JSON Schema、GraphQL Schema 或 API 参数定义中，常通过 `snake_case` 映射后端实现。
- **RPC 服务定义**：在 gRPC/brpc 等框架中，RPC 方法名通常采用 LowerCamelCase，但其中的字段参数名仍采用 `lower_snake_case`。

## 相关概念

- [[concepts/title-case|TitleCase]]（大驼峰式，PascalCase）
- [[concepts/upper-snake-case|UPPER_SNAKE_CASE]]（大写蛇形命名法，用于常量）
- [[concepts/camelcase|camelCase]]（小驼峰式命名）
- [[concepts/package-naming|Package naming]]（包命名约定）
- [[concepts/field-naming|Field naming]]（协议字段命名约定）

## 相关实体

- [[entities/brpc|brpc]]（Apache brpc RPC 框架）
- [[entities/thrift|thrift]]（Apache Thrift，另一种 IDL 与 RPC 框架）

## 来源提及

- "lower_snake_case: Contains lowercase letters, underscores, and numbers; Words are separated by a single underscore." — [[sources/style|Protobuf 样式指南]]
- "Use snake_case for field names, including extensions." — [[sources/style|Protobuf 样式指南]]
- "Use pluralized names for repeated fields." — [[sources/style|Protobuf 样式指南]]
- "Package names should be a dot-delimited sequence of lower_snake_case names." — [[sources/style|Protobuf 样式指南]]