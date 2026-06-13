---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_backup_request]]"
  - "[[brpc/en_client.md]]"
tags:
  - "term"
aliases:
  - "ChannelOptions"
  - "brpc ChannelOptions"
  - "Channel 选项"
---

## Related Concepts
- [[concepts/channel|Channel]]
- [[concepts/selectivechannel|SelectiveChannel]]
- [[concepts/controller|Controller]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/backup-request-ms|backup_request_ms]]
- [[concepts/timeout|Timeout]]
- [[concepts/retry|Retry]]
- [[concepts/connection-type|Connection Type]]
- [[concepts/load-balancing|负载均衡]]
- [[concepts/authentication|Authentication]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/en_backup_request]]**
> - "when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server"
> - "If the response is not returned after channelOptions.backup_request_ms ms, then another sub channel is visited."

> **Source: [[sources/en_client]]**
> - "Like most classes, Channel must be Init()-ed before usage. Parameters take default values when `options` is NULL. If you want non-default values, code as follows:"
> - "brpc::ChannelOptions: defined in src/brpc/channel.h, for initializing Channel, becoming immutable once the initialization is done."