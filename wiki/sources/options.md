---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[protobuf/options.md]]"
tags: [Protobuf Global Extension Registry, Custom options, Extension numbers, descriptor.proto, protoc plugins]
aliases: ["Protocol Buffers 扩展注册表", "descriptor.proto 扩展登记表"]
---

# Protobuf Global Extension Registry - Summary

## 来源
- Original file: [[protobuf/options.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 Protocol Buffers（protobuf）项目的**全局扩展注册表**（[[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]），由 [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]] 维护，集中登记所有第三方项目为 [[concepts/descriptor-proto|descriptor.proto]] 注册的扩展编号。其核心目的是防止不同第三方项目在为 protobuf [[concepts/custom-options|Custom options]] 申请扩展编号时发生冲突。开发者可通过提交 Pull Request 或创建 Issue 的方式申请新的扩展编号，注册表从编号 1000 开始分配，当前已涵盖 1000 至 1190 以上号段，登记超过 90 个第三方项目，涵盖语言端口、gRPC 工具链、容器接口规范、监控系统、商业平台等广泛领域。该注册表是 protobuf 生态系统中跨项目协调的核心基础设施。

## 关键实体
- 语言端口：[[entities/protobuf-csharp-port|protobuf-csharp-port]]、[[entities/nanopb|nanopb]]、[[entities/scalapb|ScalaPB]]、[[entities/protobuf-net|protobuf-net]]、[[entities/mypy-protobuf|mypy-protobuf]]
- gRPC 与 RPC 框架：[[entities/grpc-gateway|grpc-gateway]]、[[entities/connect|Connect]]、[[entities/grpc-federation|gRPC Federation]]
- 协议与规范：[[entities/container-storage-interface|Container Storage Interface]]、[[entities/container-object-storage-interface|Container Object Storage Interface]]、[[entities/certificate-transparency|Certificate Transparency]]、[[entities/digital-twins-definition-language|Digital Twins Definition Language]]
- 代码生成与验证工具：[[entities/protoc-gen-validate|protoc-gen-validate]]、[[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]]、[[entities/buf|buf]]、[[entities/google-gnostic|Google Gnostic]]、[[entities/pigweed|Pigweed]]
- 平台与系统：[[entities/perfetto|Perfetto]]、[[entities/wire|Wire]]、[[entities/confluent-schema-registry|Confluent Schema Registry]]、[[entities/bazel|Bazel]]、[[entities/cloudstate|Cloudstate]]、[[entities/kratos|Kratos]]、[[entities/criu|CRIU]]、[[entities/ygot|ygot]]
- 其它项目：[[entities/fedone|FedOne]]、[[entities/goby|Goby]]、[[entities/foundationdb-sql-layer|FoundationDB SQL Layer]]、[[entities/adlink-edgesdk|ADLINK EdgeSDK]]、[[entities/protons|Protons]]

## 关键概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]：descriptor.proto 扩展编号的中央登记机制
- [[concepts/custom-options|Custom options]]：protobuf 提供的扩展机制，允许为 proto 元素添加自定义注解
- [[concepts/extension-numbers|Extension numbers]]：标识自定义扩展字段的数字标识符
- [[concepts/descriptor-proto|descriptor.proto]]：protobuf 自身的元数据描述文件
- [[concepts/protoc-plugins|protoc plugins]]：protoc 编译器生态中用于扩展代码生成能力的可执行程序

## 要点
- 注册表的核心目的是防止多个第三方项目在为 [[concepts/descriptor-proto|descriptor.proto]] 自定义选项申请 [[concepts/extension-numbers|扩展编号]]时发生冲突
- 扩展编号申请通过 GitHub 上的 Pull Request 或 Issue 流程管理，协议缓冲区主项目地址为 https://github.com/protocolbuffers/protobuf
- 注册表目前涵盖从 1000 到 1190 以上的扩展号段，登记了超过 90 个第三方项目和工具
- 重要生态项目包括 [[entities/grpc-gateway|grpc-gateway]]（1022、1042）、[[entities/buf|buf]]（1157-1166）、[[entities/connect|connect]]（1167-1176）、[[entities/wire|wire]]（多个号段）、[[entities/confluent-schema-registry|confluent-schema-registry]]（1088）等
- 容器和存储规范类项目包括 [[entities/container-storage-interface|CSI]]（1059-1069）和 [[entities/container-object-storage-interface|COSI]]（1115-1124）
- 语言端口类项目涵盖 C#（1000）、PHP/XS、Objective-C、Dart、Scala、.NET 等多语言实现
- 多家商业公司和组织通过注册扩展支持自家产品，包括 Juniper、FICO、Confluent、ADLINK 等