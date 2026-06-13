---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "macOS"
  - "Apple macOS"
  - "Mac OS X"
---

## Related Entities
- [[entities/homebrew|homebrew]] — macOS 上的包管理工具，用于安装 brpc 依赖
- [[entities/openssl|openssl]] — 通过 Homebrew 安装的依赖库之一
- [[entities/gflags|gflags]] — 通过 Homebrew 安装的命令行标志库
- [[entities/leveldb|leveldb]] — 通过 Homebrew 安装的键值存储库
- [[entities/config_brpc-sh|config_brpc.sh]] — macOS 上可用的构建脚本（需注意 OpenSSL 路径兼容性）
- [[entities/cmake|cmake]] — macOS 上可用的构建工具
- [[entities/centos|centos]] — 与 macOS 对比的 Linux 发行版
- [[entities/ubuntu|ubuntu]] — 与 macOS 对比的 Linux 发行版
- [[entities/gtest|gtest]] — 可选安装的测试框架
- [[entities/libunwind|libunwind]] — 相关的栈回溯库
- [[entities/clang|clang]] — macOS 默认使用的编译器

## Related Concepts
- [[concepts/static-linking|静态链接]] — macOS 下的链接方式考量

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "## MacOS"
> - "Note: With same environment, the performance of the MacOS version is worse than the Linux version. If your service is performance-critical, do not use MacOS as your production environment."
> - "brew install openssl git gnu-getopt coreutils gflags leveldb"

> **Source: [[sources/getting_started|getting_started]]**
> - "注意：在相同硬件条件下，MacOS版brpc的性能可能明显差于Linux版。如果你的服务是性能敏感的，请不要使用MacOS作为你的生产环境。"
> - "master HEAD已支持M1系列芯片，M2未测试过。"