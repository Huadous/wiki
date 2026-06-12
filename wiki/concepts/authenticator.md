---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "验证器"
  - "brpc Authenticator"
  - "连接认证器"
  - "Authentication"
  - "验证器"
  - "brpc Authenticator"
  - "连接认证器"
---

## Related Concepts
- [[concepts/ssl-tls|SSL/TLS]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/authcontext|authcontext]]
- [[entities/redisauthenticator|redisauthenticator]]
- [[entities/iobuf|iobuf]]
- [[entities/serveroptions|ServerOptions]]
- [[entities/controller|Controller]]
- [[entities/certinfo|certinfo]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - The server needs to implement `Authenticator` to enable verifications:
> - When server receives the first request from a connection, it tries to parse related information inside (such as auth field in baidu_std, Authorization header in HTTP), and call `VerifyCredential` along with address of the client.