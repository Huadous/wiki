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

## Related Entities
- [[entities/Apache|Apache]] — brpc 所属的开源软件基金会，一致性哈希功能作为 brpc 内置能力随 Apache brpc 发布
- [[entities/butil|butil]] — brpc 基础库，一致性哈希所依赖的底层数据结构与并发原语由其提供

## Related Concepts
- [[concepts/load_balancing|brpc Naming Service 与负载均衡]] — 一致性哈希所属的 brpc 流量调度体系
- [[concepts/channel|Channel]] — 一致性哈希的启用入口，通过 `Channel.Init` 指定 `load_balancer_name`
- [[concepts/channeloptions|ChannelOptions]] — Channel 配置选项，与 `load_balancer_name` 配合配置一致性哈希
- [[concepts/naming_service|Naming Service]] — 为一致性哈希提供服务器列表与节点变化感知
- [[concepts/consistent_hashing|一致性哈希]] — 本页核心主题，对应的分布式负载均衡理论
- [[concepts/virtual_node|虚拟节点]] — 在一致性哈希 Hash Ring 上用于均匀分布负载的虚拟副本
- [[concepts/hash_ring|Hash Ring]] — 一致性哈希的环形哈希空间，brpc 选择有序数组作为其底层存储结构
- [[concepts/murmurhash3|murmurhash3]] — brpc 一致性哈希内置支持的两种哈希算法之一，对应 `c_murmurhash`
- [[concepts/md5|md5]] — brpc 一致性哈希内置支持的两种哈希算法之一，对应 `c_md5`
- [[concepts/doublebuffereddata|DoubleBufferedData]] — brpc 用来保证一致性哈希数据结构线程安全的并发机制

## Mentions in Source
> **Source: [[sources/load_balancing|load_balancing]]**
> - （现有相关引用已保留于 load_balancing 主题页中，本页聚焦 consistent_hashing 来源的新增提及）

> **Source: [[sources/consistent_hashing|consistent_hashing]]**
> - "由于节点故障和变化不常发生，我们选择了修改复杂度为O(n)的有序数组来存储hash ring，每次分流使用二分查找来选择对应的机器，由于存储是连续的，查找效率比基于平衡二叉树的实现高。"
> - "我们内置了分别基于murmurhash3和md5两种hash算法的实现，使用要做两件事：在Channel.Init 时指定*load_balancer_name*为 \"c_murmurhash\" 或 \"c_md5\"。"