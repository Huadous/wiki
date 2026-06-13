---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "内部端口"
  - "内网端口"
  - "ServerOptions.internal_port"
  - "内置服务安全 (Internal port)"
  - "内部端口"
  - "内网端口"
  - "ServerOptions.internal_port"
  - "内置服务保护"
  - "内部端口"
  - "内网端口"
  - "ServerOptions.internal_port"
  - "内置服务安全 (Internal port)"
  - "内部端口"
  - "内网端口"
  - "ServerOptions.internal_port"
---

## Description

`internal_port` 提供了一种网络隔离机制，将服务器内置服务（如 `/status`、`/flags`、`/version` 等监控和调试接口）与公开访问分离。当设置了 `internal_port` 后，公开端口（即传递给 `Start()` 的公共端口）在收到访问内置服务的请求时会拒绝并返回特定错误信息，而只有内部网络可以通过 `internal_port` 正常访问这些服务。这种设计有效防止了敏感信息（如服务器配置、运行时状态、变量标志等）通过公网泄露，是 brpc 安全实践中的重要组成部分。建议在生产环境中启用 `internal_port`，以限制内置服务的访问途径。除了设置内部端口，brpc 还提供了多种互补的安全措施：通过 [[entities/nginx|nginx]] 等代理仅转发指定 URL、使用 `ServerOptions.has_builtin_services` 完全禁用内置服务、对用户可控 URL 进行转义（`brpc::WebEscape()`），以及禁用 `-enable_dir_service` 和 `-enable_threads_service` 等选项。此外，建议不以 root 用户启动进程，以避免潜在的文件写入攻击。未设置 `internal_port` 时，公开端口默认允许访问内置服务以实现降级兼容。

## Related Concepts
- [[concepts/ServerOptions|ServerOptions]]
- [[concepts/内置服务|内置服务]]
- [[concepts/服务器生命周期管理|服务器生命周期管理]]
- [[concepts/服务器安全实践|服务器安全实践]]
- [[concepts/安全配置|安全配置]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]
- [[entities/nginx|nginx]]

## Mentions in Source

> **Source: [[sources/en_server]]**
- "Set internal port. Set ServerOptions.internal_port to a port which can only be accessible from internal. You can view builtin services via internal_port, while accesses from the public port... should see following error:"
- "Not allowed to access builtin services, try ServerOptions.internal_port=... instead if you're inside internal network"
- "Set ServerOptions.internal_port to a port which can only be accessible from internal."
- "Builtin services are useful, on the other hand include a lot of internal information and shouldn't be exposed to public."
- "If requests are from public (including being proxied by nginx etc), you have to be aware of some security issues."
- "Set internal port. Set ServerOptions.internal_port to a port which can **only be accessible from internal**."
- "You can view builtin services via internal_port, while accesses from the public port (the one passed to Server.Start) should see following error:"
- "Set ServerOptions.has_builtin_services = false, you can completely disable the built-in services."
- "**Don't turn on** -enable_dir_service and -enable_threads_service on public services."
> **Source: [[sources/en_server]]**
- "Set ServerOptions.internal_port to a port which can **only be accessible from internal**. You can view builtin services via internal_port, while accesses from the public port (the one passed to Server.Start) should see following error:"
- "Not allowed to access builtin services, try ServerOptions.internal_port=... instead if you're inside internal network"