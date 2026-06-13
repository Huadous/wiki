---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "other"
aliases:
  - "EDISP"
  - "EventDispatcher（EDISP）"
---

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