---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "mypy-protobuf"
  - "nipunn1313/mypy-protobuf"
  - "mypy protobuf stubs"
---


# mypy-protobuf

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
mypy-protobuf 是由 nipunn1313 开发的 protoc 插件,代码托管在 GitHub 的 [[entities/nipunn1313mypy-protobuf|nipunn1313/mypy-protobuf]] 仓库中。该插件为 protoc 生成的 Python 代码添加 mypy 类型存根(stub)文件,使开发者在使用 mypy 进行静态类型检查时能够获得对 proto 消息字段类型的完整检查能力。mypy-protobuf 解决了官方 protoc 生成的 Python 代码缺乏精确类型提示的问题,是 Python 生态中采用 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 的项目进行严格类型检查的关键工具。该项目支持 proto2 和 proto3 两种语法,并支持 WKT(Well-Known Types)。该插件在 [[sources/options|Protocol Buffers 扩展注册表]]中注册了扩展编号 1151-1154,用于在 proto 文件中嵌入与 mypy 类型生成相关的自定义选项。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor-proto|descriptor.proto]]
- [[concepts/protoc-plugins|protoc plugins]]

## 来源提及
- mypy-protobuf — [[sources/options|options]]
- Website: https://github.com/nipunn1313/mypy-protobuf — [[sources/options|options]]
- Extension: 1151-1154 — [[sources/options|options]]