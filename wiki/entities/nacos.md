---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "product"
aliases:
  - "Alibaba Nacos"
  - "NacosNamingService"
  - "nacos"
---

## Related Entities
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/consul|Consul]]

## Related Concepts
- [[concepts/naming-service|Naming Service]]
- [[concepts/naming-service-filter|Naming Service Filter]]
- [[concepts/naming-service-url|Naming Service URL]]
- [[concepts/weighted-round-robin|Weighted Round Robin (wrr)]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "NacosNamingService gets a list of servers from nacos periodically by Open-Api."
> - "NacosNamingService supports simple authentication."
> - "The server list is cached for `cacheMillis` milliseconds as specified in the response of `/nacos/v1/ns/instance/list` api."
> - "NOTE: The value of server weight must be an integer."

> **Source: [[sources/client|client]]**
> - "`nacos://<service-name>`：NacosNamingService使用Open-Api定时从nacos获取服务列表。NacosNamingService支持简单鉴权。"
> - "NacosNamingService拉取列表的时间间隔为`/nacos/v1/ns/instance/list` api返回的cacheMillis。NacosNamingService只支持整形的权重值。"