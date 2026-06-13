---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "ipfs-protons"
  - "ipfs/protons"
  - "Protons 代码生成器"
---


# Protons

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Protons 是 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 项目生态中由 IPFS 团队开发的 Protocol Buffers 代码生成器(protoc plugin),代码托管在 GitHub 的 `ipfs/protons` 仓库中。该项目在 [[sources/options|Protobuf Global Extension Registry]] 中注册了扩展编号 1186,用于声明 IPFS 协议相关的自定义选项与字段约束。Protons 能够从 `.proto` 文件生成 JavaScript、TypeScript 以及 Go 等多种语言的消息类,使 IPFS 生态系统的各个组件(包括 libp2p、IPLD、Multiformats 等)能够以统一的序列化格式进行数据交换。Protons 同时支持 proto2 和 proto3 语法,并提供针对 IPFS 去中心化场景优化的字段约束与编解码策略。该项目体现了 Protobuf 作为去中心化 Web 基础设施的序列化标准的核心地位。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]
- [[entities/wire|Square Wire]]
- [[entities/scalapb|scalapb]]
- [[entities/nanopb|nanopb]]
- [[entities/buf|Buf]]
- [[entities/grpc-gateway|grpc-gateway]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/protoc-plugins|protoc plugins]]
- [[concepts/proto3-syntax|proto3 syntax]]
- [[concepts/proto2-syntax|proto2 syntax]]

## 来源提及
- "Protons — [[sources/options|options]]" — [[sources/options|options]]
- "Website: https://github.com/ipfs/protons — [[sources/options|options]]" — [[sources/options|options]]
- "Extensions: 1186 — [[sources/options|options]]" — [[sources/options|options]]