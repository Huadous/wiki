---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "other"
aliases:
  - "DoNothing()"
  - "brpc::DoNothing()"
  - "brpc::DoNothing"
  - "DoNothing()"
  - "brpc::DoNothing()"
---

## Related Entities
- [[entities/brpc-controller|brpc::Controller]]
- [[entities/brpc-channel|brpc::Channel]]

## Related Concepts
- [[concepts/semi-synchronous-call|Semi-synchronous call]]
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/brpc-call-id|brpc::CallId]]

## Mentions in Source
- brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc. — [[sources/en_client]]
- Note that in above example, we access `controller.call_id()` after completion of RPC, which is safe right here, because DoNothing does not delete controller as in `on_rpc_done` in previous example. — [[sources/en_client]]
- stub2.method2(&cntl2, &request2, &response2, brpc::DoNothing()); — [[sources/en_client]]

> **Source: [[sources/client]]**
> - brpc::DoNothing()可获得一个什么都不干的done，专门用于半同步访问。它的生命周期由框架管理，用户不用关心。
> - stub1.method1(&cntl1, &request1, &response1, brpc::DoNothing());