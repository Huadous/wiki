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
  - "[[brpc/bvar.md]]"
  - "[[brpc/bthread_or_not.md]]"
  - "[[brpc/bthread.md]]"
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
- [[entities/Apache|Apache]] — brpc 所属的开源软件基金会，一致性哈希功能作为 brpc 内置能力随 Apache brpc 发布，bvar 源码同样托管于 Apache 名下的 `apache/brpc` 仓库
- [[entities/butil|butil]] — brpc 基础库，一致性哈希所依赖的底层数据结构与并发原语由其提供
- [[entities/bvar|bvar]] — brpc 内置计数器类库，源码位于 brpc 源代码树 `src/bvar` 目录下（对应 GitHub `apache/brpc/tree/master/src/bvar/`），为一致性哈希运行指标提供观测能力
- [[entities/mbvar|mbvar]] — bvar 的多维度扩展，与单维度 bvar 共同构成 brpc 监控统计体系，间接支撑一致性哈希的可观测性
- [[entities/Prometheus|Prometheus]] — brpc 通过 `/brpc_metrics` 端点集成的外部监控系统，可消费一致性哈希等 bvar 暴露的运行指标
- [[entities/ubaserver|ubaserver]] — bthread_or_not 文档中作为示例出现的服务器端示例，常被用于演示一致性哈希客户端的同步/异步/bthread 调用方式
- [[entities/bthread|bthread]] — brpc 使用的 M:N 线程库，在 server 端与 client 端都为一致性哈希调用提供并发处理能力，可通过 `ServerOptions.num_threads`（server）或 `-bthread_concurrency`（server/client）调整 worker 数

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
- [[concepts/bthread|bthread]] — brpc 用户态 M:N 线程库，是 server 端与 client 端并发处理的基础；除非确需在一次 RPC 中并发执行代码，否则不直接调用 bthread 函数，留给 brpc 处理
- [[concepts/pthread_worker|pthread worker]] — bthread 的底层执行载体，brpc server 端与 client 端可通过 `ServerOptions.num_threads`（server）或 `-bthread_concurrency`（server/client）调整其数量
- [[concepts/bthread_concurrency|bthread concurrency]] — 通过 `-bthread_concurrency` gflag 控制的 bthread worker 并发度配置项，server/client 端通用
- [[concepts/同步接口|同步接口]] — 一致性哈希客户端的调用方式之一，延时不长、qps 不高时优先选用
- [[concepts/异步接口|异步接口]] — 一致性哈希客户端的调用方式之一，回调会运行在与调用处不同的线程中
- [[concepts/组合访问|组合访问]] — 借助 ComboChannel / ParallelChannel 在一致性哈希客户端侧组合多次 RPC 调用
- [[concepts/ParallelChannel|ParallelChannel]] — 组合访问工具之一，可在一致性哈希客户端侧实现多路并行调用
- [[concepts/ExecutionQueue|ExecutionQueue]] — brpc 提供的异步编程简化工具，可与一致性哈希的异步调用配合使用
- [[concepts/半同步|半同步]] — 一致性哈希客户端侧在同步与异步之间的折中调用模式
- [[concepts/回调|回调]] — 一致性哈希异步客户端依赖的核心机制，回调可能运行在与调用处不同的线程中

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
> - "单维度bvar使用文档，多维度mbvar请移步(mbvar_c++.md)。"（说明 brpc 提供了单维度 bvar 与多维度 mbvar 两套体系，与一致性哈希可观测性共同构成 brpc 监控统计能力。）
> - "前者在brpc中通过/vars服务提供"（说明 bvar 变量通过 brpc 的 `/vars` HTTP 服务对外暴露，一致性哈希的运行指标可经此查询。）
> - "在brpc中也可通过/flags服务在启动后动态修改。"（说明 brpc 内置了 gflags 的动态修改能力，一致性哈希相关 gflags 借助此机制可在运行时调整。）

> **Source: [[sources/bvar|bvar]]**
> - "brpc集成了bvar，/vars可查看所有曝光的bvar，/vars/VARNAME可查阅某个bvar，在brpc中的使用方法请查看vars"（说明 brpc 集成了 bvar，一致性哈希等 brpc 内置能力的运行指标可通过 `/vars` 与 `/vars/VARNAME` HTTP 接口查阅。）
> - "brpc大量使用了bvar提供统计数值，当你需要在多线程环境中计数并展现时，应该第一时间想到bvar"（说明 brpc 大量使用 bvar 提供统计数值，一致性哈希属于此类被 bvar 监控的内置能力之一。）
> - "还有像brpc内部的各类计数器"（说明 bvar 在 brpc 内部还覆盖了 bthread 调度器、iobuf、bvar collector 等多种计数器，一致性哈希可观测性是该统计体系的一部分。）
> - "bvar是多线程环境下的计数器类库，链接指向https://github.com/apache/brpc/tree/master/src/bvar/"（说明 bvar 位于 brpc 源代码树 `src/bvar` 目录下，由 Apache 软件基金会管理的 `apache/brpc` 仓库托管。）

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "brpc提供了异步接口，所以一个常见的问题是：我应该用异步接口还是bthread？"（说明一致性哈希客户端可选择异步接口或基于 bthread 的并行调用方式之一。）
> - "brpc中的异步和单线程的异步是完全不同的，异步回调会运行在与调用处不同的线程中，你会获得多核扩展性"（说明一致性哈希的异步调用回调会运行在与调用处不同的线程中，从而获得多核扩展性。）
> - "当然，延时不长，qps不高时，我们更建议使用同步接口，这也是创建bthread的动机：维持同步代码也能提升交互性能。"（说明在延时不长、qps 不高时，一致性哈希客户端更建议使用同步接口，bthread 旨在维持同步代码风格的同时提升交互性能。）

> **Source: [[sources/bthread|bthread]]**
> - "bthread是brpc使用的M:N线程库"（说明 bthread 是 brpc 使用的 M:N 线程库，为一致性哈希 server/client 调用提供并发基础。）
> - "在brpc中用户可以选择调大worker数来缓解问题, 在server端可设置ServerOptions.num_threads或-bthread_concurrency, 在client端可设置-bthread_concurrency。"（说明通过 `ServerOptions.num_threads`（server）或 `-bthread_concurrency`（server/client）可调大 bthread worker 数，缓解一致性哈希等负载均衡场景下的并发压力。）
> - "你不应该直接调用bthread函数，把这些留给brpc做更好。"（说明 brpc 建议除非确需在一次 RPC 中并发运行代码，否则不直接调用 bthread 函数，一致性哈希客户端应优先沿用 brpc 提供的同步/异步接口与 bthread 集成方式。）