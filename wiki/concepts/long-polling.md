---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [method]
aliases:
  - "long polling"
  - "长轮询"
---


# long polling

## 定义
long polling 是一种网络通信方式，在 brpc 与 Consul 命名服务的交互中被采用。brpc 对 Consul 的首次请求采用普通方式，但后续请求均采用 long polling——即仅当服务列表发生更新或请求超时时，Consul 才返回结果，从而减少不必要的网络请求开销。

## 关键特征
- 在 brpc 与 Consul 命名服务的交互中，除首次请求外，后续请求均采用 long polling 方式
- 仅当服务列表更新或请求超时时，Consul 才返回结果，客户端无需频繁轮询
- 减少了不必要的网络请求开销，降低了服务发现延迟
- brpc 中 long polling 的默认超时时间为 60 秒
- 可通过 `-consul_blocking_query_wait_secs` 参数自定义超时时间

## 应用
- brpc 客户端与 Consul 命名服务之间的服务发现通信
- 需要实时感知服务列表变更、同时希望降低请求频率的场景
- 对延迟和负载敏感的服务发现机制设计

## 相关概念
- [[concepts/命名服务|命名服务]]
- [[concepts/命名服务降级|命名服务降级]]

## 相关实体
- [[entities/Consul|Consul]]

## 来源提及
- "除了对consul的首次请求，后续对consul的请求都采用long polling的方式，即仅当服务列表更新或请求超时后consul才返回结果，这里超时时间默认为60s，可通过-consul_blocking_query_wait_secs来设置。" — [[sources/client|client]]