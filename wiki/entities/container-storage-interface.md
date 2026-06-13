---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "CSI"
  - "容器存储接口"
  - "Container Storage Interface (CSI)"
---


# Container Storage Interface

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Container Storage Interface(CSI)是Kubernetes等容器编排系统定义的标准存储接口规范,注册了Protocol Buffers扩展编号1059-1069,规范托管在GitHub的container-storage-interface/spec仓库中。CSI旨在将存储插件从容器编排系统核心中解耦,使第三方存储供应商能够以标准化的方式提供块存储、文件存储与对象存储卷的动态供给、挂载与快照功能。该规范使用Protocol Buffers作为其RPC接口与卷拓扑消息的定义语言,并通过[[entities/protocolbuffersprotobuf|Protocol Buffers]] 的 descriptor.proto 扩展机制为CSI特有的容量、访问模式与拓扑约束等自定义选项保留较大范围的扩展编号(1059-1069)。CSI现已成为Kubernetes持久卷(PV)供给的事实标准,其规范与实现也持续在 [[sources/options|Protobuf Global Extension Registry]] 中维护。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- Protobuf Global Extension Registry

## 相关概念
- Extension numbers
- Custom options
- descriptor.proto

## 来源提及
- "Container Storage Interface — [[sources/options|options]]"
- "Website: https://github.com/container-storage-interface/spec — [[sources/options|options]]"
- "Extensions: 1059-1069 — [[sources/options|options]]"