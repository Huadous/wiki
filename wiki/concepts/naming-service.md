---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
  - "[[sources/circuit_breaker]]"
tags:
  - "method"
aliases:
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "DNS"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "NamingService（命名服务）"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "DNS"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "命名服务 (naming service)"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "DNS"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "NamingService（命名服务）"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
  - "DNS"
  - "命名服务"
  - "服务发现"
  - "命名服务 (Naming Service)"
  - "命名服务"
  - "服务发现"
---

## Related Entities
- [[entities/bns|BNS]]
- [[entities/brpc|brpc]]
- [[entities/baidu|百度]]
- [[entities/etcd|etcd]]
- [[entities/zookeeper|ZooKeeper]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd."
> - "Inside Baidu, we use BNS (Baidu Naming Service)."
> - "In brpc accessing BNS is expressed as `Init("bns://node-name", ...)`, DNS is `Init("http://domain-name", ...)` and local machine list is `Init("file:///home/work/server.list", ...)`."
> - "brpc provides 'list://' and 'file://' as well."
> - "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd). — [[brpc/en_overview|en_overview]]"
> - "DNS is `Init("http://domain-name", ...)`" — [[sources/en_overview|en_overview]]

> **Source: [[sources/circuit_breaker|circuit_breaker]]**
> - "当我们发起一个rpc之后，brpc首先会从命名服务(naming service)拿到一个可用节点列表，之后根据负载均衡策略挑选出一个节点作为实际访问的节点。"
> - "当某个节点出现故障时，brpc能够自动将它从可用节点列表中剔除，并周期性的对故障节点进行健康检查。"