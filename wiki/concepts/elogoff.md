---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "brpc::ELOGOFF"
  - "服务关闭错误码"
  - "优雅关闭信号"
---

## Related Concepts
- [[concepts/优雅重启|优雅重启]]
- [[concepts/服务停止|服务停止]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/服务器生命周期管理|服务器生命周期管理]]
- [[concepts/限流|限流]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/server|Server]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/bns|bns]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Regardless of the value of closewait_ms, server waits for all requests being processed before exiting and returns ELOGOFF errors to new requests immediately to prevent them from entering the service." — [[sources/en_server|en_server]]
> - "When a client sees ELOGOFF, it skips the corresponding server and retry the request on another server." — [[sources/en_server|en_server]]
> - "When a client sees ELOGOFF, it skips the corresponding server and retry the request on another server. As a result, restarting a cluster with brpc clients/servers gradually should not lose traffic by default." — [[sources/en_server|en_server]]