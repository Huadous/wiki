---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "method"
aliases:
  - "usercode_in_pthread"
  - "Pthread模式"
  - "pthread mode"
  - "usercode_in_pthread"
  - "Pthread模式"
  - "pthread Mode"
  - "usercode_in_pthread"
  - "Pthread模式"
  - "pthread mode"
  - "usercode_in_pthread"
  - "Pthread模式"
---

## Related Concepts
- [[concepts/bthread|bthread]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/同步服务|同步服务]]
- [[concepts/Server-thread-local数据|Server-thread-local数据]]
- [[concepts/Session-local数据|Session-local数据]]
- [[concepts/最大并发控制|最大并发控制]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]

## Mentions in Source

> **Source: [[sources/server|brpc Server端使用文档]]**
> - "用户代码（客户端的done，服务器端的CallMethod）默认在栈为1MB的bthread中运行。"
> - "对于这些情况，brpc提供了pthread模式，开启**-usercode_in_pthread**后，用户代码均会在pthread中运行"