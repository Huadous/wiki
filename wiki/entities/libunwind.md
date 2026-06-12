---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "libunwind"
  - "LLVM libunwind"
  - "栈回溯库"
---


# libunwind

## 基本信息
- **Type:** product
- **Source:** [[sources/en_getting_started|en_getting_started]]

## 描述

libunwind 是一个用于获取程序调用栈（stack unwinding）的 C 语言库，广泛应用于性能分析、异常处理和调试工具中。在 brpc 框架中，libunwind 并非默认链接的依赖项，但用户可以通过构建选项启用它以支持 bthread 的栈回溯功能。brpc 官方推荐使用最新版本的 libunwind，并已测试兼容 libunwind 1.3 至 1.8.1 版本。对于需要深度堆栈调试或协程（bthread）上下文追踪的场景，libunwind 是一个有用的补充。用户可通过 `config_brpc.sh` 脚本添加 `--with-bthread-tracer` 参数或在 CMake 中设置 `-DWITH_BTHREAD_TRACER=ON` 来按需启用。

## 相关实体

- [[entities/config_brpc-sh|config_brpc-sh]] — brpc 的配置脚本，通过 `--with-bthread-tracer` 参数启用 libunwind
- [[entities/cmake|cmake]] — brpc 可用的构建工具，通过 `-DWITH_BTHREAD_TRACER=ON` 启用 libunwind
- [[entities/brpc|brpc]] — 集成 libunwind 以支持 bthread 栈回溯的 RPC 框架

## 相关概念

（无）

## 来源提及

- "libunwind: 1.3-1.8.1" — [[sources/en_getting_started|en_getting_started]]
- "brpc does **not** link libunwind by default. Users link libunwind on-demand by adding --with-bthread-tracer to config_brpc.sh or adding -DWITH_BTHREAD_TRACER=ON to cmake" — [[sources/en_getting_started|en_getting_started]]