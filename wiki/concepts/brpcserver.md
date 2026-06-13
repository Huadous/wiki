---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "term"
aliases:
  - "brpc Server"
  - "Server"
  - "ServerOptions"
  - "brpc Server"
  - "Server"
  - "brpc::Server"
  - "brpc Server"
  - "Server"
  - "ServerOptions"
  - "brpc Server"
  - "Server"
  - "AddService"
  - "brpc Server"
  - "Server"
  - "ServerOptions"
  - "brpc Server"
  - "Server"
  - "brpc::Server"
  - "brpc Server"
  - "Server"
  - "ServerOptions"
  - "brpc Server"
  - "Server"
---

## Related Concepts
- [[concepts/限流|限流]]
- [[concepts/数据局部存储|数据局部存储]]
- [[concepts/SSL/TLS|SSL/TLS]]
- [[concepts/Authenticator|Authenticator]]
- [[concepts/优雅退出|优雅退出]]
- [[concepts/协议支持|协议支持]]
- [[concepts/内置服务|内置服务]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/echoservice|EchoService]]
- [[entities/datafactory|DataFactory]]
- [[entities/iobuf|IOBuf]]
- [[entities/redisauthenticator|RedisAuthenticator]]
- [[entities/certinfo|CertInfo]]
- [[entities/dp系统|DP系统]]
- [[entities/nova_pbrpc|Nova_pbrpc]]
- [[entities/curl|cURL]]
- [[entities/bvar|bvar]]
- [[entities/serviceoptions|ServiceOptions]]
- [[entities/authcontext|AuthContext]]
- [[entities/Authenticator|Authenticator]]
- [[entities/HealthReporter|HealthReporter]]
- [[entities/Protocol Buffers|Protocol Buffers]]
- [[entities/brpc::Controller|brpc::Controller]]
- [[entities/brpc::ServerOptions|brpc::ServerOptions]]

## Mentions in Source

> **Source: [[sources/server|server]]**
> - "Service在插入brpc.Server后才可能提供服务。"
> - "默认构造后的Server不包含任何服务，也不会对外提供服务，仅仅是一个对象。"
> - "调用以下Server的接口启动服务。"
> - "一个server只能监听一个端口（不考虑ServerOptions.internal_port），需要监听N个端口就起N个Server。"