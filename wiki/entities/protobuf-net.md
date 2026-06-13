---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "protobuf-net"
  - "protobuf net"
  - "protobuf-net.Grpc"
---


# protobuf-net

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
protobuf-net 是面向 .NET 平台的 Protocol Buffers 实现，由 Marc Gravell 创建并维护，代码仓库托管在 https://github.com/mgravell/protobuf-net。该项目在 [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 中注册到的扩展编号（extension number）为 1037。protobuf-net 允许 .NET 开发者通过属性标注（attribute-based）的方式将 C# 类与 protobuf 消息进行映射，从而简化 .NET 应用对 protobuf 序列化与反序列化的集成工作。它是 .NET 生态中应用较早且影响广泛的 protobuf 库之一，与 [[entities/protobuf-csharp-port|protobuf-csharp-port]]、[[entities/Protokt|Protokt]] 等同属 .NET 平台下的 Protocol Buffers 实现。

## 相关实体
- [[entities/protobuf-csharp-port|protobuf-csharp-port]] — Google 官方的 C# Protocol Buffers 移植实现
- [[entities/Protokt|Protokt]] — 另一款面向 Kotlin/JVM 的 Protocol Buffers 实现

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] — Protocol Buffers 全局扩展注册表，分配唯一扩展编号
- [[concepts/custom-options|Custom options]] — Protobuf 自定义选项机制
- [[concepts/extension-numbers|Extension numbers]] — 扩展编号，用于在自定义选项中标识特定扩展

## 来源提及
- `protobuf-net — [[protobuf/options|options]]` — [[sources/options|options]]
- `Website: https://github.com/mgravell/protobuf-net — [[protobuf/options|options]]` — [[sources/options|options]]
- `Extensions: 1037 — [[protobuf/options|options]]` — [[sources/options|options]]