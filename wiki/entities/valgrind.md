---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Valgrind"
  - "Valgrind 内存调试工具"
---


# valgrind

## 基本信息
- **类型**: product
- **来源**: [[sources/en_getting_started|en_getting_started]]

## 描述

Valgrind 是一个用于内存调试、内存泄漏检测和性能分析的动态分析工具。它被广泛应用于 C/C++ 开发中，帮助开发者发现内存管理错误的根源。[[entities/brpc|brpc]] 在运行时能够自动检测 Valgrind 环境，并注册 bthread 的栈信息以便于调试。brpc 官方支持 Valgrind 3.8 及以上版本，更早版本不受支持。作为开发过程中常用的调试工具，Valgrind 与 brpc 的集成有助于排查内存相关问题。

## 相关实体

- [[entities/brpc|brpc]]

## 相关概念

_无_

## 来源提及

- "valgrind: 3.8+ brpc detects valgrind automatically (and registers stacks of bthread)." — [[sources/en_getting_started|en_getting_started]]
- "Older valgrind(say 3.2) is not supported." — [[sources/en_getting_started|en_getting_started]]