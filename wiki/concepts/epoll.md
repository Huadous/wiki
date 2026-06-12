---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_io]]"
tags:
  - "term"
aliases:
  - "epoll系统调用"
  - "Linux epoll"
  - "Non-blocking IO"
  - "epoll系统调用"
  - "Linux epoll"
---

## Related Entities
- [[entities/redis|redis]]
- [[entities/nginx|nginx]]
- [[entities/node-js|node-js]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/brpc|brpc]]
- [[entities/socket|socket]]
- [[entities/socketid|socketid]]

## Description
epoll是Linux下的IO多路复用机制，使用红黑树实现，支持[[concepts/边缘触发|边缘触发]]和[[concepts/水平触发|水平触发]]模式。由于epoll基于红黑树实现，[[concepts/epoll_ctl|epoll_ctl]]操作在多线程环境下开销较大。在高并发场景下，epoll性能优于select和poll。

## Usage Notes
brpc使用epoll的[[concepts/边缘触发|边缘触发]]模式，因为当时（brpc开发时期）epoll存在bug且epoll_ctl开销高。[[entities/eventdispatcher|EventDispatcher]]依赖epoll接收事件。