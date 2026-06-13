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
  - "[[brpc/avalanche.md]]"
  - "[[brpc/auto_concurrency_limiter.md]]"
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
- [[sources/load_balancing|brpc 负载均衡]]
- [[sources/consistent_hashing|brpc 一致性哈希]]
- [[sources/client|brpc::Channel 客户端]]
- [[sources/bvar_c++|bvar 单维度使用文档]]
- [[sources/bvar|bvar 介绍]]
- [[sources/bthread_or_not|bthread or not]]
- [[sources/bthread|bthread M:N 线程库]]
- [[sources/avalanche|brpc 雪崩防护]]
- [[sources/auto_concurrency_limiter|brpc 自适应限流]]

## Related Concepts
- [[concepts/hash-ring|hash ring]]
- [[concepts/consistent-hashing|一致性哈希]]
- [[concepts/load-balancing|负载均衡]]
- [[concepts/murmurhash3|murmurhash3]]
- [[concepts/md5|md5]]
- [[concepts/channel|brpc::Channel]]
- [[concepts/bvar|bvar 监控]]
- [[concepts/bthread|bthread 线程模型]]
- [[concepts/auto-concurrency-limiter|自适应限流]]
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/littles-law|Little's Law]]

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

> **Source: [[sources/avalanche|avalanche]]**
> - "了解这些因素后可以更好的理解brpc中相关的设计。"（说明 avalanche 文档讨论的雪崩防护设计同样适用于一致性哈希等 brpc 内置能力所处的 brpc 整体运行环境。）
> - "brpc也提供了完整的异步接口，让用户可以进一步提高io-bound服务的并发度，降低服务被打满的可能性。"（说明 brpc 提供的完整异步接口可提高 io-bound 服务的并发度、降低被打满的可能性，是一致性哈希客户端异步调用在雪崩防护语境下的设计动机。）
> - "brpc server端的max_concurrency选项控制了server的最大并发：当同时处理的请求数超过max_concurrency时，server会回复client错误，而不是继续积压。"（说明 brpc server 端通过 `max_concurrency` 在并发超限时直接回复 client 错误而非积压请求，从源头控制积压量；一致性哈希 server 端因此可在雪崩场景下避免请求无限堆积。）

> **Source: [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]**
> - "目前只有method级别支持自适应限流。如果要为某个method开启自适应限流，只需要将它的最大并发设置为\"auto\"即可。"
> - "对应的方法就是设置最大并发，链接指向 brpc 的 server.md 文档。"