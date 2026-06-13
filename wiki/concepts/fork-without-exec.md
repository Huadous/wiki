---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "phenomenon"
aliases:
  - "fork后不exec"
  - "进程分叉"
  - "fork without exec"
---

## Related Concepts
- [[concepts/bthread|bthread]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/多线程fork问题|多线程fork问题]]
- [[concepts/pthread模式|pthread模式]]
- [[concepts/按需线程创建|按需线程创建]]

## Related Entities
- [[entities/bvar|bvar]]
- [[entities/brpc|brpc]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/bthread|bthread]]

## Mentions in Source
> **Source: [[sources/server|server]]**
> - "最新版本的brpc会在fork后重建这个线程(如有必要)，从而使bvar在fork后能正常工作，再次fork也可以。"
> - "brpc的策略是按需创建这类线程，同时fork without exec必须发生在所有可能创建这些线程的代码前。"