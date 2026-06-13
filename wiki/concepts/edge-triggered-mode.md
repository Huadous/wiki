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
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge Triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge Triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge triggered 模式"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge Triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
  - "Edge Triggered"
  - "边缘触发"
  - "ET"
  - "Edge Triggered Mode"
---

## Description
Edge triggered（边沿触发）是 epoll 提供的两种事件触发模式之一，与 level triggered（水平触发）相对。在水平触发模式下，只要文件描述符处于就绪状态，epoll 就会持续通知；而在边沿触发模式下，事件仅在状态发生变化的瞬间通知一次，应用程序必须一次性处理完所有数据，否则将丢失事件。brpc 的 EventDispatcher (EDISP) 选择采用边沿触发模式，主要原因有二：一是当时 epoll 仍存在一个已知 bug，二是 epoll_ctl 因底层红黑树实现而具有较大的开销，边沿触发能够有效减少事件重复通知带来的额外开销。

在 EDISP 的具体实现中，每当接收到一个事件时，系统会给该 fd 关联的一个原子变量加 1；只有当加 1 前的值为 0 时，才会启动一个新的 bthread 来处理该 fd 上的数据。这种机制配合其他优化手段，使得 brpc 在读取同一个 fd 时产生的竞争是 wait-free 的，避免了锁竞争带来的性能损耗。该方案与 brpc 的整体 IO 模型以及 bthread 的工作窃取调度机制紧密相关，共同支撑了 brpc 高并发的网络处理能力。

## Related Concepts
- [[concepts/epoll|epoll]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/bthread-work-stealing|bthread work stealing]]
- [[concepts/wait-free|wait-free]]
- [[concepts/edge-triggered|edge triggered]]

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|bthread]]

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "Because of a bug of epoll (at the time of developing brpc) and overhead of epoll_ctl, edge triggered mode is used in EDISP."
> - "After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd."

> **Source: [[sources/io|io]]**
> - "由于epoll的一个bug(开发brpc时仍有)及epoll_ctl较大的开销，EDISP使用Edge triggered模式。"
> - "当收到事件时，EDISP给一个原子变量加1，只有当加1前的值是0时启动一个bthread处理对应fd上的数据。"
> - "这些方法使得brpc读取同一个fd时产生的竞争是wait-free的。"