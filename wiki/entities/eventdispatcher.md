---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "other"
aliases:
  - "EDISP"
  - "EventDispatcher（EDISP）"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/inputmessenger|InputMessenger]]

## Related Concepts
- [[concepts/epoll|epoll]]
- [[concepts/bthread|bthread]]
- [[concepts/work-stealing|work stealing]]
- [[concepts/wait-free|wait-free]]
- [[concepts/edge-triggered|edge-triggered]]
- [[concepts/non-blocking-io|Non-blocking IO]]

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "brpc uses one or several EventDispatcher (referred to as EDISP) to wait for events from file descriptors."
> - "Unlike the common 'IO threads', EDISP is not responsible for reading or writing."
> - "After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd."

> **Source: [[sources/io|io]]**
> - "brpc使用一个或多个EventDispatcher(简称为EDISP)等待任一fd发生事件。"
> - "和常见的"IO线程"不同，EDISP不负责读取。"
> - "由于epoll的一个bug(开发brpc时仍有)及epoll_ctl较大的开销，EDISP使用Edge triggered模式。"
> - "No directly relevant information"