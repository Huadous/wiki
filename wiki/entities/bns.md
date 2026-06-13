---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
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
- [[entities/baidu|baidu]] — BNS 是百度内部开发的命名服务系统，也是百度内部最常用的命名服务
- [[entities/brpc|brpc]] — BNS 是其可插拔命名服务实现之一，通过 `bns://` 前缀访问；brpc 还提供 `list://` 和 `file://` 等替代方案
- [[entities/zookeeper|zookeeper]] — BNS 与 ZooKeeper 类似，同为命名服务的实现方案
- [[entities/etcd|etcd]] — BNS 与 etcd 类似，同为命名服务的实现方案

## Related Concepts
- [[concepts/naming-service|naming service]] — BNS 属于命名服务的一种实现，且是百度内部最常用的命名服务
- [[concepts/load-balancing|load balancing]] — BNS 与 brpc 的负载均衡器配合实现机器选择
- [[concepts/periodicservicenaming|periodic naming service]] — 因 BNS 无事件通知，brpc 通过 `PeriodicNamingService` 定期拉取最新节点列表（默认 5 秒，可通过 `-ns_access_interval` gflag 调节）
- [[concepts/channel|channel]] — BNS 中状态位非零的机器不会被加入 Channel 的候选服务器列表
- [[concepts/命名服务过滤器|naming service filter]] — BNS 返回的机器列表包含 status 状态位，brpc 通过命名服务过滤器机制过滤掉 status 非 0 的不可用机器

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

> **来源：[[sources/en_client|en_client]]**
- "BNS is the most common naming service inside Baidu. In `bns://rdev.matrix.all`, `bns` is protocol and `rdev.matrix.all` is service-name."
- "If the list in BNS is non-empty, but Channel says `no servers`, the status bit of the machine in BNS is probably non-zero."

> **来源：[[sources/client|client]]**
- "BNS是百度内常用的命名服务，比如bns://rdev.matrix.all，其中"bns"是protocol，"rdev.matrix.all"是service-name。"
- "如果BNS中显示不为空，但Channel却说找不到服务器，那么有可能BNS列表中的机器状态位（status）为非0，含义为机器不可用，所以不会被加入到server候选集中．状态位可通过命令行查看："
- "`get_instance_by_service [bns_node_name] -s`"