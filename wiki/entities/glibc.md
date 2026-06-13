---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/bthread.md]]"
tags:
  - "product"
aliases:
  - "GNU C Library"
  - "GNU glibc"
---

## Related Entities
- [[entities/gcc|GCC]] — 与glibc共同构成brpc编译运行的基础工具链
- [[entities/brpc|brpc]] — 依赖glibc提供底层系统调用与C运行时支持
- [[entities/cmake|CMake]] — brpc构建系统中涉及glibc版本检测的构建工具
- [[entities/bthread|bthread]] — bthread在设计时需考虑glibc阻塞函数带来的兼容性与死锁问题

## Related Concepts
- [[concepts/pthread|pthread]] — bthread非目标讨论中涉及的POSIX线程模型，与bthread的混用可能导致死锁
- [[concepts/fiber|fiber]] — 与bthread同属协程/纤程类概念，bthread文档中作为对比概念出现
- [[concepts/bthread|bthread]] — 与glibc阻塞函数兼容性问题直接相关的协程/线程库概念

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "glibc: 2.12-2.25 no known issues."

> **Source: [[sources/bthread|bthread]]**
> - "覆盖各类可能阻塞的glibc函数和系统调用，让原本阻塞系统线程的函数改为阻塞bthread。"
> - "bthread阻塞可能切换系统线程，依赖系统TLS的函数的行为未定义。"
> - "和阻塞pthread的函数混用时可能死锁。"
> - "这类hook函数本身的效率一般更差，因为往往还需要额外的系统调用，如epoll。"