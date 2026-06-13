---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Windows Subsystem for Linux"
  - "WSL"
---


# WSL

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
WSL（Windows Subsystem for Linux）是 Microsoft 开发的 Linux 兼容层，允许在 Windows 操作系统上直接运行 Linux 二进制可执行文件，无需传统虚拟机或双系统配置。在 brpc 的构建文档中，WSL 与 [[entities/ubuntu|Ubuntu]] 和 LinuxMint 被列为同一支持组，表明 brpc 可以原生地在 WSL 环境中完成编译和构建。WSL 用户可以使用与 Ubuntu 完全相同的 `apt-get` 包管理器命令来安装所有必需的依赖项，如 Git、GCC、Make 等构建工具。这一特性为 Windows 开发者提供了无缝的 Linux 开发体验，无需切换操作系统即可参与 Linux 原生软件的开发。WSL 本身不提供图形界面，专注于命令行和服务器端开发场景，是跨平台开发的重要桥接工具。

## 相关实体
- [[entities/ubuntu|Ubuntu]]
- [[entities/gflags|gflags]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/cmake|cmake]]
- [[entities/gcc|gcc]]

## 相关概念
- [[concepts/static-linking|静态链接]]

## 来源提及
- "### Ubuntu/LinuxMint/WSL" — [[sources/en_getting_started|en_getting_started]]
- "sudo apt-get install -y git g++ make libssl-dev libgflags-dev libprotobuf-dev libprotoc-dev protobuf-compiler libleveldb-dev" — [[sources/en_getting_started|en_getting_started]]