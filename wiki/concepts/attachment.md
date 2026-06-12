---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "附件"
  - "附加数据"
  - "Attachment (附件)"
  - "附件"
  - "附加数据"
---

## Related Concepts
- [[concepts/baidu_std|baidu_std]]
- [[concepts/Compression|Compression]]
- [[concepts/Protobuf|Protobuf]]
- [[concepts/HTTP/JSON访问|HTTP/JSON访问]]
- [[concepts/协议自动检测|协议自动检测]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/hulu_pbrpc|hulu_pbrpc]]
- [[entities/brpc::Controller|brpc::Controller]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/serviceoptions|ServiceOptions]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
> - "From a server's perspective, data set in Controller.response_attachment() will be received by the client while Controller.request_attachment() contains attachment sent from the client."
> - "In http, attachment corresponds to message body"
> - "Attachment is not compressed by framework."
> - "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
> - "From a server's perspective, data set in Controller.response_attachment() will be received by the client."