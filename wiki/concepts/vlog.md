---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/builtin_service]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "term"
aliases:
  - "VLOG控制服务"
  - "brpc VLOG接口"
---

## Description
`/vlog` 是 brpc 内置服务提供的 HTTP 接口，开发者可以通过浏览器查看当前可开启的 VLOG 模块列表，并在不重启服务的情况下交互式地调整特定模块的日志级别，从而方便线上问题的排查。`/vlog` 仅作用于 brpc 自研的 streaming_log 流式日志系统，对 glog 无效。

VLOG 机制本身是 streaming_log 中的分层详细日志机制，调用方式形如 `VLOG(verbose_level)`，类似 glog 的 `VLOG(n)`，对应 glog 的 INFO 级详细日志；层级越深代表越详细的调试信息。VLOG 的启用通过两个 gflags 控制：全局最低级别由 `--verbose` 设置；按文件/模块名进行细粒度覆盖则使用 `--verbose_module`（注意 streaming_log 使用 `--verbose`，而 glog 使用 `--v`，参数名不同）。`--verbose_module` 可以按模块名（即源码文件名或路径名）单独覆盖全局层级，例如 `--verbose_module="channel=2"` 可以让 `channel.cpp` 中的 `VLOG(2)` 打印出来，而其他模块保持原状。这两个 gflag 也可以通过 `google::SetCommandLineOption` 在运行时动态调整，实现不重启服务的级别变更。

此外，VLOG 还提供变种 `VLOG2`，允许用户指定虚拟文件路径而非使用真实文件名，以便更灵活地按模块过滤日志。`VLOG_IF` 和 `VLOG2_IF` 是相应的条件打印版本。

## Related Concepts
- [[concepts/builtin_service|内置服务]]
- [[concepts/version|/version]]
- [[concepts/health|/health]]
- [[concepts/protobufs|/protobufs]]
- [[concepts/streaming_log|streaming_log]]
- [[concepts/log_macros|LOG宏]]
- [[concepts/dlog|DLOG]]
- [[concepts/throttled_logging|节流日志]]
- [[concepts/vlog|VLOG（详细日志）]]
- [[concepts/vlog2|VLOG2]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/glog|glog]]

## Mentions in Source

> **Source: [[sources/builtin_service|builtin_service]]**
> - "/vlog: 查看程序中当前可开启的VLOG（对glog无效）。"
> - "作为其他服务之一，/vlog帮助在不重启服务的情况下开启特定模块的调试日志，极大方便了线上问题排查。"

> **Source: [[sources/streaming_log|streaming_log]]**
> - "VLOG(verbose_level)是分层的详细日志，通过两个gflags：*--verbose*和*--verbose_module*控制需要打印的层（注意glog是--v和–vmodule）。"
> - "VLOG有一个变种VLOG2让用户指定虚拟文件路径"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "VLOG(verbose_level) is detail log that support multiple layers."
> - "Note that glog uses --v and --vmodule."
> - "You can set --verbose and --verbose_module through google::SetCommandLineOption dynamically."