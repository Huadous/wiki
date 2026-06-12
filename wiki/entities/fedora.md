---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Fedora Linux"
  - "Fedora 发行版"
---


# Fedora

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
Fedora 是一个由社区支持的 Linux 发行版，由 Fedora 项目开发和维护，作为 Red Hat Enterprise Linux (RHEL) 的上游源。在 brpc 的构建文档中，Fedora 与 CentOS 一起被列为受支持的操作系统环境。Fedora 用户可以通过 yum 或 dnf 包管理器安装 brpc 所需的依赖包，包括 gflags-devel、protobuf-devel、leveldb-devel 等。对于部分软件包，Fedora 用户需要先安装 EPEL (Extra Packages for Enterprise Linux) 仓库才能获取。brpc 的构建脚本 [[entities/config_brpc-sh|config_brpc.sh]] 和 [[entities/cmake|cmake]] 均支持在 Fedora 上构建项目。

## 相关实体
- [[entities/centos|CentOS]]
- [[entities/leveldb|leveldb]]
- [[entities/gtest|gtest]]
- [[entities/gperftools|gperftools]]

## 相关概念
- [[concepts/static-linking|静态链接]]

## 来源提及
- "## Fedora/CentOS" — [[sources/en_getting_started|en_getting_started]]
- "sudo yum install epel-release" — [[sources/en_getting_started|en_getting_started]]
- "sudo yum install gflags-devel protobuf-devel protobuf-compiler leveldb-devel" — [[sources/en_getting_started|en_getting_started]]