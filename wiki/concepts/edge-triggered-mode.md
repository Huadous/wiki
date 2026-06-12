---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
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
---

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|bthread]]

## Mentions in Source
> **Source: [[sources/en_io]]**
> - "Because of a bug of epoll (at the time of developing brpc) and overhead of epoll_ctl, edge triggered mode is used in EDISP."
> - "After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd."

## Additional Notes
No additional relevant information found in recent source updates.