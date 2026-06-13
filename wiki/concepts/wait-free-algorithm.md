---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "无等待算法"
  - "wait-free manner"
  - "wait-free"
  - "无等待算法"
  - "wait-free manner"
  - "wait-free MPSC list"
  - "无等待算法"
  - "wait-free manner"
  - "wait-free"
  - "无等待算法"
  - "wait-free manner"
  - "Wait-free MPSC list"
  - "无等待算法"
  - "wait-free manner"
  - "wait-free"
  - "无等待算法"
  - "wait-free manner"
  - "wait-free MPSC list"
  - "无等待算法"
  - "wait-free manner"
  - "wait-free"
  - "无等待算法"
  - "wait-free manner"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bthread|bthread]]
- [[entities/socket|Socket]]
- [[entities/socketid|SocketId]]
- [[entities/eventdispatcher|EventDispatcher]]

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "the first thread directly writes in-place and other threads submit their write requests in wait-free manner."
> - "One fd can be written into 5,000,000 16-byte messages per second by a couple of highly-contended threads."
> - "When multiple threads write into the same fd (common for multiplexed connections), the first thread directly writes in-place and other threads submit their write requests in wait-free manner."
> - "When multiple threads write into the same fd (common for multiplexed connections), the first thread directly writes in-place and other threads submit their write requests in [wait-free](https://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom) manner."
> - "One fd can be written into 5,000,000 16-byte messages per second by a couple of highly-contended threads."

> **Source: [[sources/en_io|en_io]]**
> - "brpc uses a special wait-free MPSC list to solve the issue."
> - "When a thread wants to write out some data, it tries to atomically exchange the node with the list head(Socket::_write_head) first."
> - "This method makes the writing contentions wait-free."
> - "All data ready to write is put into a node of a singly-linked list, whose next pointer points to a special value(Socket::WriteRequest::UNCONNECTED)."
> - "These methods make contentions on dispatching events of one fd wait-free."
> - "This function is wait-free."

## Description

等待自由算法是并发编程中的一种非阻塞算法，保证每个线程在有限步骤内完成操作，无论其他线程的速度或行为如何。在brpc中，等待自由算法被用于高效处理多线程对同一个文件描述符的写入操作，以及事件分发机制。

### 技术实现

- 使用特殊的等待自由MPSC（多生产者单消费者）列表来解决多线程写入问题
- 写入线程通过原子操作将节点与列表头(`Socket::_write_head`)交换
- 所有待写数据放入单链表的节点中，节点的next指针指向特殊值`Socket::WriteRequest::UNCONNECTED`
- 第一个线程直接进行原地写入，其他线程以等待自由的方式提交写入请求

### 性能特点

- 一个文件描述符每秒可被多个高竞争线程写入5,000,000条16字节消息
- 对单个文件描述符的事件分发竞争也是等待自由的