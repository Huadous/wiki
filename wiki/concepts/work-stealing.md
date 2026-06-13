---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
  - "[[brpc/bthread.md]]"
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

## Related Concepts
- [[concepts/edge-triggered|Edge triggered 模式]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/wait-free|Wait-free 同步]]
- [[concepts/work-stealing|Work Stealing 调度]]
- [[concepts/butex|butex]]
- [[concepts/m-n-threading|M:N threading]]

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/baidu|baidu]]
- [[entities/bthread|bthread]]
- [[entities/socket|socket]]
- [[entities/pthread-worker|pthread worker]]
- [[entities/runqueue|runqueue]]

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

> **Source: [[sources/bthread|bthread]]**
> - "关键技术两点：work stealing调度和butex，前者让bthread更快地被调度到更多的核心上，后者让bthread和pthread可以相互等待和唤醒。"
> - "pthread worker在任何时间只会运行一个bthread，当前bthread挂起时，pthread worker先尝试从本地runqueue弹出一个待运行的bthread，若没有，则随机偷另一个worker的待运行的bthread，仍然没有才睡眠并会在有新的待运行的bthread时被唤醒。"