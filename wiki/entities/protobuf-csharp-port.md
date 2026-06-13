---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "C# port of protocol buffers"
  - "protobuf-csharp-port"
---


# protobuf-csharp-port

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
protobuf-csharp-port 是 Protocol Buffers 的 C# 语言端口实现，作为该注册表中第一个注册的项目（扩展编号 1000）。其代码仓库托管在 GitHub 上（https://github.com/jskeet/protobuf-csharp-port），由 Jon Skeet 等人维护。该项目使 .NET 生态系统能够使用 protobuf 进行结构化数据序列化，并通过注册专属扩展编号避免了与其它第三方项目的冲突。该项目是 [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 中最早登记的第三方实现之一，为后续类似项目（如 [[entities/nanopb|nanopb]]、[[entities/protobuf-net|protobuf-net]]、[[entities/protobuf-c|protobuf-c]]、[[entities/protokt|Protokt]]）的扩展编号分配提供了先例。

## 相关实体
- [[entities/nanopb|nanopb]]
- [[entities/protobuf-net|protobuf-net]]
- [[entities/protobuf-c|protobuf-c]]
- [[entities/protokt|Protokt]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- "C# port of protocol buffers" — [[sources/options|options]]
- "Website: https://github.com/jskeet/protobuf-csharp-port" — [[sources/options|options]]
- "Extensions: 1000" — [[sources/options|options]]