---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_overview.md]]"
tags: [RPC, Serialization, Load balancing, Naming Service, RAFT, Consistent hashing, bthread, bvar, Builtin service, Streaming RPC, Profiler, Locality-aware load balancing]
aliases: ["What is RPC? - 远程过程调用介绍", "brpc 概述文档"]
---

# What is RPC? - Summary

## 来源
- 原始文件：[[brpc/en_overview.md]]
- 录入时间：2026-06-12

## 核心内容
本文介绍了远程过程调用（RPC）的基本概念，阐明它如何利用 [[concepts/tcpip|TCP/IP]] 层解决序列化、连接管理、服务发现、负载均衡和故障恢复等分布式通信问题。文章重点介绍了百度开源的工业级 RPC 框架 [[entities/brpc|brpc]]，详细阐述了它的易用性、高可靠性、高性能特点，包括多协议支持（HTTP/h2、[[entities/grpc|gRPC]]、[[entities/redis|Redis]]、[[entities/memcached|Memcached]]、[[entities/thrift|thrift]] 等）、多负载均衡算法、命名服务集成以及丰富的内置调试工具。文章还涉及 [[concepts/bthread|bthread]] 轻量级线程模型和 [[entities/braft|braft]] Raft 共识算法实现。brpc 在百度内部广泛使用，拥有超过 100 万个实例。

## 关键实体
- [[entities/brpc|brpc]]：百度开源的高性能工业级 RPC 框架，本文核心介绍对象
- [[entities/baidu|百度]]：brpc 的开发者和主要使用者
- [[entities/protobuf|protobuf]]：默认序列化方案
- [[entities/bns|BNS]]：百度内部命名服务
- [[entities/braft|braft]]：基于 Raft 共识算法的高可用服务构建组件
- [[entities/grpc|gRPC]]：brpc 原生支持的协议之一
- [[entities/redis|Redis]]：brpc 支持的协议
- [[entities/memcached|Memcached]]：brpc 支持的协议
- [[entities/thrift|thrift]]：brpc 支持的协议
- [[entities/zookeeper|ZooKeeper]]：可选的命名服务实现
- [[entities/etcd|etcd]]：可选的命名服务实现
- [[entities/bvar|bvar]]：内置性能监控库

## 关键概念
- [[concepts/rpc|RPC]]：远程过程调用，本文的核心主题
- [[concepts/tcpip|TCP/IP]]：互联网通信的底层协议栈
- [[concepts/serialization|序列化]]：解决数据传输格式的兼容性问题
- [[concepts/naming-service|命名服务]]：服务发现机制（DNS、ZooKeeper、etcd、BNS）
- [[concepts/load-balancing|负载均衡]]：包括轮询、随机、[[concepts/consistent-hashing|一致性哈希]]和 [[concepts/locality-aware-load-balancing|局部感知]]算法
- [[concepts/raft-consensus-algorithm|RAFT]]：braft 支持的共识算法
- [[concepts/bthread|bthread]]：轻量级线程模型，用于动态调整并发
- [[concepts/io-thread-model|IO 线程模型]]：完全并行的请求处理架构
- [[concepts/connection-pooling|连接池]]：复用 TCP 连接减少开销
- [[concepts/retry|重试]]：连接断开时的自动重试机制
- [[concepts/timeout|超时]]：控制请求等待时间的参数
- [[concepts/wait-free|无等待算法]]：多线程写入 fd 时的关键技术
- [[concepts/builtin-service|内置服务]]：用于在线调试和性能分析的 HTTP 服务集合
- [[concepts/parallel-message-processing|并行消息处理]]：同连接内的消息可并行处理

## 要点
- RPC 解决了序列化、连接管理、服务发现、负载均衡和故障恢复等分布式通信核心问题
- brpc 支持多协议在同一端口共存，并提供同步、异步、半同步等多种调用模式
- brpc 通过并行化读写、最小化锁竞争、使用 bthread 轻量级线程实现高吞吐和低延迟
- brpc 支持多种命名服务（BNS、DNS、ZooKeeper、etcd）和负载均衡算法
- brpc 提供 braft 实现 Raft 共识算法，内置丰富的调试和服务治理工具