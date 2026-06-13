---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [term]
aliases:
  - "protobuf custom options"
  - "Protocol Buffers 自定义选项"
  - "Custom Options"
---


# Custom options

## 定义
Custom options（自定义选项）是 Protocol Buffers 提供的一种扩展机制，允许开发者为 proto 文件中的元素（消息、字段、服务、方法、枚举值等）添加自定义注解。该机制基于 `descriptor.proto` 中 `ExtensionRange`（扩展范围）的实现，使第三方工具能够在不修改 protobuf 核心代码的前提下增强 proto 文件的语义表达。每个自定义选项都对应一个全局唯一的扩展编号（extension number），由 [[concepts/Extension numbers|Extension numbers]] 进行管理，并在 [[concepts/Protobuf Global Extension Registry|Protobuf Global Extension Registry]] 中登记。

## 关键特征
- 基于 `descriptor.proto` 中的 `ExtensionRange` 实现，proto 文件中几乎所有可声明的元素（message、field、service、method、enum value、oneof 等）均支持扩展。
- 每一个自定义选项必须分配一个全局唯一的 extension number，避免与官方选项及其他第三方选项冲突。
- 通过扩展机制注入，不修改 protobuf 核心代码即可增加新的语义注解。
- 自定义选项本身也是 proto 消息，因此可嵌套、组合使用，并可定义多种数据类型（标量、消息、枚举、repeated 等）。
- 由 protoc 编译时解析并写入 `FileDescriptorProto` 等描述符，运行时和工具链可读取。

## 应用
- **API 网关与路由**：在 service 或 method 上附加网关配置注解，控制路由、超时、鉴权等行为。
- **代码生成器增强**：protoc 插件读取自定义选项，生成特定语言或框架的胶水代码（如 gRPC stub、OpenAPI 文档、ORM 模型等）。
- **数据校验**：[`protoc-gen-validate`](https://github.com/bufbuild/protoc-gen-validate)（[[entities/protoc-gen-validate|protoc-gen-validate]]）通过 field 上的选项注解实现参数校验规则（如范围、长度、正则等）。
- **构建与 lint 工具**：[`Buf`](https://buf.build)（[[entities/buf|buf]]）等工具利用自定义选项来标注模块（module）、许可（license）、所有权（ownership）等元信息，支持 lint 与 breaking 检查。
- **API 治理与文档生成**：附加 OpenAPI、GraphQL、AsyncAPI 等规范所需的额外元数据，用于自动生成跨语言 API 文档。
- **协议版本控制**：在消息或字段上标记稳定性（stable、beta、experimental）、废弃（deprecated）信息，辅助 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 的版本演进。

## 相关概念
- [[concepts/Protobuf Global Extension Registry|Protobuf Global Extension Registry]]
- [[concepts/Extension numbers|Extension numbers]]
- [[concepts/descriptor.proto|descriptor.proto]]

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/buf|buf.build]]

## 来源提及
- "If you need an extension number for your custom option (see custom options), please send us a pull request to add an entry to this doc, or create an issue with info about your project (name and website) so we can add an entry for you." — [[sources/options|options]]