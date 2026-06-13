---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bthread_or_not.md]]"
tags:
  - "method"
aliases:
  - "半同步调用"
  - "Semi-synchronous call"
  - "半同步"
  - "半同步调用"
  - "Semi-synchronous call"
---

## Related Concepts
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/synchronous-call|Synchronous call]]
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/异步访问|异步访问]]
- [[concepts/同步访问|同步访问]]
- [[concepts/bthread|bthread]]
- [[concepts/parallel-channel|ParallelChannel]]
- [[concepts/异步接口|异步接口]]
- [[concepts/同步接口|同步接口]]

## Related Entities
- [[entities/channel|Channel]]
- [[entities/controller|Controller]]
- [[entities/brpcdonothing|brpc::DoNothing]]
- [[entities/brpcchannel|brpc::Channel]]
- [[entities/brpccontroller|brpc::Controller]]
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "Join can be used for implementing "Semi-synchronous" call: blocks until multiple asynchronous calls to complete."
> - "Since the callsite blocks until completion of all RPC, controller/response can be put on stack safely."
> - "brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc."

> **Source: [[sources/client|client]]**
> - "Join可用来实现"半同步"访问：即等待多个异步访问完成。"
> - "brpc::DoNothing()可获得一个什么都不干的done，专门用于半同步访问。"
> - "brpc::Join(cntl1.call_id())"

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "有了bthread这个工具，用户甚至可以自己实现异步。以"半同步"为例，在brpc中用户有多种选择："
> - "发起多个异步RPC后挨个Join，这个函数会阻塞直到RPC结束。"
> - "哪种效率更高呢？显然是前者。后者不仅要付出创建bthread的代价，在RPC过程中bthread还被阻塞着，不能用于其他用途。"