---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [term]
aliases:
  - "Virtual IP"
  - "VIP (Virtual IP)"
  - "layer-4 load balancer VIP"
---


# VIP

## 定义
VIP（Virtual IP，虚拟 IP）是四层负载均衡器（layer-4 load balancer）的公网 IP 地址。它代理客户端流量并转发到其背后的真实服务器（RS）。当 brpc 客户端连接到 VIP 时，会建立一个 TCP 连接到一个被选中的真实服务器；若该客户端连接断开，则对应到该 RS 的连接也会被重置。

## 关键特征
- VIP 是四层负载均衡器的对外 IP，本身不对应单一物理节点，而是后端多个真实服务器（RS）的统一入口。
- 客户端与 VIP 之间建立的连接，本质上被负载均衡器映射到某一个被选中的 RS。
- 客户端连接断开时，对应的 RS 连接也会随之重置。
- 如果客户端只与 VIP 建立一条连接（即 brpc 中的 "single" 连接类型），该客户端的所有流量都会落在同一台 RS 上，容易造成热点。
- 在客户端数量少或各客户端负载差异较大时，VIP 模式更容易出现负载不均的问题。

## 应用
- **统一接入入口**：在 brpc 客户端通过 VIP 接入后端 RS 集群时，VIP 作为单一访问点屏蔽后端拓扑。
- **缓解热点问题**：
  - 使用 pooled（连接池）连接类型，让单个客户端可以与不同 RS 建立多条连接。
  - 使用 wrr（加权轮询）负载均衡器，为多个 VIP 分配权重以分散流量。
  - 为 VIP 打上不同标签（tag），通过命名服务将一个 VIP 拆分为更多实例。
- **高性能受限场景**：当连接数受限且追求极致性能时，可使用单连接配合带标签的 VIP 组合方案。

## 相关概念
- [[concepts/wrr|wrr]]
- [[concepts/load-balancer|Load Balancer]]
- [[concepts/connection-type|Connection Type]]
- [[concepts/naming-service-filter|Naming Service Filter]]

## 相关实体
无相关实体。

## 来源提及
- "VIP is often the public IP of layer-4 load balancer, which proxies traffic to RS behide. When a client connects to the VIP, a connection is established to a chosen RS. When the client connection is broken, the connection to the RS is reset as well." — [[sources/en_client]]
- "If one client establishes only one connection to the VIP("single" connection type in brpc), all traffic from the client lands on one RS." — [[sources/en_client]]