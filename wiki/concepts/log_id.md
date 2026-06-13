---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "term"
aliases:
  - "log_id"
  - "log-id"
  - "日志标识符"
---

## Related Concepts
- [[concepts/Controller|Controller]]
- [[concepts/Timeout|Timeout]]

## Related Entities
- [[entities/Channel|Channel]]
- [[entities/Controller|Controller]]
- [[entities/brpc|brpc]]
- [[entities/brpc::Controller|brpc::Controller]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "set_log_id() sets a 64-bit integral log_id, which is sent to the server-side along with the request, and often printed in server logs to associate different services accessed in a session."
> - "String-type log-id must be converted to 64-bit integer before setting."

> **Source: [[sources/client|client]]**
> - "通过set_log_id()可设置64位整型log_id。这个id会和请求一起被送到服务器端，一般会被打在日志里，从而把一次检索经过的所有服务串联起来。"
> - "字符串格式的需要转化为64位整形才能设入log_id。"