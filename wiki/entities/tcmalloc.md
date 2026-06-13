---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/memory_management.md]]"
tags:
  - "product"
aliases:
  - "Thread-Caching Malloc"
  - "Google tcmalloc"
---

## Related Entities
- [[entities/tcmalloc|tcmalloc]] — Google开发的线程缓存内存分配器，本实体描述的核心主题
- [[entities/jemalloc|jemalloc]] — 与tcmalloc并列为一般应用可使用的成熟内存分配方案
- [[entities/brpc|brpc]] — brpc框架支持按需链接tcmalloc，tcmalloc是brpc分析器的基础；同时也是推动超越tcmalloc、自研内存池的对象
- [[entities/glibc|glibc]] — glibc中的ptmalloc是tcmalloc替代的目标内存分配器
- [[entities/gcc|gcc]] — brpc推荐使用与代码相同GCC版本编译tcmalloc
- [[entities/threads|threads]] — tcmalloc性能在多线程场景下的表现是核心关注点
- [[entities/gflags|gflags]] — Google开发的命令行参数处理库，与tcmalloc同属Google基础设施组件

## Related Concepts
- [[concepts/memory-allocator|memory allocator]] — tcmalloc作为高性能多线程内存分配器的分类定位
- [[concepts/thread-local-variables|thread-local variables]] — tcmalloc性能与线程局部变量机制直接相关
- [[concepts/等长对象分配|等长对象分配]] — brpc场景下tcmalloc未能满足的极致优化需求方向
- [[concepts/内存池|内存池]] — brpc针对tcmalloc不足而采用的自研内存管理方案

## Mentions in Source
> **Source: en_getting_started**
> - "brpc does **not** link tcmalloc by default. Users link tcmalloc on-demand."
> - "Comparing to ptmalloc embedded in glibc, tcmalloc often improves performance."
> - "When you program behave unexpectedly, remove tcmalloc or try another version."
> - "If you want to use cpu profiler or heap profiler, do link libtcmalloc_and_profiler.a."

> **Source: memory_management**
> - "一般的应用可以使用tcmalloc、jemalloc等成熟的内存分配方案，但这对于较为底层，关注性能长尾的应用是不够的。"