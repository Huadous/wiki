---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
tags:
  - "project"
aliases:
  - "Apache ZooKeeper"
  - "zk"
  - "ZooKeeper"
---

## Related Entities
- [[entities/brpc|brpc]] — brpc 支持通过 ZooKeeper 进行服务注册与发现，其命名服务抽象层可灵活集成 ZooKeeper，可在配置中使用 "zk://" 协议指定。
- [[entities/etcd|etcd]] — 另一种分布式键值存储，与 ZooKeeper 类似的协调服务，同样可作为命名服务实现方案。
- [[entities/bns|bns]] — 百度命名服务（BNS）是 ZooKeeper 的可替代方案之一。
- [[entities/baidu|baidu]] — 百度内部广泛使用 ZooKeeper 作为分布式协调组件。

## Related Concepts
- [[concepts/dns|DNS]] — 域名系统，ZooKeeper 在命名服务场景中的对比对象和替代方案之一。
- [[concepts/load-balancing|Load Balancing]] — 负载均衡，ZooKeeper 帮助管理服务实例列表，是实现负载均衡的关键组件。
- 命名服务 — ZooKeeper 作为分布式命名服务实现，帮助服务实例发现，是 brpc 中多个可选命名服务之一。

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd."
- "customize components, including naming services (dns, zk, etcd)"
- "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd)."