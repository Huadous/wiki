---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/lalb]]"
tags:
  - "method"
aliases:
  - "UB WeightedStrategy"
  - "加权策略"
  - "权值分流策略"
---

## Related Concepts
- [[concepts/lalb|LALB]] — 被对比的自适应负载均衡算法，通过基础权值和[[concepts/base_weight|base_weight]]计算实现更优的分流均衡
- [[concepts/负载均衡|负载均衡]] — 所属领域
- [[concepts/权值分流|权值分流]] — 核心机制
- [[concepts/base_weight|base_weight]] — LALB中的基础权值计算方式，解决了WeightedStrategy的数学悖论
- [[concepts/weight-tree|weight-tree]] — LALB中用于高效权值查询的数据结构
- [[concepts/doublybuffereddata|doublybuffereddata]] — 权值更新时的线程安全机制
- [[concepts/Locality-aware load balancing|Locality-aware load balancing]] — 相关负载均衡理念

## Related Entities
- [[entities/ub|ub]] — 所属框架，百度内部RPC框架，WeightedStrategy是其内置负载均衡策略
- [[entities/brpc|brpc]] — UB框架与brpc同属百度RPC体系，在[[sources/lalb|lalb]]源文件中提到UB框架和brpc的关联

## Mentions in Source
> **源文件: [[sources/lalb|lalb]]**
> - "框架层面也有过一些努力，比如UB中的WeightedStrategy是根据下游的cpu占用率来进行分流，但明显地它解决不了延时相关的问题，甚至cpu的问题也解决不了。" — [[sources/lalb|lalb]]
> - "因为它被实现为定期reload一个权值列表，可想而知更新频率高不了，等到负载均衡反应过来，一大堆请求可能都超时了。" — [[sources/lalb|lalb]]
> - "这里有个数学问题：怎么把cpu占用率转为权值。" — [[sources/lalb|lalb]]
> - "这些因素使得这类算法的实际效果和那两个基本算法没什么差距，甚至更差，用者甚少。" — [[sources/lalb|lalb]]
> - "UB中的[WeightedStrategy](https://svn.baidu.com/public/trunk/ub/ub_client/ubclient_weightstrategy.h)是根据下游的cpu占用率来进行分流，但明显地它解决不了延时相关的问题，甚至cpu的问题也解决不了：因为它被实现为定期reload一个权值列表，可想而知更新频率高不了，等到负载均衡反应过来，一大堆请求可能都超时了。" — [[sources/lalb|lalb]]
> - "并且这儿有个数学问题：怎么把cpu占用率转为权值。假设下游差异仅仅由同机运行的其他程序导致，机器配置和网络完全相同，两台机器权值之比是cpu idle之比吗？假如是的，当我们以这个比例给两台机器分流之后，它们的cpu idle应该会更接近对吧？而这会导致我们的分流比例也变得接近，从而使两台机器的cpu idle又出现差距。你注意到这个悖论了吗？这些因素使得这类算法的实际效果和那两个基本算法没什么差距，甚至更差，用者甚少。" — [[sources/lalb|lalb]]