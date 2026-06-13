---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/getting_started.md]]"
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
- [[concepts/gflags|gflags]]
- [[concepts/静态链接|静态链接]]
- [[concepts/config_brpc.sh|config_brpc.sh]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/iobuf|iobuf]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]

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

> **Source: [[sources/getting_started]]**
> - "gflags: Extensively used to define global options."
> - "以[gflags](https://github.com/gflags/gflags)为例，它默认不构建共享库，你需要给`cmake`指定选项去改变这一行为："
> - "gflags: 2.1-2.2.2"