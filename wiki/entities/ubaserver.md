---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/bthread_or_not]]"
  - "[[brpc/bthread.md]]"
tags:
  - "product"
aliases:
  - "ubaserver"
  - "uba server"
  - "ub a server"
---

## Related Entities
- [[entities/brpc|brpc]]

## Related Concepts
- [[concepts/异步接口|异步接口]]
- [[concepts/回调|回调]]
- [[concepts/半同步|半同步]]
- [[concepts/event-loop|event loop]]
- [[concepts/协程|coroutine]]

## Mentions in Source
> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "那是不是服务能搞成类似的形式呢？多个线程，每个都是独立的eventloop。可以，ubaserver就是（注意带a)，但实际效果糟糕"
> - "因为阻塞改回调可不简单，当阻塞发生在循环，条件分支，深层子函数中时，改造特别困难"
> - "结果是代码中会出现不可避免的阻塞，导致那个线程中其他回调都被延迟，流量超时，server性能不符合预期。"

> **Source: [[sources/bthread|bthread]]**
> - "比如ubaserver（注意那个a，不是ubserver）是百度对异步框架的尝试，由多个并行的eventloop组成，真实表现糟糕：回调里打日志慢一些，访问redis卡顿，计算重一点，等待中的其他请求就会大量超时。所以这个框架从未流行起来。"