---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
  - "[[brpc/en_client.md]]"
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
- [[concepts/PROTOCOL_HTTP|PROTOCOL_HTTP]]
- [[concepts/PROTOCOL_H2|PROTOCOL_H2]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/hulu_pbrpc|hulu_pbrpc]]
- [[entities/brpc::Controller|brpc::Controller]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/serviceoptions|ServiceOptions]]
- [[entities/brpc::Channel|brpc::Channel]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
> - "From a server's perspective, data set in Controller.response_attachment() will be received by the client while Controller.request_attachment() contains attachment sent from the client."
> - "In http, attachment corresponds to message body"
> - "Attachment is not compressed by framework."
> - "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
> - "From a server's perspective, data set in Controller.response_attachment() will be received by the client."

> **Source: [[sources/server|server]]**
> - "baidu_std和hulu_pbrpc协议支持传递附件，这段数据由用户自定义，不经过protobuf的序列化。站在server的角度，设置在Controller.response_attachment()的附件会被client端收到，Controller.request_attachment()则包含了client端送来的附件。"
> - "附件不会被框架压缩。"
> - "在http协议中，附件对应message body，比如要返回的数据就设置在response_attachment()中。"

> **Source: [[sources/en_client|en_client]]**
> - "baidu_std and hulu_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf."
> - "As a client, data set in Controller::request_attachment() will be received by server and response_attachment() contains attachment sent back by the server."
> - "Attachment is not compressed by framework."
> - "No directly relevant information"