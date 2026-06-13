---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/avalanche.md]]"
tags: [雪崩, QPS, 拥塞, 重试, backup request, bthread, max_concurrency, Little's Law, RPC超时, 线程池, Channel, RetryPolicy, deadline, 流量放大, 追排问题]
aliases: ["brpc雪崩防护", "avalanche protection in brpc"]
---

# brpc中的雪崩现象与防护 - Summary

## 来源
- Original file: [[brpc/avalanche.md]]
- Ingested: 2026-06-13

## 核心内容
本文深入剖析了分布式服务集群中的[[concepts/雪崩|雪崩]]现象——即绝大部分请求超时、流量下降后仍无法恢复的状态。单服务被打满时通常可恢复，但链式调用中上游服务因client线程等待下游超时而被阻塞，使最大[[concepts/qps|QPS]]从"线程数/平均延时"降为"线程数/超时"，骤降3-4倍，引发更激烈的[[concepts/拥塞|拥塞]]。雪崩不可恢复的两个关键例外是：基于超时的频繁重试导致[[concepts/流量放大|流量放大]]陷入恶性循环，以及无长度限制的缓冲/队列因[[concepts/追排问题|追排问题]]导致排空时间极长。文章系统介绍了[[entities/brpc|brpc]]的雪崩防护设计：[[concepts/bthread|bthread]]软限线程、仅在连接出错时[[concepts/重试|重试]]、[[concepts/backup-request|backup request]]机制以及server端[[concepts/max_concurrency|max_concurrency]]选项，并给出基于[[concepts/littles-law|Little's Law]]估算最大并发、审慎使用[[concepts/retrypolicy|RetryPolicy]]等关键实践建议。

## 关键实体
- [[entities/brpc|brpc]]：百度开发的高性能开源RPC框架，本文讨论的雪崩防护设计主体

## 关键概念
- [[concepts/雪崩|雪崩]]：访问服务集群时绝大部分请求超时且流量减少后无法恢复的现象
- [[concepts/qps|QPS]]：每秒查询数，衡量服务处理能力的关键指标
- [[concepts/拥塞|拥塞]]：服务因请求量超出处理能力而产生的过载状态
- [[concepts/重试|重试]]：客户端在请求失败后再次发起请求的机制，雪崩场景中的关键风险放大因子
- [[concepts/backup-request|backup request]]：brpc提供的特殊重试机制，最多一次额外请求，放大程度最低
- [[concepts/bthread|bthread]]：brpc中使用的软限线程模型，单个请求超时不影响新请求建立
- [[concepts/max_concurrency|max_concurrency]]：brpc server端控制最大并发的配置选项
- [[concepts/littles-law|Little's Law]]：利特尔法则，L = λ × W，用于指导max_concurrency设置
- [[concepts/rpc超时|rpc超时]]：RPC调用中请求等待响应的最长时间限制
- [[concepts/线程池|线程池]]：服务处理请求所使用的线程集合，固定个数时易引发雪崩
- [[concepts/channel|channel]]：brpc客户端访问服务端连接的抽象
- [[concepts/retrypolicy|RetryPolicy]]：brpc中决定重试行为的可定制策略接口
- [[concepts/deadline|deadline]]：brpc中RPC超时的实现方式，绝对截止时间语义
- [[concepts/流量放大|流量放大]]：重试机制导致实际打到下游的请求量超过原始请求量的现象
- [[concepts/追排问题|追排问题]]：拥塞恢复阶段积压请求排空时间取决于"积压请求数/(最大QPS-当前QPS)"

## 要点
- **雪崩本质**：单服务被打满通常可恢复，但链式调用在两个条件下不可恢复——基于超时的频繁重试造成流量恶性放大、无长度限制的缓冲或队列导致恢复时间过长
- **链式调用QPS跳变机制**：当client线程因等待下游超时而阻塞时，服务最大QPS从"线程数/平均延时"降为"线程数/超时"，通常下降3-4倍
- **重试恶性循环条件**：基于超时的频繁重试使上游QPS降为"线程数/超时"的同时让下游QPS翻"重试次数"倍，条件为"线程数/超时×重试次数 > 下游最大QPS"
- **brpc的四层雪崩防护**：[[concepts/bthread|bthread]]软限线程避免超时阻塞影响新请求、默认仅在连接出错时[[concepts/重试|重试]]避免流量放大、[[concepts/backup-request|backup request]]将超时重试放大次数限制为最多1次、[[concepts/max_concurrency|max_concurrency]]在源头控制积压请求数
- **max_concurrency设置建议**：通过"最大QPS × 非拥塞时的延时（秒）"根据[[concepts/littles-law|Little's Law]]评估最大并发，max_concurrency等于或略大于该值即可
- **RetryPolicy定制风险**：用户自实现重试时需仔细评估最差情况下的请求放大倍数，特别是通过多[[concepts/channel|Channel]]切换的场景
- **队列追赶问题**：排空时间 = 积压请求数/(最大QPS-当前QPS)，当两者接近时排空时间可能极长，因此必须限制队列长度