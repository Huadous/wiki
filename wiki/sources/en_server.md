---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_server.md]]"
tags: [Protocol Buffers, 同步服务, 异步服务, RAII, ClosureGuard, 限流, 数据局部存储, baidu_std协议, bthread, SSL/TLS, Authenticator, pthread模式, AutoConcurrencyLimiter, Protobuf Arena, HTTP/2, gRPC, ServerOptions, Butil.EndPoint, DataFactory, HealthReporter, json2pb, 流式RPC, Compression, Attachment, Builtin Services, ServiceOwnership, max_body_size, idle_timeout_sec, Protocol Auto-detection, Version, ELIMIT, Multiple Ports, Security Configuration, google::protobuf::Closure, fork without exec, ELOGOFF, eovercrowded, SO_REUSEPORT, nova_pbrpc, nshead_mcpack, RTMP, public_pbrpc, bvar]
aliases: ["brpc 服务器端文档", "brpc 服务端教程"]
---

# brpc Server 使用教程 - Summary

## 来源
- Original file: [[brpc/en_server.md]]
- Ingested: 2026-06-12

## 核心内容
本文档是 Apache [[entities/brpc|brpc]] 框架的服务器端使用指南，详细说明了如何创建和运行 RPC 服务。内容涵盖：从定义 `.proto` 文件、实现 protobuf 服务接口、将服务添加到 `brpc::Server`、启动和停止服务器，到各种高级设置（如 SSL、限流、身份验证、协议支持等）。文档还解释了[[concepts/同步服务|同步服务]]与[[concepts/异步服务|异步服务]]的区别、[[concepts/raii|RAII]] 技巧（如[[concepts/closureguard|ClosureGuard]]）、以及多种[[concepts/数据局部存储|数据局部存储]]机制。此外，提供了协议支持列表、常见问题解答和服务器端工作流程图，是开发基于 brpc 的服务器的权威参考。

## 关键实体
- [[entities/brpc|brpc]]：Apache 软件基金会下的高性能 RPC 框架，核心产品
- [[entities/brpc-server|brpc Server]]：框架中用于承载 RPC 服务的核心类
- [[entities/brpccontroller|brpc::Controller]]：服务器端编程中用于传递元数据的核心接口
- [[entities/nginx|nginx]]：高性能反向代理服务器，可用于保护内置服务
- [[entities/curl|curl]]：用于测试 HTTP+JSON 接口的命令行工具
- [[entities/hulu_pbrpc协议|hulu_pbrpc协议]]：默认启用的外部 RPC 协议
- [[entities/sofa_pbrpc协议|sofa_pbrpc协议]]：默认启用的外部 RPC 协议

## 关键概念
- [[concepts/protocol-buffers|Protocol Buffers]]：定义服务接口和消息格式的标准
- [[concepts/同步服务|同步服务]]与[[concepts/异步服务|异步服务]]：两种服务实现模式
- [[concepts/raii|RAII]]与[[concepts/closureguard|ClosureGuard]]：资源管理和回调执行机制
- [[concepts/限流|限流]]：通过 `max_concurrency` 控制的并发保护机制
- [[concepts/数据局部存储|数据局部存储]]：session-local、server-thread-local、bthread-local 三种机制
- [[concepts/bthread|bthread]]：brpc 的轻量级协程实现
- [[concepts/protocol-auto-detection|协议自动检测]]：同一端口自动识别多种协议
- [[concepts/ssltls|SSL/TLS]]与[[concepts/authenticator|Authenticator]]：安全与认证机制
- [[concepts/builtin-services|Builtin Services]]：内置的诊断和管理 HTTP 接口
- [[concepts/serveroptions|ServerOptions]]：服务器配置结构体
- [[concepts/baidu_std协议|baidu_std协议]]：百度内部标准 RPC 协议
- [[concepts/http2|HTTP/2]]与[[concepts/grpc|gRPC]]：现代通信协议支持

## 要点
- 在 `.proto` 文件中定义服务接口，通过 protoc 生成 C++ 代码
- 实现服务接口时，必须正确处理 `done->Run()`，推荐使用 ClosureGuard 确保资源释放
- 同步服务在 CallMethod 返回前完成处理，异步服务将 done 保存到后续事件
- brpc Server 支持添加多个服务，且可以在同一端口上自动检测多种协议
- 服务器限流（max_concurrency）可防止过载，提供服务器级和方法级两种设置
- 提供三种局部存储机制：session-local、server-thread-local、bthread-local
- 支持 SSL、身份验证、压缩、附件等功能
- pthread 模式用于兼容不支持 bthread 的代码（如 JNI）
- fork 无 exec 的情况需要特殊注意，建议在初始化所有 Server/Channel 前进行
- 内置服务可通过 internal_port 隐藏，或通过配置关闭特定内置服务