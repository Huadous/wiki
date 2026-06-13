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
brpc是Apache开源的工业级RPC框架项目，代码仓库托管在GitHub上（apache/brpc），由百度发起并开源，提供了高性能网络通信与基础库实现，包含butil等多个子模块。其核心包含内存管理（默认使用jemalloc以提升多线程内存分配性能）、IO模型（基于EventDispatcher等待fd事件，通过Socket/SocketId机制管理连接生命周期，Socket类似shared_ptr而SocketId类似weak_ptr但支持SetFailed确保优雅退出）、数据传输（butil::IOBuf作为非连续零拷贝缓冲）、HTTP/H2服务（服务端通过Controller暴露header和body，支持URL路由、参数处理、压缩、HTTPS等特性）、HTTP/H2客户端（通过brpc::Channel访问，需指定PROTOCOL_HTTP或PROTOCOL_H2协议）、服务发现与负载均衡（Naming Service）、JSON-protobuf双向转化（json2pb，支持pb 2.x和3.x）、流式RPC（streaming_rpc）、Redis客户端、RDMA支持、熔断机制（circuit breaker）、备用请求（backup request）以及内置服务（builtin service）等核心模块。brpc Server基于bthread构建，支持多种并发模型和协议，鼓励静态链接依赖以便部署机器无需重复安装。butil作为brpc的基础工具库，包含FlatMap等高性能容器组件和streaming_log等日志工具——其中streaming_log是brpc的流式日志机制，被广泛应用于brpc服务端和客户端的日志输出场景。FlatMap定位为"可能是最快的哈希表，以空间为代价换取速度"，是brpc基础库的重要组成部分。streaming_log与bthread协程深度结合，brpc默认通过streaming_log将高频日志分散到各bthread中并以noflush缓冲，在RPC结束时统一刷新，且其fatal日志默认不会像glog那样直接触发coredump，除非显式开启--crash_on_fatal_log gflag。

## Related Entities
- [[entities/flatmap|flatmap]] — butil 的高性能容器组件，以空间换速度
- [[entities/smalltable|smalltable]] — 百度哈希表系列
- [[entities/cowhashmap|cowhashmap]] — 百度 smalltable 系列的 COW 实现
- [[entities/alignhashmap|alignhashmap]] — 百度闭链哈希表
- [[entities/stdmap|stdmap]] — C++ 标准 map，用作 FlatMap 性能对比参照
- [[entities/homebrew|homebrew]] — macOS 上构建 brpc 的包管理工具
- [[entities/examplehttp_c++|examplehttp_c++]] — brpc HTTP 客户端示例
- [[entities/searchrequest|searchrequest]] — protobuf SearchRequest 消息示例

## Related Concepts
- [[concepts/iobuf|butil::IOBuf]] — 非连续零拷贝缓冲
- [[concepts/json2pb|json2pb]] — JSON 与 protobuf 双向转化
- [[concepts/load_balancing|brpc Naming Service 与负载均衡]] — 服务发现与流量调度
- [[concepts/memory_management|brpc 内存管理]] — ResourcePool 与 ObjectPool
- [[concepts/streaming_rpc|流式 RPC]] — Streaming RPC 概念
- [[concepts/noflush]] — streaming_log 的 noflush 缓冲策略，日志先缓冲至 RPC 结束统一刷新
- [[concepts/bthread]] — brpc 协程模型，streaming_log 将高频日志分散到各 bthread

## Mentions in Source

> **Source: [[sources/flatmap|flatmap]]**
> - "FlatMap - Maybe the fastest hashmap, with tradeoff of space" (FlatMap — 可能是最快的哈希表，以空间为代价换取速度)
> - "butil/containers/flat_map.h"（位于 [src/butil/containers/flat_map.h](https://github.com/apache/brpc/blob/master/src/butil/containers/flat_map.h)）

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "you can push lots of logs from the server's bthreads without actually print them (using noflush), and flush the whole log at the end of RPC."
> - "since most fatal log inside baidu is not fatal actually, it won't trigger coredump directly as glog, unless you turn on -crash_on_fatal_log"