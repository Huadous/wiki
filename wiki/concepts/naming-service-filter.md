---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client|en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "method"
aliases:
  - "brpc::NamingServiceFilter"
  - "ns_filter"
  - "命名服务过滤器"
---

## Related Concepts
- [[concepts/naming-service|Naming Service]]
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/channel-options|ChannelOptions]]

## Related Entities
- [[entities/brpc-channel|brpc::Channel]]

## Mentions in Source

> **Source: [[sources/en_client|en_client]]**
> - "Users can filter servers got from the NamingService before pushing to LoadBalancer."
> - "class NamingServiceFilter { public: virtual bool Accept(const ServerNode& server) const = 0; };"
> - "Customized filter is set to ChannelOptions to take effects. NULL by default means not filter."

> **Source: [[sources/client|client]]**
> - "当命名服务获得机器列表后，可以自定义一个过滤器进行筛选，最后把结果传递给负载均衡"
> - "class NamingServiceFilter { virtual bool Accept(const ServerNode& server) const = 0; };"
> - "自定义的过滤器配置在ChannelOptions中，默认为NULL（不过滤）。"