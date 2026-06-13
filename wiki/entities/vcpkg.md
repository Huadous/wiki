---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Vcpkg"
  - "微软 vcpkg"
---


# vcpkg

## 基本信息
- 类型: product
- 来源: [[sources/en_getting_started|en_getting_started]]

## 描述

vcpkg 是微软推出的跨平台 C/C++ 包管理器，支持 Windows、Linux 和 macOS 三大操作系统。在 [[entities/brpc|brpc]] 文档中，vcpkg 被列为一种可选的构建方式，用户可以通过 vcpkg 安装 brpc 及其所有依赖。使用 vcpkg 构建 brpc 的基本流程包括：克隆 vcpkg 仓库、运行 bootstrap 脚本、然后执行 `./vcpkg install brpc` 命令。vcpkg 尤其简化了 Windows 环境下的 C/C++ 依赖管理，使开发者无需手动配置第三方库的编译和链接参数。

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/gflags|gflags]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/openssl|openssl]]

## 相关概念

- [[concepts/静态链接|静态链接]]

## 来源提及

- "### Compile brpc with vcpkg" — [[sources/en_getting_started|en_getting_started]]
- "[vcpkg](https://github.com/microsoft/vcpkg) is a package manager that supports all platforms" — [[sources/en_getting_started|en_getting_started]]
- "$ git clone https://github.com/microsoft/vcpkg.git" — [[sources/en_getting_started|en_getting_started]]
- "$ ./vcpkg install brpc" — [[sources/en_getting_started|en_getting_started]]