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
  - "GNU Compiler Collection"
  - "GNU编译器套件"
---

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/Clang|Clang]]
- [[entities/protobuf|protobuf]]
- [[entities/cmake|cmake]]
- [[entities/tcmalloc|tcmalloc]]

## Related Concepts

- [[concepts/静态链接|静态链接]]
- [[concepts/c++11|c++11]]

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "Prefer GCC 8.2+"
> - "GCC: 4.8-11.2"
> - "Adding -D__const__=__unused__ to cxxflags in your makefiles is a must to avoid errno issue in gcc4+."
> - "The over-aligned issues in GCC7 is suppressed temporarily now."

> **Source: [[sources/getting_started|getting_started]]**
> - "推荐 8.2 及以上版本。"
> - "默认启用 c++11，以去除对 boost 的依赖（比如 atomic）。"
> - "用gcc4.8.2编译然后链接更早版本GCC编译的tcmalloc，可能会让程序中main()函数之前挂掉或者死锁"