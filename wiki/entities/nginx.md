---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_http_service]]"
  - "[[brpc/server.md]]"
tags:
  - "product"
aliases:
  - "nginx"
  - "NGINX"
---

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/HealthReporter|HealthReporter]]

## Related Concepts

- [[concepts/单线程反应器|单线程反应器]]
- [[concepts/事件驱动架构|事件驱动架构]]
- [[concepts/内置服务|内置服务]]
- [[concepts/HTTP-2|HTTP/2]]
- [[concepts/SSL-TLS|SSL/TLS]]
- [[concepts/SSL|SSL]]
- [[concepts/SNI|SNI]]
- [[concepts/HTTP header|HTTP header]]
- [[concepts/Status code|Status code]]
- [[concepts/反向代理|反向代理]]
- [[concepts/Proxy_method|Proxy_method]]
- [[concepts/安全|安全]]

## Mentions in Source

> **Source: [[sources/单线程反应器|单线程反应器]]**
> - "Nginx：早期版本也采用类似的事件驱动单线程模型（master-worker 架构中 worker 为单线程）。"

> **Source: [[sources/en_server|en_server]]**
> - "If client is nginx, remote_side() is address of nginx. To get address of the "real" client before nginx, set `proxy_header ClientIp $remote_addr;` in nginx and call `controller->http_request().GetHeader("ClientIp")` in RPC to get the address."
> - "nginx etc is able to configure how to map different URLs to back-end servers. For example the configure below maps public traffic to /MyAPI to `/ServiceName/MethodName` of `target-server`."
> - "If builtin services like /status are accessed from public, nginx rejects the attempts directly."
> - "location /MyAPI { ... proxy_pass http://<target-server>/ServiceName/MethodName$query_string ... }"

> **Source: [[sources/en_http_service|en_http_service]]**
> - "The error is caused by that brpc server closes the http connection directly without sending a response."
> - "When using Nginx to forward traffic, set `$HTTP_method` to allowed HTTP methods or simply specify the HTTP method in `proxy_method`."
> - "Q: The nginx before brpc encounters final fail — brpc/en_http_service"

> **Source: [[sources/server|server]]**
> - "如果client是nginx，remote_side()是nginx的地址。要获取真实client的地址，可以在nginx里设置`proxy_header ClientIp $remote_addr;`, 在rpc中通过`controller->http_request().GetHeader("ClientIp")`获得对应的值。"
> - "http proxy指定转发路径。nginx等可配置URL的映射关系，比如下面的配置把访问/MyAPI的外部流量映射到`target-server`的`/ServiceName/MethodName`。"