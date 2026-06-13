---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "brpc::Join()"
  - "Join()"
  - "JoinResponse()"
---

## Related Concepts
- [[concepts/Controller]]
- [[concepts/Asynchronous call]]
- [[concepts/Synchronous call]]
- [[concepts/Cancel RPC]]
- [[concepts/half-synchronous-access|半同步访问]]

## Related Entities
- [[entities/brpc-controller|brpc::Controller]]

## Mentions in Source
> **Source: [[sources/en_client]]**
> - "Join() blocks until completion of RPC and end of done->Run(), properties of Join: If the RPC is complete, Join() returns immediately. Multiple threads can Join() one id, all of them will be woken up."
> - "Join() was called JoinResponse() before, if you meet deprecated issues during compilation, rename to Join()."

> **Source: [[sources/client|client]]**
> - "Join()的行为是等到RPC结束且done->Run()运行后，一些Join的性质如下："
> - "Join()在之前的版本叫做JoinResponse()，如果你在编译时被提示deprecated之类的，修改为Join()。"
> - "No directly relevant information"