---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/bthread_or_not]]"
  - "[[brpc/bthread.md]]"
tags:
  - "method"
aliases:
  - "ExecutionQueue"
  - "bthread ExecutionQueue"
  - "执行队列"
---

## Related Concepts
- [[concepts/bthread|bthread]]
- [[concepts/组合访问|组合访问]]
- [[concepts/m-n-threading|M:N threading]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "另外当你有类似线程池的需求时，像执行一类job的线程池时，也可以用bthread代替。"
> - "如果对job的执行顺序有要求，你可以使用基于bthread的ExecutionQueue。"

> **Source: [[sources/bthread|bthread]]**
> - "我们需要的往往是buffered channel，扮演的是队列和有序执行的作用，bthread提供了ExecutionQueue，可以完成这个目的。"