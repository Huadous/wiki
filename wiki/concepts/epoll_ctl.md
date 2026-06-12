---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [method]
aliases:
  - "epoll_ctl 系统调用"
  - "epoll控制接口"
---


# epoll_ctl

## 定义
`epoll_ctl`是Linux epoll机制中的核心系统调用，用于对已创建的epoll实例进行事件控制，包括添加新的文件描述符、修改已有文件描述符的事件类型，以及从epoll实例中删除文件描述符。

## 关键特征
- **系统调用开销**：`epoll_ctl`是一个系统调用，相对于用户态操作具有更高的执行成本。
- **红黑树实现**：epoll底层使用红黑树（red-black tree）来管理注册的文件描述符，因此`epoll_ctl`的插入、删除和修改操作的时间复杂度为O(log n)。
- **多线程性能瓶颈**：在多线程环境中，红黑树的并发操作需要加锁保护，导致`epoll_ctl`在竞争激烈时性能显著下降。
- **高频调用的风险**：在大量连接高频率添加或修改事件场景下，频繁调用`epoll_ctl`会成为系统的性能瓶颈。

## 应用
- **epoll实例管理**：在事件驱动的网络服务器中，用于注册新连接的读写事件。
- **事件类型更新**：当连接状态发生变化（如从读事件切换到写事件）时，修改文件描述符的事件类型。
- **连接关闭**：当连接关闭时，从epoll实例中删除对应的文件描述符。
- **brpc中的优化实践**：brpc为了避免高频`epoll_ctl`调用带来的性能问题，采用了[[concepts/edge-triggered|边缘触发模式]]和[[concepts/atomic-variable|原子变量]]来管理事件分发，从而减少对`epoll_ctl`的依赖。

## 相关概念
- [[concepts/epoll|epoll]]
- [[concepts/edge-triggered-mode|边缘触发模式]]
- [[concepts/atomic-variable|原子变量]]
- [[concepts/system-call|系统调用]]
- [[concepts/red-black-tree|红黑树]]

## 相关实体
- [[entities/socket|Socket]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/socketid|SocketId]]

## 来源提及
- "more system calls, such as epoll_ctl." — [[sources/en_io|en_io]]
- "Since epoll is implemented as a red-black tree, epoll_ctl is not a very fast operation, especially in multi-threaded environments." — [[sources/en_io|en_io]]