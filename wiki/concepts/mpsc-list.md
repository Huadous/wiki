---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [method]
aliases:
  - "多生产者单消费者链表"
  - "MPSC list"
  - "Multi-Producer Single-Consumer List"
---


# MPSC list

## 定义

MPSC（Multi-Producer Single-Consumer）list 是一种 wait-free 的链表数据结构，主要用于多线程并发写入场景。在 brpc 中，它被用作写队列，允许多个生产者（写入线程）同时将数据以节点形式挂载到链表上，但只有一个消费者（实际执行 write 系统调用的线程）负责将链表中的数据刷新到文件描述符。这种设计通过原子交换操作避免了锁竞争，实现 wait-free 的写入。

## 关键特征

- **Wait-free 保证**：多个生产者线程可以并发地将节点插入链表，而无需等待其他线程释放锁，避免阻塞。
- **原子交换机制**：生产者线程通过原子操作（如 CAS）将自身节点与链表头指针交换，实现非阻塞插入。
- **单一消费者模式**：只有一个线程（当前持有写入权的线程）负责遍历链表并实际执行 write 调用，保证写入有序且无数据竞争。
- **特殊哨兵值**：链表节点的 next 指针初始指向一个特殊值（如 `Socket::WriteRequest::UNCONNECTED`），用于标识节点尚未被链接到链表。
- **无锁写入高效**：在多生产者高并发场景下，仅通过原子操作即可完成节点入队，显著提升写入性能。

## 应用

- **brpc 写入队列**：在 brpc 中，多个线程同时向同一个 Socket 文件描述符写入数据时，使用 MPSC list 管理待写入数据，避免锁竞争，提升高并发下的写入性能。
- **网络 I/O 框架**：适用于需要多线程并发写入但仅需单线程处理 I/O 的模型，如事件驱动型网络库。
- **日志系统**：多线程日志系统中，生产者线程将日志条目写入 MPSC list，单一线程负责批量化写入磁盘。

## 相关概念

- [[concepts/wait-free|Wait-free]]

## 相关实体

- [[entities/socket|Socket]]
- [[entities/brpc|brpc]]

## 来源提及

- "brpc uses a special wait-free MPSC list to solve the issue." — [[sources/en_io|en_io]]
- "All data ready to write is put into a node of a singly-linked list, whose next pointer points to a special value(Socket::WriteRequest::UNCONNECTED)." — [[sources/en_io|en_io]]
- "When a thread wants to write out some data, it tries to atomically exchange the node with the list head first." — [[sources/en_io|en_io]]