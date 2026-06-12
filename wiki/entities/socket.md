---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "other"
aliases:
  - "Socket 结构体"
  - "brpc Socket"
---

## Related Concepts
- [[concepts/blocking-io|Blocking IO]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/bthread|bthread]]
- [[concepts/wait-free|wait-free]]
- [[concepts/lock-free|lock-free]]
- [[concepts/health-checking|Health Checking]]
- [[concepts/wait-free-mpsc-list|wait-free MPSC list]]
- [[concepts/streaming-rpc|Streaming RPC]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "Socket contains data structures related to fd and is one of the most complex structure in brpc. The unique feature of this structure is that it uses 64-bit SocketId to refer to a Socket object to facilitate usages of fd in multi-threaded environments."
> - "We can see that, Socket is similar to shared_ptr in the sense of referential counting and SocketId is similar to weak_ptr."
> - "Address returns a SocketUniquePtr which will be released automatically. The content of Socket remains unchanged as long as the pointer is valid."
> - "SetFailed marks the Socket as invalid. After that, Address returns null pointer until health check recovers the Socket."
> - "The writing of Socket uses a wait-free multi-producer single-consumer linked list to handle multi-threaded writing efficiently."

> **Source: [[sources/en_io|en_io]]**
> - No directly relevant information provided about Socket.