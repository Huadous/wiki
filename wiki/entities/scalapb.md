---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "scalapb"
  - "Scala Protocol Buffers"
---


# ScalaPB

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
ScalaPB 是 Protocol Buffers 的 Scala 语言编译器插件，能够从 `.proto` 文件生成 Scala 案例类和接口。它在 [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 中分配到的扩展编号为 1020，官方网站为 https://scalapb.github.io/。该项目是 Scala 生态系统中处理 protobuf 的主流工具，提供了与 Scala 类型系统的深度集成。除了核心 ScalaPB 之外，还有一个名为 ScalaPB Validate 的扩展（编号 1089，网站为 https://scalapb.github.io/docs/validation）用于数据验证，与 [[entities/protoc-gen-validate|protoc-gen-validate]] 在功能上类似，均属于 [[concepts/custom-options|Custom options]] 生态下的验证工具。

## 相关实体
- [[entities/protoc-gen-validate|protoc-gen-validate]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- ScalaPB — [[sources/options|options]]
- Website: https://scalapb.github.io/ — [[sources/options|options]]
- Extensions: 1020 — [[sources/options|options]]
- ScalaPB Validate — [[sources/options|options]]
- Website: https://scalapb.github.io/docs/validation — [[sources/options|options]]
- Extension: 1089 — [[sources/options|options]]