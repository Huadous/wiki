---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "工作窃取"
  - "work-stealing"
  - "任务窃取"
---

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