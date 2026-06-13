---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/server.md]]"
tags: [protobuf服务定义, 异步Service, RAII, session-local data, server-thread-local data, bthread-local, pthread模式, 自适应限流算法, 最大并发控制, SSL, 身份验证, 压缩, JSON <=> PB转换, fork without exec, brpc::Server, brpc::Controller, brpc::ServerOptions, 协议支持, 内置服务, 优雅退出, SO_REUSEPORT, AuthContext, ServerSSLOptions, RPC Protobuf message factory, protobuf arena, 限制最大消息, baidu_std, streaming_rpc, nshead_service, 附件, SNI, butil::EndPoint, DataFactory, ELIMIT, CertInfo, ELOGOFF, RunUntilAskedToQuit, ignore_eovercrowded, ALPN, SetFailed, bthread_key_create, WebEscape]
aliases: ["brpc Server端使用文档", "brpc Server Documentation"]
---

# brpc Server端使用文档 - Summary

## 来源
- Original file: [[brpc/server.md]]
- Ingested: 2026-06-13

## 核心内容
本文档系统介绍了 [[entities/brpc|Apache brpc]] 框架 Server 端的开发流程与高级特性。内容涵盖：基础开发流程（[[concepts/protobuf服务定义|protobuf服务定义]] → Service 实现 → [[entities/protobuf|protobuf]] 接口生成 → 添加到 [[concepts/brpcserver|brpc::Server]] → 启动服务）；核心 RAII 机制（[[entities/closureguard|ClosureGuard]] 确保 done->Run() 被调用）；同步/[[concepts/异步service|异步Service]] 的差异与实现；高级特性包括 [[concepts/ssl|SSL]] 配置、基于连接的 [[concepts/身份验证|身份验证]]（[[concepts/authcontext|AuthContext]]）、[[concepts/压缩|压缩]]、[[concepts/最大并发控制|最大并发控制]] 与 [[concepts/自适应限流算法|自适应限流算法]]、[[concepts/pthread模式|pthread模式]]、三种 [[concepts/session-local-data|session-local]] / [[concepts/server-thread-local-data|server-thread-local]] / [[concepts/bthread-local|bthread-local]] 线程私有数据机制，以及 [[concepts/rpc-protobuf-message-factory|RPC Protobuf message factory]] 和 [[concepts/protobuf-arena|protobuf arena]] 的内存管理；多协议支持（[[concepts/baidu_std|baidu_std]]、[[concepts/streaming_rpc|streaming_rpc]]、[[concepts/协议支持|http/h2/RTMP 等]]）；[[concepts/内置服务|内置服务]]、HTTP/H2 访问、nginx 反向代理；[[concepts/fork-without-exec|fork without exec]] 等场景的注意事项及常见问题 FAQ。

## 关键实体
- [[entities/brpc|brpc]]：百度开源、工业级 C++ RPC 框架，Apache 顶级项目
- [[entities/apache|Apache]]：brpc 项目托管方
- [[entities/closureguard|ClosureGuard]]：brpc 的 RAII 辅助类，管理 done->Run()
- [[entities/defaultrpcpbmessagefactory|DefaultRpcPBMessageFactory]]：brpc Server 默认的 message 工厂
- [[entities/protobuf|protobuf]]：RPC 服务接口与消息定义基础设施
- [[entities/bthread|bthread]]：百度开源用户态线程库，brpc 并发基础
- [[entities/bvar|bvar]]：百度开源监控/计数器库
- [[entities/glog|glog]]：Google 日志库，与 brpc 日志深度集成
- [[entities/nginx|nginx]]：外部 HTTP 流量入口与内置服务保护代理
- [[entities/healthreporter|HealthReporter]]：brpc /health 页面定制类

## 关键概念
- 基础类与配置：[[concepts/brpcserver|brpc::Server]]、[[concepts/brpccontroller|brpc::Controller]]、[[concepts/brpcserveroptions|brpc::ServerOptions]]
- 开发方法：[[concepts/protobuf服务定义|protobuf服务定义]]、[[concepts/异步service|异步Service]]、[[concepts/raii|RAII]]、[[concepts/setfailed|SetFailed]]、[[concepts/rununtilaskedtoquit|RunUntilAskedToQuit]]
- 线程与并发：[[concepts/bthread-local|bthread-local]]、[[concepts/session-local-data|session-local data]]、[[concepts/server-thread-local-data|server-thread-local data]]、[[concepts/pthread模式|pthread模式]]、[[concepts/最大并发控制|最大并发控制]]、[[concepts/自适应限流算法|自适应限流算法]]、[[concepts/ignore_eovercrowded|ignore_eovercrowded]]
- 安全与协议：[[concepts/ssl|SSL]]、[[concepts/serverssloptions|ServerSSLOptions]]、[[concepts/sni|SNI]]、[[concepts/alpn|ALPN]]、[[concepts/certinfo|CertInfo]]、[[concepts/身份验证|身份验证]]、[[concepts/authcontext|AuthContext]]、[[concepts/baidu_std|baidu_std]]、[[concepts/streaming_rpc|streaming_rpc]]、[[concepts/协议支持|协议支持]]、[[concepts/nshead_service|nshead_service]]、[[concepts/附件|附件]]、[[concepts/butilendpoint|butil::EndPoint]]
- 服务端特性：[[concepts/内置服务|内置服务]]、[[concepts/优雅退出|优雅退出]]、[[concepts/elogoff|ELOGOFF]]、[[concepts/elimit|ELIMIT]]、[[concepts/so_reuseport|SO_REUSEPORT]]、[[concepts/限制最大消息|限制最大消息]]、[[concepts/json-=-pb转换|JSON <=> PB转换]]、[[concepts/compress|压缩]]（[concepts/压缩|压缩]）
- 内存管理：[[concepts/rpc-protobuf-message-factory|RPC Protobuf message factory]]、[[concepts/protobuf-arena|protobuf arena]]、[[concepts/datafactory|DataFactory]]、[[concepts/bthread_key_create|bthread_key_create]]
- 现象与工具：[[concepts/fork-without-exec|fork without exec]]、[[concepts/webescape|WebEscape]]

## 要点
- **基础开发流程**：proto 文件中通过 `option cc_generic_services = true;` 定义 [[concepts/protobuf服务定义|protobuf服务定义]]，protoc 生成 Service 基类后继承实现回调 → 通过 `Server.AddService()` 插入到 [[concepts/brpcserver|brpc::Server]] → `Server.Start(port, options)` 启动监听。
- **RAII 与 done 调用**：[[entities/closureguard|ClosureGuard]] 是核心安全机制，强烈建议在 Service 回调开头构造 `done_guard(done)`，以确保无论成功失败 `done->Run()` 都会被调用一次（[[concepts/raii|RAII]] 模式）；[[concepts/异步service|异步Service]] 的最后一行需 `done_guard.release()` 避免重复调用。注意：Service 的 done 由框架创建，Channel 的 done 由用户创建，二者**不可混淆**。
- **三种线程私有数据**：[[concepts/session-local-data|session-local data]] 绑定一次 RPC（进出 service + done），[[concepts/server-thread-local-data|server-thread-local data]] 绑定一次 service 回调（不依赖 Controller），[[concepts/bthread-local|bthread-local]] 是通用机制但 brpc server 中 bthread 退出时不删除而是回收到 pool 复用；异步 Service 的 done 中只能用 session-local。
- **并发控制**：[[concepts/最大并发控制|最大并发控制]] 支持 server 级与 method 级，超过限制立即返回 [[concepts/elimit|ELIMIT]] 让 client 重试；method 级可设 `"auto"` 启用 [[concepts/自适应限流算法|自适应限流算法]]。
- **pthread 模式**：开启 gflag `-usercode_in_pthread` 可让用户代码运行在 pthread（用于 JNI 等 bthread 不支持的场景），但性能下降且为硬限线程资源。
- **多协议支持**：[[concepts/brpcserver|brpc::Server]] 自动协商协议（[[concepts/baidu_std|baidu_std]]、[[concepts/streaming_rpc|streaming_rpc]]、http/1.0/1.1、h2/gRPC、RTMP、hulu_pbrpc、sofa_pbrpc 等），一个 listen 端口可承载多种协议；[[concepts/nshead_service|nshead_service]] 系列协议需显式开启。
- **SSL 与安全**：[concepts/ssl|SSL] 通过 [[concepts/serverssloptions|ServerSSLOptions]] 开启，作用于 Socket 层故所有协议均支持；[[concepts/sni|SNI]] 与 [[concepts/alpn|ALPN]] 扩展支持多证书与协议协商；基于连接的 [[concepts/身份验证|身份验证]] 通过实现 `Authenticator` 接入，结果存于 [[concepts/authcontext|AuthContext]]；内置服务（如 /status）应通过 internal_port、nginx URL 映射或 `has_builtin_services = false` 保护；外部 URL 应使用 [[concepts/webescape|WebEscape]] 转义。
- **内存管理**：[[concepts/rpc-protobuf-message-factory|RPC Protobuf message factory]] 默认使用 [[entities/defaultrpcpbmessagefactory|DefaultRpcPBMessageFactory]]（new/delete），可替换为 [[concepts/protobuf-arena|protobuf arena]] 实现以提升性能（自 Protobuf v3.14.0 起默认开启 arena）。
- **生命周期管理**：[[concepts/brpcserver|brpc::Server]] 优雅退出（[[concepts/优雅退出|graceful shutdown]]）依靠 `Stop()`（不阻塞）+ `Join()`（阻塞）的拆分，退出时对新请求回复 [[concepts/elogoff|ELOGOFF]]；`RunUntilAskedToQuit()` 简化 Ctrl-C 等待逻辑。**不支持随意 fork without exec**，必须发生在所有 Server/Channel 初始化之前。
- **Controller 能力**：[concepts/brpccontroller|brpc::Controller] 提供 `remote_side()`/`local_side()`（[concepts/butilendpoint|butil::EndPoint]）、`http_request()`、`session_local_data()`、`auth_context()`、`protocol()` 等方法；调用 `SetFailed()` 可标记失败并自动设置 HTTP status-code。
- **关键限制**：[concepts/限制最大消息|限制最大消息] 由 `-max_body_size` gflag 控制，brpc 已移除 protobuf `CodedInputStream` 的默认 TotalBytesLimit；[[concepts/so_reuseport|SO_REUSEPORT]] 允许多进程共同监听同一端口以分担负载。