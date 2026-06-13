---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options]]"]
tags: [project]
aliases:
  - "YANG Go Tools"
  - "ygot"
  - "OpenConfig ygot"
---


# ygot

## 基本信息
- Type: project
- Source: [[sources/options]]

## 描述
ygot 是 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 生态系统中由 OpenConfig 项目维护的 YANG 到 Go 代码生成工具,代码托管在 GitHub 的 `openconfig/ygot` 仓库中。该工具以 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 扩展的方式进行注册,共占用了三个扩展编号:1040、1179 和 1180,体现了 ygot 对 [[concepts/descriptor.proto|descriptor.proto]] 扩展空间较为复杂的使用需求。

ygot 的核心功能是从 YANG 数据模型(网络设备配置的事实标准)生成对应的 Go 结构体、验证器以及 Proto/Protobuf 代码,使网络自动化系统能够以类型安全的方式处理配置与状态数据。凭借这一能力,ygot 在网络运营商和 SDN 生态系统中占据了重要地位,被多家大型网络运营商所采用。

作为 YANG 与 Go 语言生态之间的桥梁,ygot 与 [[entities/protocolbuffersprotobuf|protobuf]] 主项目以及其他 Protobuf 相关工具(如 [[entities/protoc-gen-validate|protoc-gen-validate]]、[[entities/protoc-gen-jsonschema|protoc-gen-jsonschema]])共同构成了 Protobuf 工具链在网络自动化领域的延伸。ygot 同时占用多个扩展编号这一事实,使其在 [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]] 中成为一个值得关注的案例。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[entities/pigweed|Pigweed]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]

## 来源提及
- ygot — [[sources/options]]
- Website: https://github.com/openconfig/ygot — [[sources/options]]
- Extensions: 1040, 1179, 1180 — [[sources/options]]