---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Community Enterprise Operating System"
  - "CentOS Linux"
---


# CentOS

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
CentOS 是一个基于 Red Hat Enterprise Linux (RHEL) 的免费企业级 Linux 发行版，由开源社区维护。在 brpc 项目的构建指南中，CentOS 被列为支持的开发环境之一，与 Fedora 并列提供依赖安装说明。brpc 文档特别指出 CentOS 通常需要安装 EPEL (Extra Packages for Enterprise Linux) 仓库，因为许多必需的软件包在默认仓库中不可用。CentOS 用户可以通过 `yum` 包管理器安装 brpc 构建所需的依赖，如 `gflags-devel` 和 `protobuf-devel`。brpc 的构建脚本 `config_brpc.sh` 和 CMake 构建系统均支持 CentOS 平台。

## 相关实体
- [[entities/cmake|cmake]]
- [[entities/config_brpc-sh|config_brpc.sh]]
- [[entities/gflags|gflags]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/gtest|gtest]]
- [[entities/gperftools|gperftools]]

## 相关概念
- [[concepts/静态链接|静态链接]]

## 来源提及
- "## Fedora/CentOS" — [[sources/en_getting_started|en_getting_started]]
- "CentOS needs to install EPEL generally otherwise many packages are not available by default." — [[sources/en_getting_started|en_getting_started]]
- "sudo yum install epel-release" — [[sources/en_getting_started|en_getting_started]]