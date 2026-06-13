---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options]]"]
tags: [standard]
aliases:
  - "Global Extension Registry"
  - "Protocol Buffers 扩展注册表"
  - "descriptor.proto 扩展登记表"
---


# Protobuf Global Extension Registry

## 定义
Protobuf Global Extension Registry（Protocol Buffers 全局扩展注册表）是由 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 项目维护的中央注册表，用于登记所有第三方项目为 `descriptor.proto` 注册的扩展编号。其核心目的是防止不同第三方项目在为 protobuf 自定义选项申请扩展编号时发生冲突。

## 关键特征
- **集中协调**：由 Protocol Buffers 官方项目集中维护，作为跨项目编号分配的权威来源。
- **冲突防范**：确保任意开发者同时使用多个带有各自扩展的第三方项目时，扩展编号不会发生碰撞。
- **编号分配起点**：注册表从编号 1000 开始分配，预留较低编号供官方内部使用。
- **开放申请流程**：开发者可通过提交 Pull Request 或创建 Issue 的方式申请新的扩展编号。
- **覆盖广泛**：截至当前，注册表已涵盖编号至 1190 以上的多个第三方项目。
- **基础设施定位**：是 protobuf 生态系统中跨项目协调的核心基础设施之一。

## 应用
- **第三方项目注册扩展编号**：任何需要在 `descriptor.proto` 中定义自定义选项的 protobuf 第三方工具或框架，都需先在此注册表登记所申请的扩展编号，以避免冲突。
- **自定义选项开发**：开发 protobuf 自定义选项（Custom options）时，开发者查询该注册表以确认目标编号未被占用，并按流程申请新编号。
- **Protobuf 工具链生态协调**：被 [[entities/buf|Buf]]、[[entities/protoc-gen-validate|protoc-gen-validate]]、[[entities/grpc-federation|grpc-federation]] 等大量依赖 protobuf 自定义选项的项目作为参考基础设施。
- **gRPC 与 API 网关集成**：包括 [[entities/grpc-federation|grpc-federation]]、grpc-gateway 等项目在为自定义选项选择编号时遵循该注册表。

## 相关概念
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/descriptor-proto|descriptor.proto]]

## 相关实体
- [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]]
- [[entities/buf|buf]]
- [[entities/grpc-federation|grpc-federation]]

## 来源提及
- "This file contains a global registry of known extensions for descriptor.proto, so that any developer who wishes to use multiple 3rd party projects, each with their own extensions, can be confident that there won't be collisions in extension numbers." — [[sources/options|options]]