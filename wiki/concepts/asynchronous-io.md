---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "term"
aliases:
  - "异步 I/O"
  - "AIO"
  - "Asynchronous I/O"
  - "Linux AIO"
  - "异步 I/O"
  - "AIO"
  - "Asynchronous I/O"
---

## Related Concepts
- [[concepts/blocking-io|Blocking IO]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/overlapped|OVERLAPPED]]
- [[concepts/iocp|IOCP]]

## Related Entities
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/socket|Socket]]
- [[entities/inputmessenger|InputMessenger]]

## Mentions in Source
> **Source: [[sources/en_io|en_io]]**
> - "Asynchronous IO: Start a read or write operation with a callback, which will be called when the IO is done, such as OVERLAPPED + IOCP in Windows."
> - "Native AIO in Linux only supports files."
> - "brpc uses non-blocking IO instead of asynchronous IO."

> **Source: en_io**
> - No directly relevant information provided.

> **Source: [[sources/io|io]]**
> - "asynchronous IO: 发起IO操作后不阻塞，用户得递一个回调待IO结束后被调用。如windows下的OVERLAPPED + IOCP。linux的native AIO只对文件有效。"