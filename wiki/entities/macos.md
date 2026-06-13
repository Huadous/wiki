---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "macOS"
  - "Apple macOS"
  - "Mac OS X"
---


# MacOS

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
macOS 是 Apple 公司开发的桌面操作系统，在 brpc 文档中被列为受支持的构建和运行环境。brpc 文档明确警告，在相同环境下 macOS 版本的性能低于 Linux 版本，不建议将其用于性能关键的生产环境。对于希望在 macOS 上构建 brpc 的用户，文档提供了通过 [[entities/openssl|Homebrew]] 安装依赖的详细步骤，包括 [[entities/openssl|openssl]]、[[entities/gflags|gflags]]、[[entities/leveldb|leveldb]] 等库。macOS 支持 Apple Silicon 芯片（M1 系列），用户可以使用 [[entities/config_brpc-sh|config_brpc.sh]] 或 [[entities/cmake|CMake]] 进行构建，但需注意 openssl 路径问题。macOS 与 [[entities/centos|centos]]、[[entities/ubuntu|ubuntu]] 等 Linux 发行版在 brpc 支持方面存在差异，主要体现在性能优化和构建工具链上。

## 相关实体
- [[entities/openssl|openssl]] — 通过 Homebrew 安装的依赖库之一
- [[entities/gflags|gflags]] — 通过 Homebrew 安装的命令行标志库
- [[entities/leveldb|leveldb]] — 通过 Homebrew 安装的键值存储库
- [[entities/config_brpc-sh|config_brpc.sh]] — macOS 上可用的构建脚本
- [[entities/cmake|cmake]] — macOS 上可用的构建工具
- [[entities/centos|centos]] — 与 macOS 对比的 Linux 发行版
- [[entities/ubuntu|ubuntu]] — 与 macOS 对比的 Linux 发行版
- [[entities/gtest|gtest]] — 可选安装的测试框架
- [[entities/libunwind|libunwind]] — 相关的栈回溯库
- [[entities/clang|clang]] — macOS 默认使用的编译器

## 相关概念
- [[concepts/static-linking|静态链接]] — macOS 下的链接方式考量

## 来源提及
- "## MacOS" — [[sources/en_getting_started|en_getting_started]]
- "Note: With same environment, the performance of the MacOS version is worse than the Linux version. If your service is performance-critical, do not use MacOS as your production environment." — [[sources/en_getting_started|en_getting_started]]
- "brew install openssl git gnu-getopt coreutils gflags leveldb" — [[sources/en_getting_started|en_getting_started]]