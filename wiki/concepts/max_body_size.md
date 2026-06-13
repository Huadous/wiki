---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
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
  - "限制最大消息"
  - "最大消息体大小"
  - "消息大小限制"
  - "max_body_size"
  - "gflags"
  - "最大消息体大小"
  - "消息大小限制"
  - "max_body_size"
---

## Description
max_body_size 是 brpc 提供的一项安全配置选项，用于保护 server 和 client 免受超大消息攻击。当 server 收到的 request 或 client 收到的 response 超过该限制时，brpc 会拒收消息并关闭连接，同时打印相应的错误日志（例如 "A message from ... is bigger than ... bytes, the connection will be closed. Set max_body_size to allow bigger messages"）。该选项通过 gflag `-max_body_size` 配置，单位为字节，默认值为 67108864（64MB）。值得注意的是，brpc 移除了 protobuf 中 CodedInputStream 默认的 TotalBytesLimit 限制，完全由 `-max_body_size` 单独控制：只要该 flag 足够大，消息就不会被拒收，也不会打印错误日志。此功能对 protobuf 的版本没有要求。

## Related Concepts
- [[concepts/baidu_std|baidu_std]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/ServerOptions|ServerOptions]]
- [[concepts/Max concurrency|Max concurrency]]
- [[concepts/Compression|Compression]]
- [[concepts/SSL|SSL]]
- [[concepts/Builtin services|Builtin services]]
- [[concepts/安全配置|安全配置]]
- [[concepts/空闲连接超时|空闲连接超时]]
- [[concepts/安全性|安全性 (Security Configuration)]]
- [[concepts/VLOG|VLOG]]
- [[concepts/streaming_log|streaming_log]]

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

> **Source: [[sources/streaming_log]]**
> - "VLOG(verbose_level)是分层的详细日志，通过两个gflags：--verbose和--verbose_module控制需要打印的层（注意glog是--v和–vmodule）。"
> - "--verbose=1 --verbose_module=\"channel=2,server=3\"                # 打印channel.cpp中<=2，server.cpp中<=3，其他文件<=1的VLOG"
> - "--verbose和--verbose_module可以通过google::SetCommandLineOption动态设置。"

> **Source: [[sources/server]]**
> - "为了保护server和client，当server收到的request或client收到的response过大时，server或client会拒收并关闭连接。"
> - "此最大尺寸由-max_body_size控制，单位为字节。"
> - "brpc移除了protobuf中的限制，全交由此选项控制，只要-max_body_size足够大，用户就不会看到错误日志。"
> - "A message from 127.0.0.1:35217(protocol=baidu_std) is bigger than 67108864 bytes, the connection will be closed. Set max_body_size to allow bigger messages"