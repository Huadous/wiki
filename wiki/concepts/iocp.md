---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_io]]"]
tags: [method]
aliases:
  - "I/O Completion Ports"
  - "IOCP完成端口"
---


# IOCP

## 定义
IOCP（I/O Completion Ports，I/O完成端口）是Windows操作系统提供的一种高效异步I/O模型。它允许应用程序发起异步读写操作（通常与OVERLAPPED结构配合使用），并在操作完成时通过完成端口（Completion Port）接收完成通知，从而避免线程阻塞和轮询，实现高并发I/O处理。

## 关键特征
- **异步操作模型**：调用者发起I/O操作后立即返回，无需等待操作完成；操作完成后，I/O完成结果被投递到完成端口的队列中。
- **事件驱动通知**：与回调或信号不同，IOCP使用完成端口对象集中管理I/O完成事件，工作线程从端口取出完成包进行处理。
- **与OVERLAPPED结构绑定**：每次异步I/O请求必须指定OVERLAPPED结构，该结构包含操作偏移量及用户自定义上下文信息，用于完成时识别具体请求。
- **线程池友好**：IOCP天然支持并发量可控的工作线程池模型，开发者创建少量线程即可处理数千个并发连接，减少上下文切换开销。
- **Windows平台专属**：IOCP是Windows NT系列内核提供的底层机制，不跨平台。在Linux平台，类似功能由epoll（非阻塞I/O + 事件通知）实现。

## 应用
- **高性能网络服务器（Windows平台）**：用于实现HTTP服务器、数据库服务器、游戏服务器等需要处理大量并发TCP连接的服务。
- **文件异步读写**：结合OVERLAPPED，对文件进行非阻塞的大块读写操作，提升磁盘I/O吞吐量。
- **RPC框架对比学习**：在brpc文档中，IOCP被作为异步I/O的典型示例，用于与Linux的epoll模式进行对比，帮助开发者理解跨平台I/O模型的差异。

## 相关概念
- [[concepts/asynchronous-io|异步I/O]]
- [[concepts/overlapped-io|Overlapped I/O]]

## 相关实体
无

## 来源提及
- "Asynchronous IO: Start a read or write operation with a callback, which will be called when the IO is done, such as OVERLAPPED + IOCP in Windows." — [[sources/en_io|en_io]]