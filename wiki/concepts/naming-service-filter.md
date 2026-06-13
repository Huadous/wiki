---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [method]
aliases:
  - "brpc::NamingServiceFilter"
  - "ns_filter"
  - "命名服务过滤器"
---


# Naming Service Filter

## 定义
Naming Service Filter 是 brpc 提供的一个扩展点（extension point），允许用户在从 NamingService 获取到服务器列表之后、推送到 LoadBalancer 之前，对候选服务器进行筛选和过滤。其核心接口为 `brpc::NamingServiceFilter` 抽象类，用户通过子类化该类并实现 `virtual bool Accept(const ServerNode&) const` 方法，返回 `true` 表示保留该服务器，返回 `false` 表示丢弃该服务器。

## 关键特征
- **扩展点机制**：以抽象类 `NamingServiceFilter` 的形式定义，用户通过继承并重写 `Accept` 方法实现自定义过滤逻辑。
- **过滤位置精确**：作用于 NamingService 返回结果与 LoadBalancer 接收之间，属于"上游筛选"，不影响 LoadBalancer 自身的负载均衡算法。
- **按服务器粒度筛选**：针对每一个 `ServerNode` 单独判定，决定其是否进入下游负载均衡环节。
- **通过 ChannelOptions 注入**：自定义过滤器通过 `ChannelOptions.ns_filter` 字段挂载到 Channel 上，默认为 `NULL`（即不过滤）。
- **常见用途为按 tag 过滤**：例如保留具有特定 tag 的服务器、剔除不符合环境的实例等。
- **判定语义清晰**：`Accept` 方法命名直接体现"是否接受"的二元决策语义，便于阅读与维护。

## 应用
- **按 tag 过滤服务器**：从 NamingService 返回的全量服务器中，仅保留带有特定 tag（如机房、环境、版本灰度标签）的实例，从而实现灰度发布、流量分组等能力。
- **多环境隔离**：在混合部署场景下，过滤掉不属于当前调用方环境的服务器，避免跨环境调用。
- **客户端维度的访问控制**：针对特定 Channel 配置命名服务过滤器，限制该 Channel 只能访问经过审批的服务器集合。
- **辅助灰度与金丝雀发布**：与 NamingService 配合，在客户端入口处完成精细化的流量裁剪。

## 相关概念
- [[concepts/naming-service|Naming Service]]
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/channel-options|ChannelOptions]]

## 相关实体
No related entities

## 来源提及
- "Users can filter servers got from the NamingService before pushing to LoadBalancer." — [[sources/en_client|en_client]]
- "class NamingServiceFilter { public: virtual bool Accept(const ServerNode& server) const = 0; };" — [[sources/en_client|en_client]]
- "Customized filter is set to ChannelOptions to take effects. NULL by default means not filter." — [[sources/en_client|en_client]]