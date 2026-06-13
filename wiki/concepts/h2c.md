---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_http_service]]"
tags:
  - "term"
aliases:
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "H2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/h2服务"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "H2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2 (h2)"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "H2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/h2服务"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
  - "H2"
  - "HTTP/2未加密"
  - "h2协议"
  - "HTTP/2"
  - "HTTP/2未加密"
  - "h2协议"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/connections-监控页面|connections-监控页面]]
- [[entities/curl|curl]]
- [[entities/progressiveattachment|progressiveattachgement]]
- [[entities/ssl-tls|SSL/TLS]]

## 其他名称
- HTTP/2 cleartext
- HTTP/2 over TCP

## 概述
h2c是HTTP/2协议在没有SSL加密时的简称，与加密的h2相对。brpc框架将HTTP/2协议统称为"h2"，但在/connections页面上区分显示：未加密的连接显示为"h2c"，加密的连接显示为"h2"。brpc中HTTP和h2的API基本相同，h2c作为h2的一种变体，与h2共享相同的编程接口和功能。

## 更多信息
- brpc将HTTP/2协议统称为"h2"，无论是否加密。
- 在/connections页面，未加密的HTTP/2连接以官方名称"h2c"显示，加密的连接显示为"h2"。
- brpc中HTTP和h2的API基本相同。