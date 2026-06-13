---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[concepts/单线程反应器]]"]
tags: [term]
aliases:
  - "kqueue 事件通知机制"
  - "BSD kqueue"
  - "kqueue 接口"
---


# kqueue

## 定义
kqueue 是 FreeBSD、macOS 等 BSD 衍生操作系统提供的一种可扩展的 I/O 事件通知接口。它允许用户空间程序向内核注册感兴趣的事件，涵盖 I/O 就绪、信号递送、文件系统变更、进程状态变化等多种类型。内核在事件发生时将通知应用，从而实现高效的事件驱动编程。kqueue 在功能上与 Linux 的 [[concepts/epoll|epoll]] 相当，是 BSD 系操作系统处理高并发网络连接的基石。

## 关键特征
- **多种事件类型支持**：除常规的文件描述符 I/O 事件（读/写就绪）外，kqueue 还支持信号（EVFILT_SIGNAL）、进程状态（EVFILT_PROC）、定时器（EVFILT_TIMER）、Vnode 事件（EVFILT_VNODE）等多种过滤器类型，覆盖面远超传统的 select/poll。
- **可扩展性**：使用 `kevent` 系统调用，通过注册/注销感兴趣的事件集合（eventlist）来进行批量操作，避免了每次调用传递所有描述符的开销。事件复杂度为 O(事件数)，与文件描述符总数无关，适合数千至数万个并发连接。
- **一次性注册**：事件通过 `EV_ADD` 标志注册后持久存在，无需像 select 那样每次循环重新加入。
- **边缘触发与水平触发**：同时支持边缘触发（EV_CLEAR）和水平触发（默认）模式，后者在事件未被处理时重复通知。
- **与 epoll 对比**：内核实现机制不同，但面向的应用场景高度一致。kqueue 在 API 设计上更通用（可监视非 I/O 事件），而 epoll 专为网络 I/O 优化。两者编程模型均为注册-等待-处理-再等待 的事件循环。
- **跨平台限制**：仅适用于 BSD 系内核（FreeBSD、OpenBSD、NetBSD、macOS）。在 Linux 上通常通过 epoll 实现等效功能。

## 应用
- **高性能网络服务器**：作为 BSD 系统上 I/O 多路复用的主力机制，被广泛应用于 Redis、nginx、Memcached、PostgreSQL 等知名服务的跨平台实现（常作为 epoll 的替代），以支撑数千乃至数万个并发连接。
- **单线程反应器模式**：在单线程反应器中，kqueue 被用作高效的事件循环核心。如源文档所述，Redis 在 BSD 系统上使用 kqueue 处理 I/O，实现单线程高并发。
- **异步 I/O 框架**：libevent、libuv 等事件库在 macOS/FreeBSD 上底层使用 kqueue 提供高性能异步 I/O 支持。
- **系统监视工具**：利用 `EVFILT_VNODE` 等过滤器实现文件变更监听（如 `fswatch` 类工具）和进程状态追踪。

## 相关概念
- [[concepts/io多路复用|I/O多路复用]]
- [[concepts/epoll|epoll]]
- [[concepts/单线程反应器|单线程反应器]]
- [[concepts/单线程反应器|单线程反应器]]

## 相关实体
- [[entities/redis|redis]]
- [[entities/nginx|nginx]]

## 来源提及
- "非阻塞 IO：使用 epoll、kqueue 等高效 IO 多路复用机制，支持成千上万个并发连接。" — [[concepts/单线程反应器|单线程反应器]]