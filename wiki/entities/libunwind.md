---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "libunwind"
  - "LLVM libunwind"
  - "栈回溯库"
---

## Related Entities

- [[entities/config_brpc-sh|config_brpc-sh]] — brpc 的配置脚本，通过 `--with-bthread-tracer` 参数启用 libunwind
- [[entities/cmake|cmake]] — brpc 可用的构建工具，通过 `-DWITH_BTHREAD_TRACER=ON` 启用 libunwind
- [[entities/brpc|brpc]] — 集成 libunwind 以支持 bthread 栈回溯的 RPC 框架

## Related Concepts

- [[concepts/stack-unwinding|stack unwinding]] — libunwind 的核心功能，用于获取程序调用栈信息
- [[concepts/bazel-build-system|Bazel]] — brpc 支持的构建系统之一，可通过 `--define with_bthread_tracer=true` 启用 libunwind

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "libunwind: 1.3-1.8.1"
> - "brpc does **not** link libunwind by default. Users link libunwind on-demand by adding --with-bthread-tracer to config_brpc.sh or adding -DWITH_BTHREAD_TRACER=ON to cmake"

> **Source: [[sources/getting_started|getting_started]]**
> - "libunwind: 1.3-1.8.1"
> - "bRPC默认**不**链接 [libunwind](https://github.com/libunwind/libunwind)。用户需要追踪bthread功能则链接libunwind，可以给config_brpc.sh增加`--with-bthread-tracer`选项或者给cmake增加`-DWITH_BTHREAD_TRACER=ON`选项，如果是用 bazel 构建，请添加 `--define with_bthread_tracer=true` 选项。"
> - "建议使用最新版本的libunwind。"