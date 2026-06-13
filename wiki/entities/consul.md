---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/en_client]]"
  - "[[brpc/client.md]]"
tags:
  - "product"
aliases:
  - "HashiCorp Consul"
  - "Consul"
---

## Description
Consul 是 HashiCorp 公司开发的服务发现与配置管理工具，也是 brpc 所支持的命名服务后端之一。brpc 通过 `consul://<service-name>` 这种 URL 格式向 Consul 查询指定 service-name 下已注册的健康服务器列表，默认连接地址为 `localhost:8500`，可通过 gflag `-consul_agent_addr` 进行修改。brpc 默认在向 Consul 发起的请求中添加 `stale` 和 `passing` 参数，以便获取通过健康检查的服务器节点。为了高效跟踪服务列表的变化，除了对 Consul 的首次请求之外，后续请求均采用 Consul 提供的 long polling / blocking-query 特性——即仅当服务列表更新或请求超时时 Consul 才返回结果；阻塞查询的超时时间默认 60 秒，可通过 `-consul_blocking_query_wait_secs` 配置，失败重试间隔由 `-consul_retry_interval_ms` 控制（默认 500 毫秒），两者均通过 gflags 暴露。当 Consul 不可用时，brpc 还可以选择性地降级为基于文件的命名服务（`-consul_enable_degrade_to_file_naming_service`），使用最近一次成功获取的服务器列表快照继续提供服务发现能力。该集成通过 [[concepts/naming-service|Naming Service]] 接口对外暴露，因此可以与 [[concepts/naming-service-filter|Naming Service Filter]] 以及 [[concepts/naming-service-url|Naming Service URL]] 机制协同工作。

## Related Entities
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/nacos|Nacos]]

## Related Concepts
- [[concepts/naming-service|Naming Service]]
- [[concepts/naming-service-filter|Naming Service Filter]]
- [[concepts/naming-service-url|Naming Service URL]]
- [[concepts/命名服务降级|命名服务降级]]
- [[concepts/long-polling|long polling]]

## Mentions in Source

> **Source: [[sources/en_client]]**
> - "Get a list of servers with the specified service-name through consul. The default address of consul is localhost:8500, which can be modified by setting -consul_agent_addr in gflags."
> - "Except the first request to consul, the follow-up requests use the long polling feature. That is, the consul responds only when the server list is updated or the request times out."

> **Source: [[sources/client]]**
> - "consul://<service-name>：通过consul获取服务名称为service-name的服务列表。consul的默认地址是localhost:8500，可通过gflags设置-consul_agent_addr来修改。"
> - "除了对consul的首次请求，后续对consul的请求都采用long polling的方式，即仅当服务列表更新或请求超时后consul才返回结果，这里超时时间默认为60s，可通过-consul_blocking_query_wait_secs来设置。"