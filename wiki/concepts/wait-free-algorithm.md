---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
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
  - "Wait-free MPSC 链表"
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

## Description

等待自由算法是并发编程中的一种非阻塞算法，保证每个线程在有限步骤内完成操作，无论其他线程的速度或行为如何。在 brpc 中，等待自由算法被用于高效处理多线程对同一个文件描述符（fd）的写入操作，以及事件分发机制。

多个线程可能会同时向一个 fd 发送消息，而写 fd 又是非原子的，因此如何高效率地排队不同线程写出的数据包是 brpc IO 层的关键问题之一。brpc 使用一种 wait-free MPSC（多生产者单消费者）链表来实现这个功能。所有待写出的数据都放入单链表的节点中，next 指针初始化为一个特殊值（`Socket::WriteRequest::UNCONNECTED`）。

写入线程通过与链表头原子交换（CAS）获取写权利：当一个线程想要写出数据时，它首先尝试将节点与链表头（`Socket::_write_head`）进行原子交换。未获取到写权的线程将其 next 指针指向旧的链表头，从而连入链表等待。这种方式使第一个线程可以直接进行原地写入，其他线程以等待自由的方式提交写入请求，从而实现写竞争（writing contention）的 wait-free 特性。

虽然获得写权的线程理论上可能短暂地被阻塞（如系统调用级别），但在实践中很少出现。当需要处理大批量数据时，可以配合 KeepWrite 线程机制来提升吞吐。性能方面，一个 fd 每秒可被多个高竞争线程写入 5,000,000 条 16 字节消息。此外，对单个 fd 的事件分发竞争同样也是 wait-free 的。

## Related Concepts
- [[concepts/原子操作|原子操作]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/keepwrite|KeepWrite]]

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

> **Source: [[sources/io|io]]**
> - "多个线程可能会同时向一个fd发送消息，而写fd又是非原子的，所以如何高效率的排队不同线程写出的数据包是这里的关键。brpc使用一种wait-free MPSC链表来实现这个功能。"
> - "所有待写出的数据都放在一个单链表节点中，next指针初始化为一个特殊值(Socket::WriteRequest::UNCONNECTED)。"
> - "这套方法可以让写竞争是wait-free的。"