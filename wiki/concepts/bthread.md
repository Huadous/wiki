---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_server]]"
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/io.md]]"
  - "[[brpc/en_streaming_log.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bvar.md]]"
  - "[[brpc/bthread_or_not.md]]"
  - "[[brpc/bthread.md]]"
  - "[[brpc/avalanche.md]]"
tags:
  - "other"
aliases:
  - "brpc 协程"
  - "bthread 线程"
  - "num_threads"
  - "brpc 协程"
  - "bthread 线程"
  - "pthread"
  - "brpc 协程"
  - "bthread 线程"
  - "num_threads"
  - "brpc 协程"
  - "bthread 线程"
---

## Description
bthread 是 brpc 使用的 M:N 线程库，目的在于在提高程序并发度的同时降低编码难度，并在核数日益增多的 CPU 上提供更好的 scalability 和 cache locality。M 个用户级 bthread 被映射至 N 个 pthread（worker）之上，一般 M 远大于 N。由于 Linux 当下的 pthread 实现（NPTL）是 1:1 的，M 个 bthread 实际上相当于映射至 N 个 LWP。bthread 的前身是百度 Distributed Process（DP）中的 fiber，一个 N:1 的合作式（cooperative）线程库，等价于 event-loop 库，但允许用户以同步代码的形式编写。bthread 是一个真正的 M:N 库——一个 bthread 因系统调用等原因被卡住不会影响其他 bthread 的执行，这一性质与早期 N:1 协程有本质区别。bthread 在数百纳秒内即可建立完成，并提供多种同步原语（如 butex、bthread_mutex_t 等）支持高效同步。

bthread 设计中的一个重要目标是与 pthread 的互操作性：bthread 所有接口可在 pthread 中被调用并有合理的行为，使用 bthread 的代码可以在 pthread 中正常执行；bthread API 在 bthread 中被调用时影响的是当前 bthread，在 pthread 中被调用时影响的是当前 pthread。但 bthread 与 pthread 仍存在关键差异——bthread 阻塞可能切换系统线程，依赖系统 TLS 的函数的行为未定义；当 bthread 因 pthread API 阻塞时，当前 pthread worker 上待运行的 bthread 会被其他空闲的 pthread worker 偷过去运行。pthread 相比 N:1 协程的优势在于能利用多核，缺点则是线程数过多会稀释 thread-local cache 资源（如 tcmalloc 的性能下降）。

从工程实践角度看，当程序延时要求不高时应优先使用简单易懂的同步接口；当同步接口无法满足时使用异步接口；只有当需要多核并行计算时才应使用 bthread。如果仅仅是为了并发 RPC，不需要引入 bthread。bthread 从建立到执行存在调度延时，在不是很忙的机器上其中位数约为 3 微秒，90% 在 10 微秒内，99.99% 在 30 微秒内。

在与传统固定线程池（硬限线程数）设计的对比中，bthread 的一个关键特性是其线程个数为软限（soft limit）：brpc server 端默认在 bthread 中处理请求，单个请求超时只会阻塞所在的 bthread，并不会阻止为新请求建立新的 bthread；而拥塞时传统 A 服务最大 QPS 出现的跳变正是因为其线程个数是硬限，单个请求的处理时间很大程度上决定了最大 QPS。这使得 bthread 模型在拥塞场景下能够避免因超时阻塞线程而导致最大 QPS 骤降的问题，保持较高的服务并发度，是 brpc 抗雪崩（avalanche）方面的核心优势。

## Related Concepts
- [[concepts/work-stealing|工作窃取（work stealing）]]
- [[concepts/bthread-work-stealing|bthread work stealing]]
- [[concepts/noflush|noflush]]
- [[concepts/thread-local-bufferr|thread-local 缓冲]]
- [[concepts/brpc-server|brpc::Server]]
- [[concepts/pthread模式|pthread模式]]
- [[concepts/bthread-local|bthread-local]]
- [[concepts/session-local-data|session-local data]]
- [[concepts/server-thread-local-data|server-thread-local data]]
- [[concepts/resourcepool|ResourcePool<t>]]
- [[concepts/taskmeta|TaskMeta]]
- [[concepts/bthread_t|bthread_t]]
- [[concepts/bthread-栈管理|bthread 栈管理]]
- [[concepts/guard-page|guard page]]
- [[concepts/edge-triggered-模式|Edge triggered 模式]]
- [[concepts/socketuniqueptr|SocketUniquePtr]]
- [[concepts/命名服务|命名服务]]
- [[concepts/健康检查|健康检查]]
- [[concepts/periodicservicervice|PeriodicNamingService]]
- [[concepts/bthread_mutex_t|bthread_mutex_t]]
- [[concepts/bthread_concurrency|bthread_concurrency]]
- [[concepts/channel|Channel]]
- [[concepts/timeout|Timeout]]
- [[concepts/异步访问|异步访问]]
- [[concepts/同步访问|同步访问]]
- [[concepts/半同步|半同步]]
- [[concepts/vars|/vars]]
- [[concepts/dump功能|dump功能]]
- [[concepts/executionqueue|ExecutionQueue]]
- [[concepts/parallelchannel|ParallelChannel]]
- [[concepts/并行计算|并行计算]]
- [[concepts/同步接口|同步接口]]
- [[concepts/异步接口|异步接口]]
- [[concepts/m-n-threading|M:N threading]]
- [[concepts/butex|butex]]
- [[concepts/coroutine|协程（coroutine）]]
- [[concepts/fiber|fiber]]
- [[concepts/cooperative-threading|合作式线程（cooperative threading）]]
- [[concepts/event-loop|event-loop]]
- [[concepts/scalability|scalability]]
- [[concepts/cache-locality|cache locality]]
- [[concepts/nptl|NPTL]]
- [[concepts/lwp|LWP]]
- [[concepts/线程局部存储|线程局部存储（Thread Local Storage, TLS）]]
- [[concepts/tcmalloc|tcmalloc]]
- [[concepts/avalanche|avalanche（雪崩防护）]]
- [[concepts/拥塞|拥塞]]
- [[concepts/qps|QPS]]
- [[concepts/线程池|线程池]]
- [[concepts/超时|超时]]
- [[concepts/软限|软限（soft limit）]]
- [[concepts/硬限|硬限（hard limit）]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/EventDispatcher|EventDispatcher]]
- [[entities/InputMessenger|InputMessenger]]
- [[entities/Socket|Socket]]
- [[entities/bvar|bvar]]
- [[entities/ClosureGuard|ClosureGuard]]
- [[entities/ServerOptions|ServerOptions]]
- [[entities/baidu|baidu]]
- [[entities/eventdispatcher|eventdispatcher]]
- [[entities/inputmessenger|inputmessenger]]
- [[entities/socket|socket]]
- [[entities/bthread|bthread]]
- [[entities/ub|ub]]
- [[entities/namingservicethread|namingservicethread]]
- [[entities/namingservicewatcher|namingservicewatcher]]
- [[entities/brpc::Channel|brpc::Channel]]
- [[entities/Distributed-Process|Distributed Process（DP）]]
- [[entities/pthread-worker|pthread worker]]
- [[entities/glibc|glibc]]

## Mentions in Source
> **Source: [[sources/bvar|bvar]]**
> - "还有像brpc内部的各类计数器："
> - "bthread_switch_second : 20422"
> - "bthread_timer_scheduled_second : 4"
> - "bthread_worker_count : 13"
> - "bthread_worker_usage : 1.33733"

> **Source: [[sources/bthread_or_not|bthread_or_not]]**
> - "短回答：延时不高时你应该先用简单易懂的同步接口，不行的话用异步接口，只有在需要多核并行计算时才用bthread。"
> - "如果仅仅是为了并发RPC，别用bthread。"
> - "bthread从建立到执行是有延时的（调度延时），在不是很忙的机器上，这个延时的中位数在3微秒左右，90%在10微秒内，99.99%在30微秒内。"

> **Source: [[sources/bthread|bthread]]**
> - "bthread是brpc使用的M:N线程库，目的是在提高程序的并发度的同时，降低编码难度，并在核数日益增多的CPU上提供更好的scalability和cache locality。"
> - "bthread的前身是Distributed Process(DP)中的fiber，一个N:1的合作式线程库，等价于event-loop库，但写的是同步代码。"
> - "bthread是一个M:N线程库，一个bthread被卡住不会影响其他bthread。"
> - "由于linux当下的pthread实现(NPTL)是1:1的，M个bthread也相当于映射至N个LWP。"
> - "bthread所有接口可在pthread中被调用并有合理的行为，使用bthread的代码可以在pthread中正常执行。"
> - "bthread API在bthread中被调用时影响的是当前bthread，在pthread中被调用时影响的是当前pthread。使用bthread API的代码可以直接运行在pthread中。"
> - "bthread阻塞可能切换系统线程，依赖系统TLS的函数的行为未定义。"

> **Source: [[sources/avalanche|avalanche]]**
> - "而brpc server端默认在bthread中处理请求，个数是软限，单个请求超时只是阻塞所在的bthread，并不会影响为新请求建立新的bthread。"
> - "拥塞时A服务最大qps的跳变是因为线程个数是硬限，单个请求的处理时间很大程度上决定了最大qps。"