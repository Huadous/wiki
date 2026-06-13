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
  - "SocketUniquePtr智能指针"
  - "套接字唯一指针"
---

## Related Entities
- [[entities/controller|Controller]]
- [[entities/socket|Socket]]
- [[entities/eventdispatcher|EventDispatcher]]

## Related Concepts
- [[concepts/wait-free|Wait-Free]]
- [[concepts/lock-free|Lock-Free]]
- [[concepts/bthread|Bthread]]
- [[concepts/health-checking|Health Checking]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/strong-reference|强引用]]
- [[concepts/weak-reference|弱引用]]
- [[concepts/race-condition|竞态条件]]
- [[concepts/aba-problem|ABA问题]]
- [[concepts/edge-triggered-mode|Edge Triggered 模式]]
- [[concepts/wait-free-mpsc-链表|Wait-free MPSC 链表]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released."
> - "As long as SocketUniquePtr is valid, the Socket enclosed will not be changed..."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed."
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released. When Socket is set failed, the pointer returned is empty. As long as Address returns a non-null pointer, the contents are guaranteed to not change until the pointer is destructed."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed. For example, Controller is used thoroughly inside RPC and has a lot of interactions with Socket, it uses SocketUniquePtr."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed. For example, Controller is used thoroughly inside RPC and has a lot of interactions with Socket, it uses SocketUniquePtr."
> - "As long as SocketUniquePtr is valid, the Socket enclosed will not be changed so that users have no need to care about race conditions and ABA problems, being safer to operate the shared socket."

> **Source: [[sources/io|io]]**
> - "Address：取得id对应的Socket，包装在一个会自动释放的unique_ptr中(SocketUniquePtr)，当Socket被SetFailed后，返回指针为空。只要Address返回了非空指针，其内容保证不会变化，直到指针自动析构。这个函数是wait-free的。"
> - "由于SocketUniquePtr只要有效，其中的数据就不会变，这个机制使用户不用关心麻烦的race condition和ABA problem，可以放心地对共享的fd进行操作。"
> - "brpc中有大量的SocketUniquePtr和SocketId，它们确实简化了我们的开发。"