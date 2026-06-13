---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
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
  - "HTTP/H2服务"
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

## Related Concepts
- [[concepts/restful-url映射|Restful URL映射]]
- [[concepts/http-headers|HTTP headers]]
- [[concepts/content-type|Content-Type]]
- [[concepts/status-code|Status Code]]
- [[concepts/query-string|Query String]]
- [[concepts/ssl-tls|SSL/TLS]]
- [[concepts/http-h2服务|HTTP/H2服务]]
- [[concepts/https|HTTPS]]
- [[concepts/ssl|SSL]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/connections-监控页面|connections-监控页面]]
- [[entities/curl|curl]]
- [[entities/progressiveattachment|progressiveattachgment]]
- [[entities/ssl-tls|SSL/TLS]]
- [[entities/controller|Controller]]

## Mentions in Source

> **Source: [[sources/http_service|http_service]]**
> - "这里指我们通常说的http/h2服务，而不是可通过http/h2访问的pb服务。"
> - "虽然用不到pb消息，但brpc中的http/h2服务接口也得定义在proto文件中，只是request和response都是空的结构体。"
> - "brpc把HTTP/2协议统称为"h2"，不论是否加密。"
> - "brpc把HTTP/2协议统称为"h2"，不论是否加密。然而未开启ssl的HTTP/2连接在/connections中会按官方名称h2c显示，而开启ssl的会显示为h2。"
> - "brpc中http和h2的编程接口基本没有区别。除非特殊说明，所有提到的http特性都同时对h2有效。"