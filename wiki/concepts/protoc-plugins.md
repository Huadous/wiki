---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [method]
aliases:
  - "protoc-gen plugins"
  - "code generator plugins"
  - "Protocol Buffers code generator plugins"
---


# protoc plugins

## 定义
protoc plugins 是 Protocol Buffers 编译器（protoc）生态中用于扩展代码生成能力的可执行程序。此类插件通常命名为 `protoc-gen-xxx` 形式并放置于系统 `PATH` 中，可通过 `--xxx_out` 参数激活。在 protoc 完成 `.proto` 文件解析之后、消费 `descriptor.proto` 元数据的过程中，插件可介入并依据用户自定义选项与消息结构，生成目标语言或目标平台的代码、文档或配置文件。

## 关键特征
- **命名约定**：可执行文件名遵循 `protoc-gen-xxx` 格式，`xxx` 对应 `--xxx_out` 标志中的标识符。
- **PATH 发现机制**：只要可执行文件位于系统 `PATH` 中，protoc 即可自动调用，无需额外注册。
- **基于 descriptor.proto 的输入**：插件读取 `FileDescriptorProto` 等元数据，在 `.proto` 解析之后介入代码生成流程。
- **与扩展机制深度耦合**：多数插件依赖自定义选项（custom options）控制代码生成行为，需在 Protobuf Global Extension Registry 中注册扩展编号。
- **输出多样性**：可生成源代码、API 文档、数据库模式、配置描述等多种目标产物。
- **语言/平台无关**：同一份 `.proto` 文件可经由不同插件生成针对不同运行时或平台的产物。

## 应用
本注册表中包含的 protoc plugins 涵盖多种典型用途，包括但不限于：
- `protoc-gen-bq-schema`：生成 BigQuery 表结构定义。
- `protoc-gen-validate`：生成运行时字段验证代码。
- `protoc-gen-jsonschema`：从 `.proto` 文件生成 JSON Schema。
- `protoc-gen-flowtypes`：生成 Flow 类型定义。
- `protoc-gen-swagger`：生成 Swagger/OpenAPI 接口文档。
- `protoc-gen-psql`：生成 PostgreSQL 数据库模式。
- `protoc-gen-sanitize`：生成输入消毒（sanitization）代码。
- 官方及第三方语言后端插件：例如 PHP 代码生成插件、GWT 代码生成插件（第三方）、Unix Domain RPC 代码生成插件、Object-C 生成插件（Plausible Labs）等。

## 相关概念
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 相关实体
- [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]
- [[entities/cloudstate|Cloudstate]]
- [[entities/kratos|Kratos]]
- [[entities/pigweed|Pigweed]]
- [[entities/google-gnostic|Google Gnostic]]
- [[entities/grpc-federation|gRPC Federation]]
- [[entities/mypy-protobuf|mypy-protobuf]]
- [[entities/ygot|ygot]]
- [[entities/protons|Protons]]
- [[entities/connect|Connect]]
- [[entities/buf|Buf]]

## 来源提及
- "PHP code generator plugin — [[sources/options|options]]" — [[sources/options|options]]
- "GWT code generator plugin (third-party!) — [[sources/options|options]]" — [[sources/options|options]]
- "Unix Domain RPC code generator plugin — [[sources/options|options]]" — [[sources/options|options]]
- "Object-C generator plugin (Plausible Labs) — [[sources/options|options]]" — [[sources/options|options]]