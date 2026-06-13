---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "FedOne"
  - "Google Wave Federation Protocol open-source release"
  - "wave-protocol"
---


# FedOne

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
FedOne 是 Google Wave Federation Protocol 的开源发布版本,网站托管在 Google Code 上的 wave-protocol 项目。该项目源自 Google Wave 实时通信与协作平台,旨在提供一个去中心化的联邦通信协议实现。FedOne 在 2010 年随着 Google Wave 服务的逐步关停而被开源,作为该协议栈最后的开源化身短暂存在。它在 [[protobuf/options|Protocol Buffers 全局扩展注册表]] 中注册了扩展编号 1003,是该注册表中早期注册的第三方项目之一,体现了该注册表对不同领域项目(从企业协作到水下机器人)的广泛覆盖。FedOne 关联的源码与 [[protocolbuffers/protobuf]] 紧密相关,涉及 [[concepts/extension-numbers|扩展编号]]、[[concepts/custom-options|自定义选项]] 以及 [[concepts/descriptor.proto|descriptor.proto]] 等概念。

## 相关实体
- [[entities/protobuf-net|protobuf-net]]
- [[entities/nanopb|nanopb]]
- [[entities/perfetto|perfetto]]
- [[entities/buf|buf]]
- [[entities/wire|wire]]
- [[entities/scalapb|scalapb]]
- [[entities/confluent-schema-registry|confluent-schema-registry]]
- [[entities/grpc-gateway|grpc-gateway]]
- [[entities/connect|connect]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]
- [[entities/protobuf-csharp-port|protobuf-csharp-port]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]

## 来源提及
- Google Wave Federation Protocol open-source release (FedOne) — [[sources/options|options]]
- Website: http://code.google.com/p/wave-protocol — [[sources/options|options]]
- Extensions: 1003 — [[sources/options|options]]