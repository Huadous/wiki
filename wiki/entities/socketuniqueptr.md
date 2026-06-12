---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "other"
aliases:
  - "SocketUniquePtr智能指针"
  - "套接字唯一指针"
---

## Related Concepts
- [[concepts/wait-free|Wait-Free]]（需要创建）
- [[concepts/lock-free|Lock-Free]]（需要创建）
- [[concepts/bthread|Bthread]]（需要创建）
- [[concepts/health-checking|Health Checking]]（需要创建）
- [[concepts/non-blocking-io|Non-blocking IO]]（需要创建）
- [[concepts/strong-reference|强引用]]（需要创建）
- [[concepts/race-condition|竞态条件]]（需要创建）
- [[concepts/aba-problem|ABA问题]]（需要创建）

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released."
> - "As long as SocketUniquePtr is valid, the Socket enclosed will not be changed..."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed."
> - "Address: retrieve Socket from an id, and wrap it into a unique_ptr(SocketUniquePtr) that will be automatically released. When Socket is set failed, the pointer returned is empty. As long as Address returns a non-null pointer, the contents are guaranteed to not change until the pointer is destructed."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed. For example, Controller is used thoroughly inside RPC and has a lot of interactions with Socket, it uses SocketUniquePtr."
> - "Using SocketUniquePtr or SocketId depends on if a strong reference is needed. For example, Controller is used thoroughly inside RPC and has a lot of interactions with Socket, it uses SocketUniquePtr."
> - "As long as SocketUniquePtr is valid, the Socket enclosed will not be changed so that users have no need to care about race conditions and ABA problems, being safer to operate the shared socket."

## 描述
SocketUniquePtr 是一个智能指针包装器，用于管理 Socket 对象的生命周期。它通过 unique_ptr 语义确保对 Socket 的独占所有权，在指针有效期内保证所指向的 Socket 内容不会发生变化。使用 SocketUniquePtr 可以提供强引用语义，避免竞态条件和 ABA 问题，使得对共享 Socket 的操作更加安全。在实际使用中，选择 SocketUniquePtr 还是 SocketId 取决于是否需要强引用——例如 Controller 在 RPC 内部需要大量与 Socket 的交互，因此使用 SocketUniquePtr。