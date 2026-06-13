---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "product"
aliases:
  - "Baidu Naming Service"
  - "百度命名服务"
  - "BNS (Baidu Naming Service)"
  - "Baidu Naming Service"
  - "百度命名服务"
---

## Related Entities
- [[entities/baidu|baidu]] — BNS 是百度内部开发的命名服务系统
- [[entities/brpc|brpc]] — BNS 是其可插拔命名服务实现之一，通过 `bns://` 前缀访问；brpc 还提供 `list://` 和 `file://` 等替代方案
- [[entities/zookeeper|zookeeper]] — BNS 与 ZooKeeper 类似，同为命名服务的实现方案
- [[entities/etcd|etcd]] — BNS 与 etcd 类似，同为命名服务的实现方案

## Related Concepts
- [[concepts/naming-service|naming service]] — BNS 属于命名服务的一种实现
- [[concepts/load-balancing|load balancing]] — BNS 与 brpc 的负载均衡器配合实现机器选择
- [[concepts/periodicservicenaming|periodic naming service]] — 因 BNS 无事件通知，brpc 通过 `PeriodicNamingService` 定期拉取最新节点列表（默认 5 秒）

## Mentions in Source

> **来源：[[sources/en_overview|en_overview]]**
- "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd. Inside Baidu, we use BNS (Baidu Naming Service)."
- "In brpc accessing BNS is expressed as `Init("bns://node-name", ...)`, DNS is `Init("http://domain-name", ...)` and local machine list is `Init("file:///home/work/server.list", ...)`. Without any explanation, you know what it means."
- "In older RPC implementations you may need to copy a pile of obscure code to make it work, however, in brpc accessing BNS is expressed as `Init("bns://node-name", ...)`"
- "Inside Baidu, we use BNS (Baidu Naming Service)."
- "brpc provides 'list://' and 'file://' as well."
- "Take naming service as an example. In older RPC implementations you may need to copy a pile of obscure code to make it work, however, in brpc accessing BNS is expressed as Init("bns://node-name", ...), DNS is Init("http://domain-name", ...) and local machine list is Init("file:///home/work/server.list", ...)."
- "Inside Baidu, we use BNS (Baidu Naming Service). brpc provides list:// and file:// as well."

> **来源：[[sources/load_balancing|load_balancing]]**
- "bns：没有事件通知，所以我们只能定期去获得最新列表，默认间隔是[5秒](http://brpc.baidu.com:8765/flags/ns_access_interval)。"
- "bns://<node-name>            # baidu naming service"
- No directly relevant information