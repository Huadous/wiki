---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/io.md]]"
tags:
  - "other"
aliases:
  - "Socket 结构体"
  - "brpc Socket"
---

## Related Entities
- [[entities/loadbalancer|LoadBalancer]]
- [[entities/namingservice|NamingService]]

## Related Concepts
- [[concepts/blocking-io|Blocking IO]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/bthread|bthread]]
- [[concepts/wait-free|wait-free]]
- [[concepts/lock-free|lock-free]]
- [[concepts/health-checking|Health Checking]]
- [[concepts/wait-free-mpsc-list|wait-free MPSC list]]
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/socketid|SocketId]]
- [[concepts/socketuniqueptr|SocketUniquePtr]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "Socket contains data structures related to fd and is one of the most complex structure in brpc. The unique feature of this structure is that it uses 64-bit SocketId to refer to a Socket object to facilitate usages of fd in multi-threaded environments."
> - "We can see that, Socket is similar to shared_ptr in the sense of referential counting and SocketId is similar to weak_ptr."
> - "Address returns a SocketUniquePtr which will be released automatically. The content of Socket remains unchanged as long as the pointer is valid."
> - "SetFailed marks the Socket as invalid. After that, Address returns null pointer until health check recovers the Socket."
> - "The writing of Socket uses a wait-free multi-producer single-consumer linked list to handle multi-threaded writing efficiently."

> **Source: [[sources/en_io|en_io]]**
> - No directly relevant information provided about Socket.

> **Source: [[sources/load_balancing|load_balancing]]**
> - "为需要的连接动态创建一个bthread专门做健康检查（Socket::StartHealthCheck）。"
> - "SetFailed marks the Socket as invalid. After that, Address returns null pointer until health check recovers the Socket." (健康检查线程先在确保没有其他人在使用Socket了后关闭连接。目前是通过对Socket的引用计数判断的。)
> - "连上后复活Socket(Socket::Revive)，这样Socket就又能被其他地方，包括LoadBalancer访问到了（通过Socket::Address）。"

> **Source: [[sources/io|io]]**
> - "和fd相关的数据均在Socket中，是rpc最复杂的结构之一，这个结构的独特之处在于用64位的SocketId指代Socket对象以方便在多线程环境下使用fd。"
> - "Create：创建Socket，并返回其SocketId。"
> - "Address：取得id对应的Socket，包装在一个会自动释放的unique_ptr中(SocketUniquePtr)，当Socket被SetFailed后，返回指针为空。只要Address返回了非空指针，其内容保证不会变化，直到指针自动析构。这个函数是wait-free的。"

> **Source: [[sources/io|io]]**
> - No directly relevant information.