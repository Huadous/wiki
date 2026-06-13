---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [product]
aliases:
  - "HashiCorp Consul"
  - "Consul"
---


# Consul

## 基本信息
- Type: product
- Source: [[sources/en_client]]

## 描述
Consul 是 HashiCorp 提供的服务网格（service mesh）与服务发现（service discovery）产品，同时也是 [[sources/load_balancing|brpc Naming Service]] 所支持的命名服务后端之一。brpc 通过 `consul://` URL scheme 向 Consul agent 查询指定 service-name 下已注册的健康服务器列表，默认连接地址为 `localhost:8500`，可通过 gflag `-consul_agent_addr` 进行修改。为了高效跟踪服务列表的变化，brpc 集成利用了 Consul 的 long polling / blocking-query 特性，其阻塞查询超时时间由 `-consul_blocking_query_wait_secs` 控制（默认 60 秒），失败重试间隔由 `-consul_retry_interval_ms` 控制（默认 500 毫秒），两者均通过 gflags 暴露。当 Consul 不可用时，brpc 还可以选择性地降级为基于文件的命名服务（`-consul_enable_degrade_to_file_naming_service`），使用最近一次成功获取的服务器列表快照继续提供服务发现能力。该集成通过 [[concepts/naming-service|Naming Service]] 接口对外暴露，因此可以与 [[concepts/naming-service-filter|Naming Service Filter]] 以及 [[concepts/naming-service-url|Naming Service URL]] 机制协同工作。

## 相关实体
No related entities

## 相关概念
- [[concepts/naming-service|Naming Service]]
- [[concepts/naming-service-filter|Naming Service Filter]]
- [[concepts/naming-service-url|Naming Service URL]]

## 来源提及
- "Get a list of servers with the specified service-name through consul. The default address of consul is localhost:8500, which can be modified by setting -consul_agent_addr in gflags." — [[sources/en_client]]
- "Except the first request to consul, the follow-up requests use the long polling feature. That is, the consul responds only when the server list is updated or the request times out." — [[sources/en_client]]