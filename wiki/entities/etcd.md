---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
tags:
  - "project"
aliases:
  - "CoreOS etcd"
  - "etcd分布式键值存储"
---

## Related Entities
- [[entities/brpc|brpc]] — 支持将 etcd 用作命名服务后端的 RPC 框架
- [[entities/zookeeper|ZooKeeper]] — 另一种分布式协调服务，与 etcd 功能类似
- [[entities/bns|BNS]] — 百度命名服务，brpc 支持的其他命名服务实现
- [[entities/kubernetes|Kubernetes]] — 依赖 etcd 作为其状态存储的容器编排平台
- [[entities/baidu|百度]] — brpc 的主要开发组织，etcd 的关联生态系统
- [[entities/braft|braft]] — brpc 的 Raft 实现，与 etcd 同属分布式一致性领域

## Related Concepts
- [[concepts/naming-service|命名服务]] — 服务发现的核心概念，etcd 是其一种实现
- [[concepts/raft|Raft]] — 分布式共识算法，etcd 基于此算法实现强一致性
- [[concepts/distributed-key-value-store|分布式键值存储]] — etcd 的基本存储模型
- [[concepts/service-discovery|服务发现]] — etcd 的核心应用场景

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
- "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd." — en_overview
- "customize components, including naming services (dns, zk, etcd)" — en_overview
- "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd)." — en_overview
- "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd." — en_overview
- "etcd是一个分布式键值存储，用于配置管理和服务发现。它由CoreOS开发，采用Raft共识算法保证一致性。" — en_overview
- "在brpc中，etcd可以作为命名服务的一种实现，用于服务发现。etcd通常用作Kubernetes等系统的后端存储。" — en_overview
- "brpc用户可以通过指定etcd地址来实现服务发现。" — en_overview
- "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd)." — [[sources/en_overview|en_overview]]
- "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd)." — en_overview