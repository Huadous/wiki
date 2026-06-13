---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
tags:
  - "method"
aliases:
  - "解析回调"
  - "Parse回调"
---

## Description
Parse callback 是 brpc 中 `InputMessenger` 用于从二进制数据流中切割消息的函数，其运行时间相对稳定，不受业务逻辑影响。它负责识别不同协议的消息边界，将接收到的原始字节解析为完整的消息单元，然后将结构化消息交给 `Process` 回调进行深度解析（如 protobuf 解析）并调用用户回调。作为消息处理的第一步，parse callback 是可定制的，这使得 brpc 能够支持多种不同的协议。`InputMessenger` 会按注册的协议顺序依次尝试调用不同的 Parse 回调，成功解析后记忆当前协议以避免后续重试。当从文件描述符读取 n(n > 1) 个消息时，`InputMessenger` 会启动 n-1 个 bthread 分别处理前 n-1 个消息，并在本地处理最后一个消息，从而实现高效的消息切割与并行处理。

## Related Concepts
- [[concepts/Process-callback|Process callback]]
- [[concepts/protocols|协议]]

## Related Entities
- [[entities/inputmessenger|InputMessenger]]
- [[entities/socket|Socket]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bthread|bthread]]

## Mentions in Source
> **Source: [[sources/en_io]]**
- "Parse callback cuts messages from binary data and has relatively stable running time;" 
- "InputMessenger cuts messages and uses customizable callbacks to handle different format of data. `Parse` callback cuts messages from binary data and has relatively stable running time; `Process` parses messages further(such as parsing by protobuf) and calls users' callbacks, which vary in running time." 
- "If n(n > 1) messages are read from the fd, InputMessenger launches n-1 bthreads to handle first n-1 messages respectively, and processes the last message in-place."
- "Parse callback cuts messages from binary data and has relatively stable running time; Process parses messages further(such as parsing by protobuf) and calls users' callbacks, which vary in running time."