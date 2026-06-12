---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "other"
aliases:
  - "SocketId 标识符"
  - "64-bit Socket引用"
  - "brpc SocketId"
---

## Related Concepts
- [[concepts/lock-free|lock-free]] — SocketId的设计借鉴了无锁编程思想
- [[concepts/wait-free|wait-free]] — SocketId的访问操作具有wait-free特性
- [[concepts/weak-reference|weak-reference]] — SocketId类似于弱引用指针的语义设计

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "The unique feature of this structure is that it uses 64-bit SocketId to refer to a Socket object to facilitate usages of fd in multi-threaded environments."（该结构的独特之处在于使用64位SocketId引用Socket对象，以简化多线程环境中fd的使用。）
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released. When Socket is set failed, the pointer returned is empty."（Address: 从id检索Socket，并将其包装为会自动释放的unique_ptr(SocketUniquePtr)。当Socket被设置为失败状态时，返回的指针为空。）