---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/bthread_or_not.md]]"
tags: [bthread, 同步接口, 异步接口, 回调, 组合访问, ParallelChannel, ExecutionQueue, 并行计算, 半同步, qps-latency决策公式, 线程池, 调度延时, 树形并行计算]
aliases: ["bthread or not", "Should I use async interface or bthread?"]
---

# 我应该用异步接口还是bthread？ - Summary

## 来源
- Original file: [[brpc/bthread_or_not.md]]
- Ingested: 2026-06-13

## 核心内容
本文档是 [[entities/brpc|brpc]] 框架的使用指导文档，核心讨论了开发者在面对RPC调用时，应该在 [[concepts/同步接口|同步接口]] 、 [[concepts/异步接口|异步接口]] 和 [[concepts/bthread|bthread]] 之间如何选择。文档以 qps-latency决策公式 作为核心判断依据：当 `qps × latency` 与CPU核数同一数量级时优先使用同步接口；远大于CPU核数时使用异步接口以节省线程资源；只有在需要多核 [[concepts/并行计算|并行计算]] 时才使用bthread。文档还介绍了 [[concepts/半同步|半同步]] 模式、 [[concepts/组合访问|组合访问]] 工具（如 [[concepts/parallelchannel|ParallelChannel]] 和 [[concepts/executionqueue|ExecutionQueue]] ）、bthread的 [[concepts/调度延时|调度延时]] 特性，以及 [[concepts/树形并行计算|树形并行计算]] 的构建方法，并以 [[entities/ubaserver|ubaserver]] 作为反面案例说明多线程独立eventloop模式的问题。

## 关键实体
- [[entities/brpc|brpc]]：百度开源的工业级RPC框架，提供同步接口、异步接口和基于bthread的三种RPC调用方式
- [[entities/ubaserver|ubaserver]]：多线程独立eventloop模式的服务器架构，被文档作为反面案例提及

## 关键概念
- [[concepts/bthread|bthread]]：brpc提供的用户态线程机制，用于多核并行计算（而非简单并发RPC）
- [[concepts/同步接口|同步接口]]：阻塞式RPC调用，延时不高时优先选择
- [[concepts/异步接口|异步接口]]：非阻塞RPC调用，回调运行在不同线程中以获得多核扩展性
- [[concepts/回调|回调]]：异步编程的核心机制，在多线程环境下与单线程JavaScript回调有本质区别
- [[concepts/组合访问|组合访问]]：brpc通过组合channel声明式执行复杂RPC访问的机制
- [[concepts/parallelchannel|ParallelChannel]]：用于并行发起多个RPC并统一等待结果的组合访问工具
- [[concepts/executionqueue|ExecutionQueue]]：基于bthread的线程池替代方案，保证job执行顺序
- [[concepts/并行计算|并行计算]]：bthread的核心适用场景，计算时间超过1ms才有收益
- [[concepts/半同步|半同步]]：发起多个RPC并等待全部完成的混合编程模式
- [[concepts/qps-latency决策公式|qps-latency决策公式]]：判断同步还是异步的经验法则（`qps × latency` vs CPU核数）
- [[concepts/线程池|线程池]]：可用bthread代替的传统并发模式
- [[concepts/调度延时|调度延时]]：bthread创建到执行的延迟（中位数3微秒，99.99%在30微秒内）
- [[concepts/树形并行计算|树形并行计算]]：利用bthread构建树形结构实现多核并行计算的编程模式

## 要点
- **决策优先级**：延时不高时先用简单易懂的同步接口，不行用异步接口，只有需要多核并行计算时才用bthread
- **核心判断公式**：计算 `qps × latency`，与CPU核数同数量级用同步，远大于则用异步
- **bthread定位**：专门用于多核并行计算（如树形并行计算结构），而非简单并发RPC（并发RPC应使用ParallelChannel或异步接口）
- **bthread调度延时**：中位数约3微秒，计算时间超过1ms时使用bthread收益才明显
- **半同步模式**：发起多个异步RPC后用ParallelChannel等待，比启动多个bthread执行同步RPC效率更高
- **brpc异步特性**：回调运行在不同线程中，获得多核扩展性，但需注意多线程问题
- **反面案例**：ubaserver采用多线程独立eventloop模式，因阻塞改回调困难，实际效果糟糕
- **编程技巧**：构建树形并行计算时让原地运行的部分最慢，可吸收bthread的调度延时