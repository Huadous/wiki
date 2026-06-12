---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "最大消息体大小"
  - "消息大小限制"
  - "max_body_size"
  - "gflags"
  - "最大消息体大小"
  - "消息大小限制"
  - "max_body_size"
---

## Related Concepts
- [[concepts/baidu_std|baidu_std]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/ServerOptions|ServerOptions]]
- [[concepts/Max concurrency|Max concurrency]]
- [[concepts/Compression|Compression]]
- [[concepts/SSL|SSL]]
- [[concepts/Builtin services|Builtin services]]
- [[concepts/gflags|gflags]]
- [[concepts/安全配置|安全配置]]
- [[concepts/空闲连接超时|空闲连接超时]]
- [[concepts/安全性|安全性 (Security Configuration)]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/iobuf|iobuf]]

## Mentions in Source
> **Source: [[sources/en_server]]**
> - "The limit is controlled by [-max_body_size](http://brpc.baidu.com:8765/flags/max_body_size), in bytes."
> - "An error log is printed when a message is too large and rejected: FATAL: 05-10 14:40:05: * 0 src/brpc/input_messenger.cpp:89] A message from 127.0.0.1:35217(protocol=baidu_std) is bigger than 67108864 bytes, the connection will be closed. Set max_body_size to allow bigger messages"
> - "Set gflag -free_memory_to_system_interval to make the program try to return free memory to system every so many seconds, values <= 0 disable the feature."
> - "If [-log_idle_connection_close](http://brpc.baidu.com:8765/flags/log_idle_connection_close) is turned on, a log will be printed before closing."
> - "To protect servers and clients, when a request received by a server or a response received by a client is too large, the server or client rejects the message and closes the connection. The limit is controlled by -max_body_size, in bytes."
> - "Set max_body_size to allow bigger messages"
> - "brpc removes the restriction from protobuf and controls the limit by -max_body_size solely: as long as the flag is large enough, messages will not be rejected and error logs will not be printed."