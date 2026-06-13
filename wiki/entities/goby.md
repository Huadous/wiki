---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Goby Underwater Autonomy Project"
  - "GobySoft"
  - "Goby AUV"
---


# Goby

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Goby 是由 GobySoft 团队主导的水下自主航行器(AUV)开源项目,源代码托管在 GitHub 的 GobySoft/goby 仓库中。该项目注册了 Protocol Buffers 全局扩展编号 1009,用于在其消息传递层中定义自定义选项和扩展字段,以支持水下机器人之间以及与岸基控制站之间的通信。Goby 的核心序列化机制基于 Protocol Buffers,借助其高效的二进制编码能力来满足水下通信链路的带宽与可靠性要求。

除 Goby 本体项目外,GobySoft 团队还开发了 Dynamic Compact Control Language(DCCL,扩展编号 1012),专门用于在水声通信带宽严重受限的环境中以紧凑方式编码控制消息。Goby 项目体现了 Protobuf 扩展机制在海洋科学与自主无人系统领域的实际应用,同时也展示了 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 作为通用序列化框架在专业垂直领域中的可扩展性。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/buf|buf]]
- [[entities/wire|Wire]]
- [[entities/grpc-gateway|gRPC Gateway]]
- [[entities/protoc-gen-validate|protoc-gen-validate]]
- [[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]
- [[entities/nanopb|nanopb]]
- [[entities/scalapb|scalapb]]
- [[entities/protobuf-net|protobuf-net]]
- [[entities/perfetto|Perfetto]]
- [[entities/confluent-schema-registry|Confluent Schema Registry]]

## 相关概念
- Extension numbers
- Custom options
- descriptor.proto
- Protobuf Global Extension Registry
- Wire Format
- Serialization

## 来源提及
- "Goby Underwater Autonomy Project — [[sources/options|options]]"
- "Website: https://github.com/GobySoft/goby — [[sources/options|options]]"
- "Extensions: 1009 — [[sources/options|options]]"