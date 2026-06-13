---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "处理回调"
  - "Process callback"
  - "brpc 消息处理回调"
---

## 描述
Process callback 是 brpc 消息处理流水线中承上启下的关键环节。当一个消息被 `InputMessenger` 从二进制字节流中切割出来后，Process 回调负责对其进一步解析（如 protobuf 反序列化）并调用用户注册的业务回调函数。与运行时间相对稳定的 Parse 回调不同，Process 回调的执行时间因消息解析复杂度和业务逻辑而异，因此 brpc 会为其创建独立的 bthread（协程）执行，避免阻塞事件循环线程。当从同一个 fd 读取到多个消息时，brpc 会对前 n-1 个消息启动独立的 bthread 执行 Process 回调，而最后一个消息则在当前上下文中原地处理，从而在实现高效并发的同时减少调度开销。Process callback 是连接底层字节流解析与上层 RPC 调用的关键桥梁，将已解析的字节转换为有意义的服务调用。

## 相关概念
- [[concepts/Parse callback|Parse callback]]
- [[concepts/bthread|bthread]]

## 相关实体
- [[entities/inputmessenger|InputMessenger]]
- [[entities/baidu|brpc]]

## 来源提及
> **Source: [[sources/en_io|en_io]]**
> - "`Parse` cuts messages from binary data and has relatively stable running time."
> - "`Process` parses messages further(such as parsing by protobuf) and calls users' callbacks, which vary in running time."
> - "If n(n > 1) messages are read from the fd, InputMessenger launches n-1 bthreads to handle first n-1 messages respectively, and processes the last message in-place."
> - "Parse callback cuts messages from binary data and has relatively stable running time; Process parses messages further(such as parsing by protobuf) and calls users' callbacks, which vary in running time."