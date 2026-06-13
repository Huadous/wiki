---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "term"
aliases:
  - "epoll系统调用"
  - "Linux epoll"
  - "Non-blocking IO"
  - "epoll系统调用"
  - "Linux epoll"
---

## Related Concepts
- [[concepts/边缘触发|边缘触发]]
- [[concepts/水平触发|水平触发]]
- [[concepts/epoll_ctl|epoll_ctl]]
- [[concepts/blocking-io|Blocking IO]]
- [[concepts/asynchronous-io|Asynchronous IO]]
- [[concepts/kqueue|kqueue]]
- [[concepts/select|select]]
- [[concepts/poll|poll]]
- [[concepts/non-blocking-io|Non-blocking IO]]

## Related Entities
- [[entities/redis|redis]]
- [[entities/nginx|nginx]]
- [[entities/node-js|node-js]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/brpc|brpc]]
- [[entities/socket|socket]]
- [[entities/socketid|socketid]]
- [[entities/inputmessenger|InputMessenger]]

## Mentions in Source

> **Source: [[sources/io|io]]**
> - "non-blocking IO: 发起IO操作后不阻塞，用户可阻塞等待多个IO操作同时结束。non-blocking也是一种同步IO："批量的同步"。"
> - "linux一般使用non-blocking IO提高IO并发度。"
> - "non-blocking IO一般由少量event dispatching线程和一些运行用户逻辑的worker线程组成，这些线程往往会被复用（换句话说调度工作转移到了用户态）。"
> - "如linux下的poll,select, epoll，BSD下的kqueue。"
> - "由于epoll的一个bug(开发brpc时仍有)及epoll_ctl较大的开销，EDISP使用Edge triggered模式。"
> - "比如epoll_ctl，由于epoll实现为一棵红黑树，epoll_ctl并不是一个很快的操作，特别在多核环境下，依赖epoll_ctl的实现往往会面临棘手的扩展性问题。"