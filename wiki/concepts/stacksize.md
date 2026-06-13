---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "bthread栈大小"
  - "栈空间"
  - "bthread stack size"
  - "bthread栈大小"
  - "栈空间"
  - "stack_size"
  - "bthread栈大小"
  - "栈空间"
  - "bthread stack size"
  - "bthread栈大小"
  - "栈空间"
---

## Description

stacksize 是 brpc 中 bthread 的栈内存大小配置参数。与 pthread 的 10MB 默认栈空间相比，bthread 的默认栈大小仅为 1MB，这使得 bthread 能够支持大量并发任务，但同时也增加了栈溢出的风险。当程序在 pthread 模式下运行正常，切换到 bthread 模式后发生崩溃时，栈空间不足是常见原因之一。这种栈溢出通常发生在深度递归或大量局部变量的场景中。brpc 提供了 `--stack_size_normal` gflag 来调整 bthread 栈大小（例如设置为 10MB），以及 `--tc_stack_normal` 参数控制每个工作 pthread 缓存的栈个数（默认值为 8），以减少从全局池中重复分配的频率。这一配置对于从 pthread 迁移到 bthread 的代码尤为重要，可以帮助快速排查因栈空间不足导致的程序崩溃甚至 coredump。

## Related Concepts

- [[concepts/bthread|bthread]]
- [[concepts/pthread模式|pthread模式]]

## Related Entities

- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_server]]**
> - "brpc server runs code in bthreads with stacksize=1MB by default, while stacksize of pthreads is 10MB."
> - "Set following gflags to enlarge the stacksize. --stack_size_normal=10000000  # sets stacksize to roughly 10MB --tc_stack_normal=1"
> - "brpc server runs code in bthreads with stacksize=1MB by default, while stacksize of pthreads is 10MB. It's possible that programs running normally on pthreads may meet stack overflow on bthreads."
> - "Set following gflags to enlarge the stacksize. --stack_size_normal=10000000  # sets stacksize to roughly 10MB --tc_stack_normal=1           # sets number of stacks cached by each worker pthread to prevent reusing from global pool each time, default value is 8"