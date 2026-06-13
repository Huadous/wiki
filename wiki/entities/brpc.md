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
- [[entities/flatmap|flatmap]] — butil 的高性能容器组件，以空间换速度
- [[entities/smalltable|smalltable]] — 百度哈希表系列
- [[entities/cowhashmap|cowhashmap]] — 百度 smalltable 系列的 COW 实现
- [[entities/alignhashmap|alignhashmap]] — 百度闭链哈希表
- [[entities/stdmap|stdmap]] — C++ 标准 map，用作 FlatMap 性能对比参照
- [[entities/homebrew|homebrew]] — macOS 上构建 brpc 的包管理工具
- [[entities/examplehttp_c++|examplehttp_c++]] — brpc HTTP 客户端示例
- [[entities/searchrequest|searchrequest]] — protobuf SearchRequest 消息示例
- [[entities/Apache|Apache]] — brpc 所属的开源软件基金会
- [[entities/butil|butil]] — brpc 基础库，提供 IOBuf 等核心数据结构
- [[entities/Kylin|Kylin]] — 早于 brpc 的项目，其 BufHandle 组件被作为 IOBuf 设计改进的对比参照

## Related Concepts
- [[concepts/iobuf|butil::IOBuf]] — 非连续零拷贝缓冲
- [[concepts/json2pb|json2pb]] — JSON 与 protobuf 双向转化
- [[concepts/load_balancing|brpc Naming Service 与负载均衡]] — 服务发现与流量调度
- [[concepts/memory_management|brpc 内存管理]] — ResourcePool 与 ObjectPool
- [[concepts/streaming_rpc|流式 RPC]] — Streaming RPC 概念
- [[concepts/noflush|noflush]] — streaming_log 的 noflush 缓冲策略，日志先缓冲至 RPC 结束统一刷新
- [[concepts/bthread|bthread]] — brpc 协程模型，streaming_log 将高频日志分散到各 bthread
- [[concepts/zero_copy_buffer|Zero-copy buffer]] — IOBuf 所采用的核心零拷贝设计思想
- [[concepts/reference_counting|Reference counting]] — IOBuf 自动管理资源生命周期所依赖的机制
- [[concepts/backup_request|Backup Request]] — brpc 中通过 Channel 的 backup_request_ms 实现的备份请求机制，主请求超时时自动发送备份请求并采用最先返回的响应
- [[concepts/channel|Channel]] — brpc 的客户端通道，备份请求功能的载体，通过 ChannelOptions 配置 backup_request_ms
- [[concepts/selectivechannel|SelectiveChannel]] — brpc 中另一种可结合备份请求使用的通道类型
- [[concepts/channeloptions|ChannelOptions]] — brpc Channel 的配置选项，包含 backup_request_ms 等参数
- [[concepts/backup_request_ms|backup_request_ms]] — ChannelOptions 中控制备份请求触发时机的毫秒数阈值
- [[concepts/cdf|CDF]] — Cumulative Distribution Function，brpc 用于展示请求延迟分布的内省监控指标
- [[concepts/naming_service|Naming Service]] — brpc 的服务发现机制，为 Channel 选择目标服务器提供依据
- [[concepts/bvar_latencyrecorder|bvar::LatencyRecorder]] — brpc 提供的延迟记录器，用于采集和分析请求延迟数据
- [[concepts/asynchronous_rpc|Asynchronous RPC]] — brpc 支持的异步 RPC 模式
- [[concepts/rpcz|/rpcz]] — brpc 提供的 RPC 内省端点，可查看请求追踪与备份请求触发情况

## Mentions in Source

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "brpc uses butil::IOBuf as data structure for attachment in some protocols and HTTP body."
> - "If you've used the BufHandle in Kylin before, you should notice the convenience of IOBuf: the former one is badly encapsulated, leaving the internal structure directly in front of users, who must carefully handle the referential countings, very error prone and leading to bugs."

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "There are several ways to achieve this in brpc:"
> - "Channel opens backup request. Channel sends the request to one of the servers and when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server, taking the response that coming back first."
> - "You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc, or add it by your own."