---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "Ubuntu Linux"
  - "Ubuntu 发行版"
---


# Ubuntu

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
Ubuntu 是一个基于 Debian 的 Linux 发行版，广泛用于开发和部署。在构建 [[entities/cmake|cmake]] 构建的 [[entities/@mcy|brpc]] 时，Ubuntu 是最主要的目标环境之一，提供了通过 apt-get 安装依赖的便捷方式。brpc 的构建脚本和 CMake 配置都针对 Ubuntu 进行了测试和优化。Ubuntu 用户可以通过简单的命令安装 [[entities/leveldb|leveldb]]、[[entities/cmake|CMake]] 等核心依赖，以及可选的 [[entities/gtest|gtest]]、[[entities/tcmalloc|tcmalloc]] 等。文档中特别提到了 Ubuntu/LinuxMint/WSL 作为兼容环境。Ubuntu 的包管理器 apt 简化了 C++ 开发环境的搭建。

## 相关实体
- [[entities/leveldb|leveldb]]
- [[entities/gtest|gtest]]
- [[entities/tcmalloc|tcmalloc]]
- [[entities/cmake|cmake]]
- [[entities/openssl|openssl]]
- [[entities/docker|docker]]

## 相关概念
- [[concepts/静态链接]]

## 来源提及
- "sudo apt-get install -y git g++ make libssl-dev libgflags-dev libprotobuf-dev libprotoc-dev protobuf-compiler libleveldb-dev" — [[sources/en_getting_started|en_getting_started]]
- "### Ubuntu/LinuxMint/WSL" — [[sources/en_getting_started|en_getting_started]]
- "### Prepare deps" — [[sources/en_getting_started|en_getting_started]]