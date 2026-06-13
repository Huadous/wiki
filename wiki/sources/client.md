---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/client.md]]"
tags: [命名服务, 负载均衡, 一致性哈希, backup request, 重试退避, 熔断, 健康检查, 异步访问, 同步访问, 半同步, 协议, 压缩, 连接方式, 客户端认证, 幂等性, 命名服务过滤器, wrr, la, BNS, bthread, SSL, 附件, log_id, 集群恢复限流, correlation_id, brpc::RetryPolicy, protobuf::Closure, VIP, 命名服务降级, long polling, SocketMap, baidu_std, Streaming RPC, brpc::NamingService, brpc::BackupRequestPolicy, brpc::Join, brpc::StartCancel, brpc::CallId, brpc::NewCallback, butil::IOBuf, brpc::Socket, brpc::LoadBalancer, butil::EndPoint, ParallelChannel, brpc::DoNothing]
aliases: ["brpc Client 文档", "brpc::Channel 使用指南"]
---

# brpc Client 端文档 - Summary

## 来源
- Original file: [[brpc/client.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/brpc|brpc]] 项目的 Client 端权威使用指南。brpc 中没有传统意义的 Client 实体，取而代之的是 [[entities/brpcchannel|brpc::Channel]]，它代表与一台或一组服务器的交互通道，线程安全且可被所有线程共享。文档围绕 [[entities/brpcchannel|brpc::Channel]] 的初始化（连接单点 vs 命名服务集群）、[[concepts/命名服务|命名服务]]（BNS、file、list、consul、nacos 等）、[[concepts/负载均衡|负载均衡]]算法（rr、wrr、random、wr、la、一致性哈希）、三种调用模式（[[concepts/同步访问|同步]]/[[concepts/异步访问|异步]]/[[concepts/半同步|半同步]]）以及超时、重试、backup request、熔断、SSL、压缩等高级特性展开，并详细介绍了 [[concepts/协议|协议]]选择（baidu_std、http、h2、grpc、thrift 等）和 [[concepts/连接方式|连接方式]]（短连接/连接池/单连接）的配置方法。

## 关键实体
- [[entities/brpc|brpc]]：Apache 基金会开源 RPC 框架
- [[entities/brpcchannel|brpc::Channel]]：代表与服务器交互通道的核心类
- [[entities/brpccontroller|brpc::Controller]]：控制单次 RPC 行为的类
- [[entities/brpcchanneloptions|brpc::ChannelOptions]]：Channel 初始化配置结构体
- [[entities/consul|Consul]]：HashiCorp 的服务发现工具
- [[entities/nacos|Nacos]]：阿里巴巴的服务发现平台
- [[entities/gflags|gflags]]：Google 命令行参数解析库

## 关键概念
- [[concepts/命名服务|命名服务]]：将服务名映射为机器列表的机制
- [[concepts/负载均衡|负载均衡]]：在多台服务器间分割流量的机制
- [[concepts/一致性哈希|一致性哈希]]：c_murmurhash/c_md5 算法
- [[concepts/wrr|wrr]]：加权轮询负载均衡
- [[concepts/la|la]]：locality-aware 负载均衡
- [[concepts/备份请求|backup request]]：降低长尾延迟的机制
- [[concepts/重试退避|重试退避]]：重试前等待的策略
- [[concepts/熔断|熔断]]：保护下游服务的机制
- [[concepts/健康检查|健康检查]]：检测 server 恢复的机制
- [[concepts/异步访问|异步访问]]、[[concepts/同步访问|同步访问]]、[[concepts/半同步|半同步]]：三种调用模式
- [[concepts/协议|协议]]：Channel 与 server 通信的格式约定
- [[concepts/压缩|压缩]]：Snappy/Gzip/Zlib 压缩算法
- [[concepts/连接方式|连接方式]]：短连接/连接池/单连接
- [[concepts/客户端认证|客户端认证]]：基于请求/连接的认证
- [[concepts/幂等性|幂等性]]：重试机制的关键考虑
- [[concepts/命名服务过滤器|命名服务过滤器]]：筛选 server 列表的机制
- [[concepts/BNS|BNS]]：百度命名服务
- [[concepts/bthread|bthread]]：brpc 底层线程库
- [[concepts/SSL|SSL]]：加密通信安全协议
- [[concepts/附件|附件]]：用户自定义数据传递机制
- [[concepts/log_id|log_id]]：分布式调用链追踪 ID
- [[concepts/集群恢复限流|集群恢复限流]]：宕机恢复时的客户端限流
- [[concepts/correlation_id|correlation_id]]：RPC 唯一关联标识
- [[concepts/命名服务降级|命名服务降级]]：Consul 不可用时的容错
- [[concepts/long-polling|long polling]]：Consul 使用的网络通信方式
- [[concepts/SocketMap|SocketMap]]：进程级 Socket 映射
- [[concepts/baidu_std|baidu_std]]：百度标准协议
- [[concepts/Streaming-RPC|Streaming RPC]]：流式 RPC
- [[concepts/ParallelChannel|ParallelChannel]]：并发组合 channel
- [[concepts/brpcjoin|brpc::Join]]：等待 RPC 完成的函数
- [[concepts/brpcstartcancel|brpc::StartCancel]]：取消 RPC 的函数
- [[concepts/brpcnewcallback|brpc::NewCallback]]：生成回调对象的工厂函数
- [[concepts/brpcdonothing|brpc::DoNothing]]：空操作 done
- [[concepts/VIP|VIP]]：4 层负载均衡器的公网 IP

## 要点
- **Channel 替代 Client**：`brpc` 中没有 `brpc::Client` 类，使用 [[entities/brpcchannel|brpc::Channel]] 代表客户端，可被所有线程共享使用（`CallMethod` 线程安全），但 `Init()` 和析构不是线程安全的
- **两种初始化方式**：连接单台服务器（`ip:port`）或连接服务集群（命名服务 URL + 负载均衡算法名称）
- **三种调用模式**：同步访问（`CallMethod` 阻塞等待）、异步访问（通过 `done` 回调）、半同步访问（`brpc::Join` + `brpc::DoNothing`）
- **命名服务与负载均衡**：内置 BNS、file、list、consul、nacos 等多种命名服务；支持 rr、wrr、random、wr、la、c_murmurhash/c_md5 等负载均衡算法
- **高级特性**：支持 backup request（降低长尾延迟）、重试退避（固定/随机间隔）、熔断保护、健康检查、SSL 加密、客户端认证、压缩（Snappy/Gzip/Zlib）
- **多协议支持**：baidu_std、http、h2、grpc、thrift、redis、memcache 等协议，每种协议有默认连接方式（短连接/连接池/单连接）
- **共享线程池**：brpc 没有独立的 Client 线程池，所有 Channel 和 Server 通过 [[concepts/bthread|bthread]] 共享线程池