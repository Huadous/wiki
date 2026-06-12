---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
  - "[[sources/en_getting_started]]"
tags:
  - "product"
aliases:
  - "Thread-Caching Malloc"
  - "Google tcmalloc"
---

## Related Entities
- [[entities/tcmalloc|tcmalloc]] — Google开发的线程缓存内存分配器，本文档描述的核心主题
- [[entities/brpc|brpc]] — brpc框架支持按需链接tcmalloc，tcmalloc是brpc分析器的基础
- [[entities/glibc|glibc]] — glibc中的ptmalloc是tcmalloc替代的目标内存分配器
- [[entities/gcc|gcc]] — brpc推荐使用与代码相同GCC版本编译tcmalloc
- [[entities/threads|threads]] — tcmalloc性能在多线程场景下的表现是核心关注点
- [[entities/gflags|gflags]] — Google开发的命令行参数处理库，与tcmalloc同属Google基础设施组件

## Related Concepts
- [[concepts/memory-allocator|memory allocator]] — tcmalloc作为高性能多线程内存分配器的分类定位
- [[concepts/thread-local-variables|thread-local variables]] — tcmalloc性能与线程局部变量机制直接相关

## Mentions in Source
> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "brpc does **not** link tcmalloc by default. Users link tcmalloc on-demand."
> - "Comparing to ptmalloc embedded in glibc, tcmalloc often improves performance."
> - "When you program behave unexpectedly, remove tcmalloc or try another version."
> - "If you want to use cpu profiler or heap profiler, do link libtcmalloc_and_profiler.a."