---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "IO multiplexing"
  - "I/O多路复用"
---

## Related Entities
- [[entities/redis|Redis]]
- [[entities/node-js|Node.js]]
- [[entities/nginx|Nginx]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/brpc|brpc]]

## Mentions in Source
> **Source: [[sources/单线程反应器|单线程反应器]]**
> - "非阻塞 IO：使用 epoll、kqueue 等高效 IO 多路复用机制，支持成千上万个并发连接。"
> - "该模型通过非阻塞 IO 和事件分派机制实现高并发，但受限于单核 CPU 的计算能力。"

> **Source: [[sources/en_io|en_io]]**
> - "Non-blocking IO is often used with IO multiplexing(poll, select, epoll in Linux or kqueue in BSD)."
> - "Since epoll is implemented as a red-black tree, epoll_ctl is not a very fast operation, especially in multi-threaded environments."
> - "Because of a bug of epoll and overhead of epoll_ctl, edge triggered mode is used in EDISP."

> **Source: [[sources/en_io|en_io]]**
> - "No directly relevant information"