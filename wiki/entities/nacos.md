---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [product]
aliases:
  - "Alibaba Nacos"
  - "NacosNamingService"
  - "nacos"
---


# Nacos

## 基本信息
- Type: product
- Source: [[sources/en_client|en_client]]

## 描述
Nacos 是阿里巴巴开源的动态服务发现与配置管理平台，在 brpc 中作为命名服务（[[concepts/naming-service|Naming Service]]）的一种实现，通过 `nacos://` 协议的 NamingService URL 进行接入。NacosNamingService 会周期性调用 Nacos Open API `/nacos/v1/ns/instance/list` 来获取指定 service-name 对应的健康服务器实例列表，并将结果按 API 响应中的 `cacheMillis` 值进行本地缓存。该实现支持 Nacos 的简易认证机制，用户名与密码通过 `-nacos_username` 与 `-nacos_password` gflags 以 URL 编码方式传入；负载均衡算法可通过 `-nacos_load_balancer` 配置，默认为 `"rr"`（轮询）。值得注意的是，与部分其他命名服务不同，Nacos 服务器权重必须为整数值才能被 brpc 集成正确识别和处理。

## 相关实体
- 无相关实体

## 相关概念
- [[concepts/naming-service|Naming Service]]
- [[concepts/naming-service-filter|Naming Service Filter]]
- [[concepts/naming-service-url|Naming Service URL]]

## 来源提及
- "NacosNamingService gets a list of servers from nacos periodically by Open-Api." — [[sources/en_client|en_client]]
- "NacosNamingService supports simple authentication." — [[sources/en_client|en_client]]
- "The server list is cached for `cacheMillis` milliseconds as specified in the response of `/nacos/v1/ns/instance/list` api." — [[sources/en_client|en_client]]
- "NOTE: The value of server weight must be an integer." — [[sources/en_client|en_client]]