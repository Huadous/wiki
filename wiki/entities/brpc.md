---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/lalb]]"
  - "[[sources/en_rdma]]"
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_streaming_rpc]]"
  - "[[sources/en_server]]"
  - "[[sources/rdma]]"
  - "[[sources/redis_client]]"
  - "[[sources/en_overview]]"
  - "[[sources/combo_channel]]"
  - "[[sources/en_io]]"
  - "[[sources/circuit_breaker]]"
  - "[[sources/en_http_service]]"
  - "[[sources/backup_request]]"
  - "[[sources/builtin_service]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/rdma.md]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/json2pb.md]]"
  - "[[brpc/io.md]]"
  - "[[brpc/iobuf.md]]"
  - "[[brpc/http_service.md]]"
  - "[[brpc/http_client.md]]"
  - "[[brpc/getting_started.md]]"
  - "[[brpc/flatmap.md]]"
  - "[[brpc/en_streaming_log.md]]"
  - "[[brpc/en_iobuf.md]]"
  - "[[brpc/en_backup_request.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/consistent_hashing.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bvar_c++.md]]"
tags:
  - "product"
aliases:
  - "baidu-rpc"
  - "Apache brpc"
  - "brpc (Apache brpc)"
  - "baidu-rpc"
  - "Apache brpc"
  - "Apache"
  - "baidu-rpc"
  - "Apache brpc"
  - "brpc (Apache brpc)"
  - "baidu-rpc"
  - "Apache brpc"
---

## Description
一致性哈希（Consistent Hashing）是 brpc 内置的一种分布式负载均衡策略，用于将请求稳定地分发到一组动态变化的服务器列表上。brpc 通过 `Channel.Init` 时将 `load_balancer_name` 指定为 `"c_murmurhash"` 或 `"c_md5"` 来启用该策略，并基于内置的 murmurhash3 或 md5 哈希算法在 Hash Ring 上定位目标节点。由于节点故障和扩缩容并不频繁，brpc 选择修改复杂度为 O(n) 的有序数组作为 Hash Ring 的底层存储结构，分流时通过二分查找选择对应机器，从而获得比基于平衡二叉树的实现更高的连续内存查找效率。为平滑节点变化带来的负载不均，brpc 在 Hash Ring 上引入虚拟节点（virtual node）机制，使负载更加均匀分布。该机制与 brpc 生态中的 bvar 监控组件深度集成：通过 `/vars` HTTP 服务可查询一致性哈希相关运行指标，通过 `/flags` 服务可在启动后动态修改一致性哈希相关的 gflags 参数。

## Related Entities
- [[entities/Apache|Apache]] — brpc 所属的开源软件基金会，一致性哈希功能作为 brpc 内置能力随 Apache brpc 发布
- [[entities/butil|butil]] — brpc 基础库，一致性哈希所依赖的底层数据结构与并发原语由其提供
- [[entities/bvar|bvar]] — brpc 生态中负责监控统计的核心组件，为一致性哈希运行指标提供观测能力
- [[entities/mbvar|mbvar]] — bvar 的多维度扩展，与单维度 bvar 共同构成 brpc 监控统计体系，间接支撑一致性哈希的可观测性

## Related Concepts
- [[concepts/load_balancing|brpc Naming Service 与负载均衡]] — 一致性哈希所属的 brpc 流量调度体系
- [[concepts/channel|Channel]] — 一致性哈希的启用入口，也是 brpc Client 端的实体代表，通过 `Channel.Init` 指定 `load_balancer_name`
- [[concepts/channeloptions|ChannelOptions]] — Channel 配置选项，与 `load_balancer_name` 配合配置一致性哈希，并承载线程数、长短连接等 Client 端参数
- [[concepts/naming_service|Naming Service]] — 为一致性哈希提供服务器列表与节点变化感知
- [[concepts/consistent_hashing|一致性哈希]] — 本页核心主题，对应的分布式负载均衡理论
- [[concepts/virtual_node|虚拟节点]] — 在一致性哈希 Hash Ring 上用于均匀分布负载的虚拟副本
- [[concepts/hash_ring|Hash Ring]] — 一致性哈希的环形哈希空间，brpc 选择有序数组作为其底层存储结构
- [[concepts/murmurhash3|murmurhash3]] — brpc 一致性哈希内置支持的两种哈希算法之一，对应 `c_murmurhash`
- [[concepts/md5|md5]] — brpc 一致性哈希内置支持的两种哈希算法之一，对应 `c_md5`
- [[concepts/doublebuffereddata|DoubleBufferedData]] — brpc 用来保证一致性哈希数据结构线程安全的并发机制
- [[concepts/bvar_gflag|bvar::GFlag]] — brpc 中用于将 gflags 监控接入 bvar 体系的适配器，一致性哈希相关 gflags 可借此被 `/vars` 查询、被 `/flags` 动态修改
- [[concepts/bvar_status|bvar::Status]] — bvar 提供的状态展示机制，与 `/vars` HTTP 服务共同支撑一致性哈希等 brpc 内置能力的状态可观测

## Mentions in Source
> **Source: [[sources/load_balancing|load_balancing]]**
> - （现有相关引用已保留于 load_balancing 主题页中，本页聚焦 consistent_hashing 来源的新增提及）

> **Source: [[sources/consistent_hashing|consistent_hashing]]**
> - "由于节点故障和变化不常发生，我们选择了修改复杂度为O(n)的有序数组来存储hash ring，每次分流使用二分查找来选择对应的机器，由于存储是连续的，查找效率比基于平衡二叉树的实现高。"
> - "我们内置了分别基于murmurhash3和md5两种hash算法的实现，使用要做两件事：在Channel.Init 时指定*load_balancer_name*为 \"c_murmurhash\" 或 \"c_md5\"。"

> **Source: [[sources/client|client]]**
> - "Client指发起请求的一端，在brpc中没有对应的实体，取而代之的是[brpc::Channel]，它代表和一台或一组服务器的交互通道。"（说明 Channel 是 brpc Client 端的实体代表，也是一致性哈希等负载均衡策略生效的载体。）
> - "一些RPC实现中有ClientManager的概念，包含了Client端的配置信息和资源管理。brpc不需要这些，以往在ClientManager中配置的线程数、长短连接等等要么被加入了brpc::ChannelOptions，要么可以通过gflags全局配置。"（说明一致性哈希相关参数通过 ChannelOptions 或 gflags 配置，brpc 摒弃了 ClientManager 概念。）
> - "Echo的[client端代码](https://github.com/apache/brpc/blob/master/example/echo_c++/client.cpp)。"（Echo 示例展示了包含一致性哈希在内的 Channel 典型初始化方式。）

> **Source: [[sources/bvar_c++|bvar_c++]]**
> - "单维度bvar使用文档，多维度mbvar请移步(mbvar_c++.md)。"
> - "前者在brpc中通过/vars服务提供"
> - "在brpc中也可通过/flags服务在启动后动态修改。"