---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options]]"]
tags: [project]
aliases:
  - "DTDL"
  - "Digital Twins Definition Language (DTDL)"
---


# Digital Twins Definition Language

## 基本信息
- Type: project
- Source: [[sources/options]]

## 描述
Digital Twins Definition Language(DTDL)是由 [[entities/protocolbuffersprotobuf|Microsoft Azure]] 主导开发的数字孪生建模语言,用于描述数字孪生模型中的核心概念,包括孪生体(twin)、接口(interface)、属性(property)、遥测(telemetry)、命令(command)与关系(relationship)等。该语言最初以 JSON-LD 作为序列化形式,使 IoT 设备、数字孪生服务与 Azure Digital Twins 服务之间能够以统一的语义进行互操作。在与 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 生态整合的过程中,DTDL 通过 [[concepts/descriptor-proto|descriptor.proto]] 自定义扩展注册了 Protocol Buffers 全局扩展编号 **1183**,以便在 Protobuf 生态中为 DTDL 特有的建模选项保留独立的命名空间。该语言的规范与参考实现托管在 GitHub 的 Azure/opendigitaltwins-dtdl 仓库中,与 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 的扩展机制紧密结合,体现了 Protobuf 扩展机制在跨领域建模语言中的复用能力。

## 相关实体
- [[entities/protocolbuffersprotobuf|protobuf]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[entities/microsoft-azure|Microsoft Azure]] (待创建)

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/json-ld|JSON-LD]] (待创建)
- [[concepts/digital-twin|Digital Twin]] (待创建)

## 来源提及
- "Digital Twins Definition Language (DTDL) — [[sources/options|options]]"
- "Website: https://github.com/Azure/opendigitaltwins-dtdl — [[sources/options|options]]"
- "Extensions: 1183 — [[sources/options|options]]"