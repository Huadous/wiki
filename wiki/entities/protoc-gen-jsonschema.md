---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "protoc-gen-jsonschema"
  - "chrusty/protoc-gen-jsonschema"
  - "Protobuf JSON Schema 生成插件"
---


# protoc-gen-jsonschema

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
protoc-gen-jsonschema 是一个 protoc 编译器插件，由 chrusty 开发并开源维护，代码仓库位于 https://github.com/chrusty/protoc-gen-jsonschema。该插件能够将 Protocol Buffers（protobuf）模式定义自动转换为对应的 JSON Schema 文档，从而在保持单一数据源（protobuf IDL）的前提下，方便地为各类下游消费方提供结构化数据契约。

在 [[sources/options|options]] 文档列出的 Protobuf Global Extension Registry（Protobuf 全局扩展注册表）中，protoc-gen-jsonschema 占用了扩展编号 1125-1129 区间，与 [[entities/grpc-gateway|grpc-gateway]]、[[entities/protoc-gen-openapi|protoc-gen-openapi]]、[[entities/protoc-gen-validate|protoc-gen-validate]] 等同类工具并列登记。该工具的典型应用场景包括 OpenAPI 规范集成、Web 客户端类型生成以及 API 文档工具链的自动化构建。

通过 protoc-gen-jsonschema，开发者可以让基于 protobuf 定义的服务同时生成符合 JSON Schema 标准的描述文件，便于与 REST/JSON 风格的 API 网关、文档生成器以及前端代码生成器进行衔接。

## 相关实体
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/protoc-gen-openapi|protoc-gen-openapi]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- Protoc-gen-jsonschema — [[sources/options|options]]
- Website: https://github.com/chrusty/protoc-gen-jsonschema — [[sources/options|options]]
- Extension: 1125-1129 — [[sources/options|options]]