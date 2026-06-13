---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options]]"]
tags: [project]
aliases:
  - "Checkpoint Restore In Userspace"
  - "CRIU 项目"
  - "criu.org"
---


# CRIU

## 基本信息
- Type: project
- Source: [[sources/options]]

## 描述
CRIU(Checkpoint Restore In Userspace)是 Linux 内核用户空间的检查点/恢复工具,项目网站为 [criu.org](http://criu.org/Main_Page)。该工具能够在不中断服务的情况下冻结正在运行的进程,并将其状态序列化到磁盘以便稍后恢复,是容器迁移、快照与高可用等场景的关键基础设施。CRIU 已向 [[entities/protocolbuffersprotobuf|Protocol Buffers]] 全局扩展注册表注册了扩展编号 **1018**,通过 `descriptor.proto` 扩展为其特有的自定义选项保留编号。CRIU 使用 Protocol Buffers 来定义其进程镜像格式与控制协议。该项目在 [[entities/zookeeper|Kubernetes]]、Docker 以及 OpenVZ 等容器生态系统中具有重要影响,是 [[concepts/extension-numbers|扩展编号]] 机制在 Linux 系统级工具中的典型应用案例。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[entities/zookeeper|Kubernetes]] (容器编排生态相关)

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]

## 来源提及
- "CRIU (Checkpoint Restore In Userspace)" — [[sources/options]]
- "Website: http://criu.org/Main_Page" — [[sources/options]]
- "Extensions: 1018" — [[sources/options]]