---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/getting_started.md]]"
  - "[[brpc/en_client.md]]"
  - "[[brpc/client.md]]"
  - "[[brpc/bvar_c++.md]]"
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
gflags 是 brpc 生态中用于配置全局行为的基础设施。在 brpc 的 server 与 client 端，许多底层行为通过 gflags 进行调节，包括请求/响应体大小上限（`-max_body_size`）、空闲连接关闭日志（`-log_idle_connection_close`）、向系统释放空闲内存的间隔（`-free_memory_to_system_interval`），以及命名服务访问间隔（`-ns_access_interval`）等。brpc 充分利用 gflags 替代 protobuf 自带的消息尺寸限制，只要 `-max_body_size` 设置得足够大，消息就不会被拒收。

在日志系统方面，brpc 使用 `--verbose` 和 `--verbose_module` 两个 gflag 来控制分层详细日志 VLOG 的输出级别（注意与 glog 的 `--v`/`--vmodule` 区别），且这两个参数可以通过 `google::SetCommandLineOption` 在运行时动态修改。构建层面，brpc 将 gflags 2.1-2.2.2 列为推荐版本，cmake 需指定特定选项以改变其默认不构建共享库的行为。

在 bvar 体系中，gflags 同样关键：可通过 `-bvar_dump` 在启动时开启后台导出线程，也可通过 `-bvar_dump_file` 与 `-bvar_dump_include` 等参数控制导出行为；不想依赖命令行解析的用户可在 `main` 函数中通过 `google::ParseCommandLineFlags` 启用，或利用 `bvar::GFlag` 类将关键 gflag 公开为同名的 bvar 以便统一监控。文档特别警告：不要直接对 `FLAGS_bvar_dump_file` 等 `std::string` 类型的 gflag 赋值，因为该操作既非线程安全，也不会触发 validator 回调来启动后台导出线程。

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
- [[concepts/静态链接|静态链接]]
- [[concepts/config_brpc.sh|config_brpc.sh]]
- [[concepts/ChannelOptions|ChannelOptions]]
- [[concepts/Controller|Controller]]
- [[concepts/Health Checking|Health Checking]]
- [[concepts/Connection Type|Connection Type]]
- [[concepts/Timeout|Timeout]]
- [[concepts/连接方式|连接方式]]
- [[concepts/命名服务|命名服务]]
- [[concepts/bvar导出|bvar导出]]
- [[concepts/bvar命名规范|bvar命名规范]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|protocol-buffers]]
- [[entities/iobuf|iobuf]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/brpc-channeloptions|brpc::ChannelOptions]]
- [[entities/bvar|bvar]]
- [[entities/bvar-gflag|bvar::GFlag]]

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

> **Source: [[sources/en_client]]**
> - "global gflags: for tuning global behaviors, being unchanged generally. Read comments in [/flags](flags.md) before setting."
> - "gflags makes configurations of global behaviors easier."
> - "A related gflag is -ns_access_interval"

> **Source: [[sources/client]]**
> - "全局gflags：常用于调节一些底层代码的行为，一般不用修改。请自行阅读服务/flags页面中的说明。"
> - "consul的默认地址是localhost:8500，可通过gflags设置-consul_agent_addr来修改。"

> **Source: [[sources/bvar_c++]]**
> - "用[gflags](flags.md)解析输入参数，在程序启动时加入-bvar_dump，或在brpc中也可通过[/flags](flags.md)服务在启动后动态修改。"
> - "不想用gflags解析参数，希望直接在程序中默认打开，在main函数处添加如下代码："
> - "请勿直接设置FLAGS_bvar_dump_file / FLAGS_bvar_dump_include / FLAGS_bvar_dump_exclude。一方面这些gflag类型都是std::string，直接覆盖是线程不安全的；另一方面不会触发validator（检查正确性的回调），所以也不会启动后台导出线程。"