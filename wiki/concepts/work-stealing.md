---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "method"
aliases:
  - "工作窃取"
  - "work-stealing"
  - "任务窃取"
  - "bthread work stealing"
  - "工作窃取"
  - "work-stealing"
  - "任务窃取"
---

## Description
bthread work stealing 是 brpc 在 bthread 层面实现的一种调度策略，主要用于解决 bthread 与 pthread 之间的负载分配问题。由于 bthread 是独立运行的执行单元，可以在任意 pthread 上恢复执行，当某个 pthread 上的工作负载较重时，系统可以将其他 pthread 上已经派发的 bthread "偷取"到当前 pthread 上运行，从而避免线程闲置并提升整体吞吐。

在实际 IO 场景中，work stealing 与 [[concepts/edge-triggered|Edge triggered 模式]] 和 [[concepts/non-blocking-io|Non-blocking IO]] 紧密配合：当 [[entities/eventdispatcher|EventDispatcher]]（EDISP）所在的 pthread 收到网络事件并新建 bthread 处理 fd 数据时，EDISP 会主动将所在 pthread 让给新建的 bthread，以获得更好的 cache locality 并尽快读取数据；而 EDISP 自身的 bthread 则会被 work stealing 机制调度到另一个 pthread 上继续执行。这种安排使得事件分发与数据读取可以流水线化运行在不同 CPU 核上，最大化 cache 利用率。结合 [[concepts/wait-free|Wait-free 同步]]（通过原子变量加一机制实现），brpc 在多个请求同时读取同一个 fd 时的竞争得以消除。

## Related Concepts
- [[concepts/edge-triggered|Edge triggered 模式]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/wait-free|Wait-free 同步]]
- [[concepts/work-stealing|Work Stealing 调度]]

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/baidu|baidu]]
- [[entities/bthread|bthread]]
- [[entities/socket|socket]]

## Mentions in Source
> **Source: [[sources/brpc概述|brpc概述]]**
> - "工作窃取（work stealing）主要解决的是调度问题：当把一个bthread调度到一个pthread上运行后，由于bthread是独立运行的，其可以在任意pthread上继续执行。例如，EventDispatcher（EDISP）所在的pthread创建了一个处理网络事件分发和回调的bthread，之后该pthread可能被其他更紧急的任务占用（如对定时器事件的响应）。此时，原本由EDISP启动的bthread就成了一个可以在其他pthread上继续执行的候选任务。这种机制正是bthread中实现的工作窃取。"

> **Source: [[sources/en_io|en_io]]**
> - "The bthread in which EDISP runs will be stolen to another pthread and keep running, this mechanism is work stealing used in bthreads."
> - "These methods make contentions on dispatching events of one fd wait-free."
> - "The pthread worker in which EDISP runs is yielded to the newly created bthread to make it start reading ASAP and have a better cache locality."

> **Source: [[sources/io|io]]**
> - "在背后，EDISP把所在的pthread让给了新建的bthread，使其有更好的cache locality，可以尽快地读取fd上的数据。"
> - "而EDISP所在的bthread会被偷到另外一个pthread继续执行，这个过程即是bthread的work stealing调度。"
> - "这些方法使得brpc读取同一个fd时产生的竞争是wait-free的。"