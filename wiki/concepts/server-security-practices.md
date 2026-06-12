---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "服务端安全实践"
  - "安全配置"
  - "Security Configuration"
  - "服务端安全实践"
  - "安全配置"
---

## Description
服务端安全实践是保障生产环境 brpc 服务稳定运行的关键措施。通过设置 `ServerOptions.internal_port` 为仅内网可达的端口，可以确保内置服务页面（如状态监控、性能分析）不被公网暴露。配合 [[entities/nginx|nginx]] 等反向代理服务，可严格限制对特定 URL 路径的访问——即使经过 nginx 代理的外部请求，也必须警惕安全风险。对于公网服务，必须禁用 `-enable_dir_service`（目录服务）和 `-enable_threads_service`（线程服务）等危险启动选项，以防止目录遍历和线程操作被滥用。对用户可控的 URL 参数使用 `brpc::WebEscape()` 进行转义，可有效防止跨站脚本（XSS）等注入攻击。此外，服务错误信息中应使用 MD5 签名代替真实的内部服务器地址，避免拓扑信息泄露。最后，禁止以 root 用户身份启动 brpc 进程，防止攻击者利用漏洞进行未授权文件写入。这些配置共同构成了生产环境中公网服务的多层次安全防护体系。

## Related Concepts
- [[concepts/SSL|SSL]]
- [[concepts/Authenticator|Authenticator]]
- [[concepts/Max_concurrency|Max concurrency]]
- [[concepts/内置服务|内置服务]]
- [[concepts/日志控制|日志控制]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/ServerOptions|ServerOptions]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Set ServerOptions.internal_port to a port which can **only be accessible from internal**."
> - "**Don't turn on** -enable_dir_service and -enable_threads_service on public services."
> - "brpc::WebEscape() escapes url to prevent injection attacks with malice."
> - "if brpc runs as the root user, attackers may exploit this feature to perform unauthorized file writes."
> - "Consider returning signatures of the addresses. For example after setting ServerOptions.internal_port, addresses in error information returned by server is replaced by their MD5 signatures."
> - "If requests are from public(including being proxied by nginx etc), you have to be aware of some security issues."
> - "Set internal port. Set ServerOptions.internal_port to a port which can only be accessible from internal."