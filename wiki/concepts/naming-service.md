---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/circuit_breaker]]"
  - "[[brpc/load_balancing.md]]"
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
  - "NamingService"
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

## Description
命名服务是分布式 RPC 系统中服务发现的基础组件，负责将抽象的服务名解析为下游节点列表，使上游能够通过多种负载均衡策略（如一致性哈希、随机、最小延迟等）将流量分配给下游节点。在 brpc 中，命名服务通过 `NamingService` 接口（在 `src/brpc/naming_service.h` 中定义）暴露给用户，实现可以基于 DNS、ZooKeeper、etcd 等多种后端，百度内部则使用自研的 BNS（Baidu Naming Service）。brpc 设计上采用了反转控制（IoC）原则：用户实现 `NamingService` 后通过 `NamingService::RunNamingService` 主动启动该过程，并在获取节点列表后调用 `NamingServiceActions::ResetServers` 接口将结果反馈给框架，而不是由 brpc 周期性调用用户的轮询函数。这种设计避免了周期性轮询带来的开销，能够充分利用 ZooKeeper 等支持事件通知（watch）的命名服务。在使用上，brpc 通过 `"protocol://node-name"` 的字符串格式指定命名服务来源，例如 `Init("bns://node-name", ...)`、`Init("http://domain-name", ...)`、`Init("file:///home/work/server.list", ...)`，并额外提供了 `list://` 前缀以支持逗号分隔的静态列表。其中 `http://<url>` 在 brpc 中被明确标注为 Domain Naming Service（即 DNS），借助现有的 DNS/HTTP 基础设施来解析服务名到地址列表，与 `bns://`、`file://`、`list://` 共同构成了 brpc 可扩展的命名服务协议族。看到这些熟悉的字符串格式，也容易联想到 `ftp://`、`zk://`、`galileo://` 等都是可以支持的——任何实现了 `NamingService` 接口的协议都可以仿照 `global.cpp` 中的注册方式进行扩展。当某个节点出现故障时，brpc 会自动将其从可用节点列表中剔除，并周期性地对故障节点进行健康检查，从而保证流量分配的可靠性。

## Related Concepts
- [[concepts/load-balancing|负载均衡]]
- [[concepts/health-check|健康检查]]
- [[concepts/naming-service-interface|NamingService 接口]]
- [[concepts/naming-service-actions|NamingServiceActions]]
- [[concepts/periodic-naming-service|PeriodicNamingService]]
- [[concepts/inversion-of-control|反转控制]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bns|BNS]]
- [[entities/baidu|百度]]
- [[entities/etcd|etcd]]
- [[entities/zookeeper|ZooKeeper]]
- [[entities/namingservicethread|namingservicethread]]
- [[entities/namingservicewatcher|namingservicewatcher]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "Machines are discovered by a Naming Service, which can be implemented by DNS, ZooKeeper or etcd."
> - "Inside Baidu, we use BNS (Baidu Naming Service)."
> - "In brpc accessing BNS is expressed as `Init("bns://node-name", ...)`, DNS is `Init("http://domain-name", ...)` and local machine list is `Init("file:///home/work/server.list", ...)`."
> - "brpc provides 'list://' and 'file://' as well."
> - "Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd). — [[brpc/en_overview|en_overview]]"
> - "DNS is `Init("http://domain-name", ...)`" — [[sources/en_overview|en_overview]]"

> **Source: [[sources/circuit_breaker|circuit_breaker]]**
> - "当我们发起一个rpc之后，brpc首先会从命名服务(naming service)拿到一个可用节点列表，之后根据负载均衡策略挑选出一个节点作为实际访问的节点。"
> - "当某个节点出现故障时，brpc能够自动将它从可用节点列表中剔除，并周期性的对故障节点进行健康检查。"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "上游一般通过命名服务发现所有的下游节点，并通过多种负载均衡方法把流量分配给下游节点。"
> - "在brpc中，NamingService用于获得服务名对应的所有节点。"
> - "所以我们反转了控制权：不是我们调用用户函数，而是用户在获得列表后调用我们的接口，对应NamingServiceActions。"
> - "当然我们还是得启动进行这一过程的函数，对应NamingService::RunNamingService。"
> - "NamingService 用于获得服务名对应的所有节点。— [[brpc/load_balancing|load_balancing]]"
> - "所以我们反转了控制权：不是我们调用用户函数，而是用户在获得列表后调用我们的接口，对应NamingServiceActions。— [[brpc/load_balancing|load_balancing]]"
> - "当然我们还是得启动进行这一过程的函数，对应NamingService::RunNamingService。— [[brpc/load_balancing|load_balancing]]"
> - "http://<url>                 # Domain Naming Service, aka DNS. — [[brpc/load_balancing|load_balancing]]"
> - "看到这些熟悉的字符串格式，容易联想到ftp:// zk:// galileo://等等都是可以支持的。— [[brpc/load_balancing|load_balancing]]"