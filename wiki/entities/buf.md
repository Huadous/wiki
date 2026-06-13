---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Buf"
  - "buf.build"
  - "Buf CLI"
---


# Buf

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Buf 是现代 Protobuf 工具链，提供模式管理、linting、breaking change 检测以及代码生成等功能，官方网站为 http://buf.build/。它在 [[sources/options|Protobuf 全局扩展注册表]] 中占用了一组连续的扩展编号 1157-1166，是分配扩展较多的项目之一。Buf 通过其构建系统（例如 [[entities/butil|bufbuild/protoc-gen-validate]] 等工具）显著提升了 Protobuf 在大型组织中的工程化使用体验。Buf 与 [[entities/grpc-gateway|grpc-gateway]]、Connect 等 RPC 生态紧密集成，共同构成现代 Protobuf 工程化体系。

## 相关实体
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/butil|bufbuild/protoc-gen-validate]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- Buf — [[sources/options|options]]
- Website: http://buf.build/ — [[sources/options|options]]
- Extension: 1157-1166 — [[sources/options|options]]