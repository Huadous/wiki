---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/io.md]]"
tags:
  - "other"
aliases:
  - "SocketId 标识符"
  - "64-bit Socket引用"
  - "brpc SocketId"
---

## Related Entities
- [[entities/brpc|brpc]] — SocketId 是 brpc 中广泛应用的 id 类型之一

## Related Concepts
- [[concepts/lock-free|lock-free]] — SocketId 的设计借鉴了无锁编程思想
- [[concepts/wait-free|wait-free]] — SocketId 的访问操作具有 wait-free 特性
- [[concepts/weak-reference|weak-reference]] — SocketId 类似于弱引用指针的语义设计
- [[concepts/bthread-t|bthread_t]] — SocketId 与 bthread_t 采用相同的生成和分配方式
- [[concepts/aba-problem|ABA问题]] — 版本号机制用于检测多线程环境下的 ABA 问题，SocketId 机制使用户无需关心该问题
- [[concepts/equal-sized-object-allocation|等长对象分配]] — SocketId 体现了等长对象分配方案在不同对象类型间的可复用性
- [[concepts/resourcepool|ResourcePool<T>]] — SocketId 的偏移量由 ResourcePool 分配
- [[concepts/socketuniqueptr|SocketUniquePtr]] — SocketId 配合 SocketUniquePtr 使用，前者表示弱引用，后者表示强引用
- [[concepts/shared-ptr|shared_ptr]] — Socket 与 shared_ptr 语义对应，管理引用计数
- [[concepts/weak-ptr|weak_ptr]] — SocketId 与 weak_ptr 语义对应，但可直接作为 epoll data 使用，这是 weak_ptr 无法做到的
- [[concepts/epoll-data|epoll data]] — SocketId 可直接作为 epoll 的 data 字段，区别于 weak_ptr

## Mentions in Source
> **Source: en_io**
> - "The unique feature of this structure is that it uses 64-bit SocketId to refer to a Socket object to facilitate usages of fd in multi-threaded environments."（该结构的独特之处在于使用64位 SocketId 引用 Socket 对象，以简化多线程环境中 fd 的使用。）
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released. When Socket is set failed, the pointer returned is empty."（Address: 从 id 检索 Socket，并将其包装为会自动释放的 unique_ptr(SocketUniquePtr)。当 Socket 被设置为失败状态时，返回的指针为空。）

> **Source: memory_management**
> - "这种id生成方式在brpc中应用广泛，brpc中的SocketId，bthread_id_t也是用类似的方法分配的。"

> **Source: memory_management（新增）**
> - 未提供与 SocketId 直接相关的新增信息。

> **Source: io**
> - "和fd相关的数据均在Socket中，是rpc最复杂的结构之一，这个结构的独特之处在于用64位的SocketId指代Socket对象以方便在多线程环境下使用fd。"
> - "可以看出，Socket类似shared_ptr，SocketId类似weak_ptr，但Socket独有的SetFailed可以在需要时确保Socket不能被继续Address而最终引用计数归0。"
> - "另外weak_ptr无法直接作为epoll的data，而SocketId可以。"

> **Source: io（新增）**
> - "No directly relevant information"