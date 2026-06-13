---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "Thread-Caching Malloc"
  - "Google tcmalloc"
---

## Related Entities
- [[entities/brpc|brpc]] — brpc框架按需链接tcmalloc，且tcmalloc是其cpu/heap profiler的基础
- [[entities/glibc|glibc]] — glibc内置的ptmalloc是与tcmalloc对比的基准分配器
- [[entities/gcc|gcc]] — brpc推荐使用与代码相同GCC版本编译tcmalloc
- [[entities/gflags|gflags]] — Google开发的命令行参数处理库，与tcmalloc同属Google基础设施组件
- [[entities/jemalloc|jemalloc]] — 与tcmalloc并列为一般应用可使用的成熟内存分配方案
- [[entities/threads|threads]] — tcmalloc在多线程场景下的性能表现是核心关注点

## Related Concepts
- [[concepts/memory-allocator|memory allocator]] — tcmalloc作为高性能多线程内存分配器的分类定位
- [[concepts/thread-local-variables|thread-local variables]] — tcmalloc性能与线程局部变量机制直接相关
- [[concepts/等长对象分配|等长对象分配]] — brpc场景下tcmalloc未能满足的极致优化需求方向
- [[concepts/内存池|内存池]] — brpc针对tcmalloc不足而采用的自研内存管理方案
- [[concepts/valgrind|valgrind]] — 内存调试与分析工具，与tcmalloc在性能剖析领域相关
- [[concepts/glog|glog]] — Google开发的日志库，与tcmalloc同属Google基础设施组件

## Mentions in Source
> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "brpc does **not** link tcmalloc by default. Users link tcmalloc on-demand."
> - "Comparing to ptmalloc embedded in glibc, tcmalloc often improves performance."
> - "When you program behave unexpectedly, remove tcmalloc or try another version."
> - "If you want to use cpu profiler or heap profiler, do link libtcmalloc_and_profiler.a."
> - "tcmalloc: 1.7-2.5"
> - "和glibc内置的ptmalloc相比，tcmalloc通常能提升性能。然而不同版本的tcmalloc可能表现迥异。" (Comparing to ptmalloc embedded in glibc, tcmalloc often improves performance. However, different versions of tcmalloc may behave very differently.)

> **Source: [[sources/memory_management|memory_management]]**
> - "一般的应用可以使用tcmalloc、jemalloc等成熟的内存分配方案，但这对于较为底层，关注性能长尾的应用是不够的。" (General applications can use mature memory allocators like tcmalloc and jemalloc, but this is insufficient for lower-level applications that care about long-tail performance.)