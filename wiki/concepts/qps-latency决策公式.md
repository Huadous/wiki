---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread_or_not|bthread_or_not]]"]
tags: [method]
aliases:
  - "qps * latency vs cpu cores"
  - "qps-latency 同步异步决策公式"
---


# qps-latency决策公式

## 定义
qps-latency决策公式是 brpc 文档中提出的一条经验法则，用于判断一个服务接口应当使用同步还是异步实现。该公式将每秒请求数（qps）与平均延迟（latency，单位为秒）相乘，得到的结果代表系统同时在进行的平均请求数；将该结果与机器的 CPU 核数进行数量级比较：若在同一数量级则推荐使用同步接口，否则推荐使用异步接口。

## 关键特征
- 核心计算方式：`qps × latency（单位：秒）`。
- 物理意义：表示同一时刻系统中平均并发处理的请求数量，可与线程数、CPU 核数进行对比。
- 决策依据：以结果与 CPU 核数是否处于同一数量级为分界点。
- 资源视角：当结果远大于 CPU 核数时，多数操作并不消耗 CPU，而是让大量线程处于阻塞等待状态，此时使用异步可显著节省线程资源（尤其是每个线程栈占用的内存）。
- 代码可读性视角：当结果小于或与 CPU 核数相当时，异步节省的线程资源有限，此时同步代码更简单、更易理解，应优先采用。
- 属于经验法则（rule of thumb），并非严格的数学证明，而是在工程实践中总结出的快速判断方法。

## 应用
- 在 brpc 等高并发 RPC 框架中，决定业务接口是采用同步调用方式还是基于 bthread/异步回调方式实现。
- 在系统设计初期，估算接口的并发压力，辅助架构师进行技术选型。
- 典型示例 1：qps = 2000，latency = 10ms，计算结果 = 2000 × 0.01s = 20，与常见的 32 核 CPU 处于同一数量级，应使用同步接口。
- 典型示例 2：qps = 100，latency = 5s，计算结果 = 100 × 5s = 500，远超常见 CPU 核数，应使用异步接口。
- 适用于 IO 密集型或包含外部依赖（数据库、缓存、下游 RPC）等待时间较长的服务场景。

## 相关概念
- [[concepts/同步接口|同步接口]]
- [[concepts/异步接口|异步接口]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "判断使用同步或异步：计算qps * latency(in seconds)，如果和cpu核数是同一数量级，就用同步，否则用异步。" — [[sources/bthread_or_not|bthread_or_not]]
- "qps = 2000，latency = 10ms，计算结果 = 2000 * 0.01s = 20。和常见的32核在同一个数量级，用同步。" — [[sources/bthread_or_not|bthread_or_not]]
- "qps = 100, latency = 5s, 计算结果 = 100 * 5s = 500。和核数不在同一个数量级，用异步。" — [[sources/bthread_or_not|bthread_or_not]]