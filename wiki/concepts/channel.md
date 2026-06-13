---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/http_client]]"
  - "[[brpc/en_backup_request.md]]"
tags:
  - "term"
aliases:
  - "brpc::Channel"
  - "Channel 类"
---

## Related Concepts
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/url-host-field|URL 与 Host 字段]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/channel-options|ChannelOptions]]
- [[concepts/selective-channel|SelectiveChannel]]
- [[concepts/backup-request-ms|backup_request_ms]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/exampleselective_echo_c++|exampleselective_echo_c++]]

## Mentions in Source

> **Source: [[sources/http_client]]**
> - "brpc::Channel可访问http/h2服务，ChannelOptions.protocol须指定为PROTOCOL_HTTP或PROTOCOL_H2。"
> - "设定好协议后，`Channel::Init`的第一个参数可为任意合法的URL。注意：允许任意URL是为了省去用户取出host和port的麻烦，`Channel::Init`只用其中的host及port，其他部分都会丢弃。"

> **Source: [[sources/en_backup_request]]**
> - "Channel opens backup request. Channel sends the request to one of the servers and when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server, taking the response that coming back first."
> - "Define a SelectiveChannel that sets backup request, in which contains two sub channel."