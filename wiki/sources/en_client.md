---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/en_client.md]]"
tags: [Channel, Naming Service, BNS, Load Balancer, Consistent Hashing, Circuit Breaker, Retry, Backup Request, Health Checking, Controller, bthread, Connection Type, Timeout, Authentication, Compression, Asynchronous call, Synchronous call, Locality-aware load balancing, Cancel RPC, ChannelOptions, Naming Service Filter, baidu_std, rr, wrr, random, wr, ParallelChannel, SelectiveChannel, brpc::Join, brpc::NewCallback, PROTOCOL_HTTP, PROTOCOL_H2, PROTOCOL_MEMCACHE, PROTOCOL_REDIS, PROTOCOL_NSHEAD, SocketMap, IOBuf, Semi-synchronous call, Attachment, log_id, SSL, Snappy, Streaming RPC, Idempotence, VIP, Deadline, gflags]
aliases: ["brpc Client 文档", "brpc client-side documentation"]
---

# brpc Client 文档（Client-side documentation） - Summary

## 来源
- Original file: [[brpc/en_client.md]]
- Ingested: 2026-06-13

## 核心内容
本文件是 [[entities/brpc|brpc]] 项目的客户端使用文档，系统介绍了客户端核心组件 [[concepts/channel|Channel]] 的工作方式与编程模型。文档明确指出 brpc 并不存在名为 `brpc::Client` 的类，而是使用 Channel 代表到一台服务器或一个服务器集群的通信线路；Channel.CallMethod() 线程安全，可被多线程共享，但 Init() 与销毁不是线程安全的。内容涵盖连接单台服务器与集群的两种 Init() 方式、多种 [[concepts/naming-service|Naming Service]] 后端（bns、file、list、http、consul、nacos）、多种 [[concepts/load-balancer|Load Balancer]] 算法（rr、wrr、random、wr、la、c_murmurhash、c_md5）、集群宕机后的客户端限流恢复机制、同步/异步调用的生命周期管理以及 [[concepts/controller|Controller]] 的用法。高级特性包括 [[concepts/retry|Retry]] 与 [[concepts/backup-request|Backup Request]]、[[concepts/circuit-breaker|Circuit Breaker]]、[[concepts/ssl|SSL]]、[[concepts/authentication|Authentication]]、[[concepts/compression|Compression]] 等，并附有 FAQ 与客户端工作流图。

## 关键实体
- [[entities/brpc|brpc]]：Apache 开源的高性能 RPC 框架，本文档描述其客户端使用方法。
- [[entities/apache|Apache]]：brpc 项目的托管方，源代码仓库位于 apache/brpc。
- [[entities/consul|Consul]]：HashiCorp 的服务发现产品，通过 consul:// URL 作为 brpc 的 NamingService 后端之一。
- [[entities/nacos|Nacos]]：阿里巴巴开源的动态服务发现与配置管理平台，通过 nacos:// URL 被 brpc 支持。
- [[entities/grpc|gRPC]]：Google 的开源 RPC 框架，通过 h2:grpc 协议在 brpc 中得到支持。
- [[entities/apache-thrift|Apache Thrift]]：跨语言 RPC 框架，通过 PROTOCOL_THRIFT 协议在 brpc 中得到支持。
- [[entities/brpcdonothing|brpc::DoNothing]]：brpc 提供的半同步调用专用空操作 closure。

## 关键概念
- [[concepts/channel|Channel]]：brpc 客户端核心抽象，代表到一台服务器或一个集群的通信线路。
- [[concepts/naming-service|Naming Service]]：将名称映射到可变服务器列表的发现机制。
- [[concepts/bns|BNS]]：百度内部最常用的命名服务，使用 bns:// URL。
- [[concepts/load-balancer|Load Balancer]]：负责在多台服务器之间分配请求流量的负载均衡器。
- [[concepts/consistent-hashing|Consistent Hashing]]：c_murmurhash/c_md5 一致性哈希算法，适合缓存服务。
- [[concepts/circuit-breaker|Circuit Breaker]]：当错误率超阈值时剔除后端的客户端保护机制。
- [[concepts/retry|Retry]]：由 ChannelOptions.max_retry 控制的客户端重试机制。
- [[concepts/backup-request|Backup Request]]：超时后向另一台服务器发备份请求的保护机制。
- [[concepts/health-checking|Health Checking]]：对连接断开服务器进行周期性重连探测的机制。
- [[concepts/controller|Controller]]：每次 RPC 的控制对象，覆盖 Channel 级选项。
- [[concepts/bthread|bthread]]：brpc 的 M:N 用户态协程，客户端与 Server 共享后台工作线程。
- [[concepts/connection-type|Connection Type]]：short、pooled、single 三种连接类型。
- [[concepts/timeout|Timeout]]：RPC 的 deadline（默认 1000ms），错误码 ERPCTIMEDOUT 不被重试。
- [[concepts/authentication|Authentication]]：请求级与连接级两种客户端认证方式。
- [[concepts/compression|Compression]]：Snappy、Gzip、Zlib 三种请求体压缩算法。
- [[concepts/asynchronous-call|Asynchronous call]]：非阻塞 RPC 调用方式，callback 运行在独立 bthread。
- [[concepts/synchronous-call|Synchronous call]]：阻塞调用方式，CallMethod 等待响应返回或出错。
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]：la 算法优先选择延迟较低的服务器。
- [[concepts/cancel-rpc|Cancel RPC]]：通过 brpc::StartCancel(call_id) 主动取消 RPC 的机制。
- [[concepts/channeloptions|ChannelOptions]]：Channel 初始化时使用的配置结构体。
- [[concepts/naming-service-filter|Naming Service Filter]]：对 NamingService 返回服务器进行过滤的扩展点。
- [[concepts/baidu_std|baidu_std]]：brpc 默认且最广泛部署的二进制协议。
- [[concepts/rr|rr]]：轮询负载均衡算法。
- [[concepts/wrr|wrr]]：加权轮询负载均衡算法。
- [[concepts/random|random]]：随机负载均衡算法。
- [[concepts/wr|wr]]：加权随机负载均衡算法。
- [[concepts/parallelchannel|ParallelChannel]]：简化多路并行异步 RPC 等待的 Channel 变体。
- [[concepts/selectivechannel|SelectiveChannel]]：允许按调用选择不同后端的 Channel 变体。
- [[concepts/brpcjoin|brpc::Join]]：阻塞等待指定 RPC 完成的同步函数。
- [[concepts/brpcnewcallback|brpc::NewCallback]]：用于生成异步 done 回调的工厂函数。
- [[concepts/protocol_http|PROTOCOL_HTTP]]：brpc 支持的 HTTP/1.0 与 HTTP/1.1 协议。
- [[concepts/protocol_h2|PROTOCOL_H2]]：brpc 支持的 HTTP/2 协议。
- [[concepts/protocol_memcache|PROTOCOL_MEMCACHE]]：brpc 支持的 memcached 二进制协议。
- [[concepts/protocol_redis|PROTOCOL_REDIS]]：brpc 支持的 Redis 1.2+ 协议。
- [[concepts/protocol_nshead|PROTOCOL_NSHEAD]]：brpc 中用于发送 NsheadMessage 的协议。
- [[concepts/socketmap|SocketMap]]：维护到各服务器连接映射的全局数据结构。
- [[concepts/iobuf|IOBuf]]：brpc 提供的链式缓冲区数据结构。
- [[concepts/semi-synchronous-call|Semi-synchronous call]]：配合 brpc::Join 与 brpc::DoNothing 的半同步调用模式。
- [[concepts/attachment|Attachment]]：baidu_std 与 hulu_pbrpc 协议支持的数据透传特性。
- [[concepts/log_id|log_id]]：通过 Controller::set_log_id() 设置的 64 位请求关联标识。
- [[concepts/ssl|SSL]]：通过 ChannelOptions.mutable_ssl_options() 启用的加密传输能力。
- [[concepts/snappy|Snappy]]：以压缩解压速度著称的压缩算法。
- [[concepts/streaming-rpc|Streaming RPC]]：用于传输流式数据的应用层连接特性。
- [[concepts/idempotence|Idempotence]]：设计重试安全性的关键服务属性。
- [[concepts/vip|VIP]]：四层负载均衡器的公网 IP 地址。
- [[concepts/deadline|Deadline]]：RPC 的绝对最大允许时间，到达后不再重试。
- [[concepts/gflags|gflags]]：brpc 用于调优全局行为的 flag 配置机制。

## 要点
- **Channel 而非 Client**：brpc 客户端使用 [[concepts/channel|Channel]] 表示到服务器的连接；Channel.CallMethod() 线程安全，但 Init() 与销毁不是线程安全的。
- **连接单点与集群**：Channel.Init() 支持连接单台服务器（指定 IP:port）或通过 [[concepts/naming-service|Naming Service]] + [[concepts/load-balancer|Load Balancer]] 连接集群。
- **多种 Naming Service**：支持 bns、file、list、http、consul、nacos 等后端，可实现 brpc::NamingService 扩展更多命名服务。
- **多种负载均衡算法**：[[concepts/rr|rr]] / [[concepts/wrr|wrr]] / [[concepts/random|random]] / [[concepts/wr|wr]] / [[concepts/locality-aware-load-balancing|la]] / [[concepts/consistent-hashing|c_murmurhash、c_md5]]；其中 rr 与 random 支持集群宕机后的客户端限流恢复（min_working_instances、hold_seconds）。
- **同步 vs 异步调用**：同步调用可放栈但不能在持 pthread 锁时调用（易死锁）；异步调用必须把 Response、Controller、done 放在堆上并在 done->Run() 中删除，callback 运行在独立 bthread。
- **超时即 deadline**：[[concepts/timeout|timeout_ms]] 是 deadline，错误码 ERPCTIMEDOUT(1008) 不被重试；[[concepts/backup-request|Backup Request]] 在指定时间内未收到响应时向其他服务器发备份请求。
- **连接类型**：[[concepts/connection-type|short / pooled / single]] 三种连接类型有不同延迟与并发特性，由 [[concepts/channeloptions|ChannelOptions.connection_type]] 控制。
- **协议矩阵**：[[concepts/baidu_std|baidu_std]]、[[concepts/protocol_http|http]]、[[concepts/protocol_h2|h2]]（含 h2:grpc）、[[concepts/protocol_redis|redis]]、[[concepts/protocol_memcache|memcache]]、[[concepts/protocol_nshead|nshead]] 等协议均可在 ChannelOptions.protocol 中切换。
- **高级特性**：[concepts/authentication] 支持请求级与连接级两种方式；[[concepts/ssl|SSL]] 通过 ChannelOptions.mutable_ssl_options() 启用；[[concepts/compression|Compression]] 支持 Snappy、Gzip、Zlib。
- **客户端工作流**：创建 bthread_id 关联 → 选服务器 → 选 Socket → 必要时认证 → 按协议序列化 → 设置超时 → 写入 Socket → Join 等待 → 解析响应并触发 done 或重试。