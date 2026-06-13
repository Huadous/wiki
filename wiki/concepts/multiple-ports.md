---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [method]
aliases:
  - "多端口监听"
  - "多端口服务"
  - "Multiple Ports Architecture"
---


# Multiple Ports

## 定义
Multiple Ports（多端口监听）是brpc Server架构设计中的一个重要限制与特性：单个brpc Server实例只能监听一个服务端口（不包括用于内置服务的 `internal_port`）。如果业务需要监听多个端口，用户必须创建多个独立的Server实例，每个实例绑定不同的端口。多个Server实例会共享同一个工作线程池（worker thread pool）。`internal_port` 作为第二端口仅用于公开内置服务，通常部署在内网管理场景中。

## 关键特征
- **单实例单端口限制**：一个brpc::Server对象只能监听一个服务端口。这是框架的显式设计选择，而非功能缺失。
- **多实例方案**：若要监听N个端口，必须启动N个独立的Server实例。每个实例拥有独立的配置和端口绑定。
- **共享工作线程池**：虽然创建了多个Server实例，但所有实例共享同一个 `bthread` 工作线程池，从而避免线程资源过度消耗。
- **二端口模式**：通过 `ServerOptions.internal_port` 提供第二个监听端口，该端口仅暴露内置服务（如 `/status`、`/vars` 等管理接口），通常仅供内网使用。
- **简化模型**：单端口设计显著简化了Server内部的事件分发、连接管理和资源调度逻辑。

## 应用
- **多协议支持**：当不同客户端需要通过不同端口使用不同协议时（如一个端口提供HTTP服务，另一个端口提供baidu_std协议），可以启动多个Server实例分别监听对应端口。
- **内网管理端口**：使用 `internal_port` 开放仅内网可访问的管理接口（如健康检查、性能指标查看），而主服务端口对外开放业务请求。
- **服务拆分部署**：在微服务架构中，将不同功能模块部署在同一进程的不同端口上，每个模块由独立的Server实例管理，便于分阶段启动和优雅关闭。
- **安全隔离**：通过不同端口绑定不同的认证逻辑或防火墙规则，实现访问权限分层控制。

## 相关概念
- [[concepts/builtin-services|内置服务 (Builtin Services)]]
- [[concepts/idle-timeout-sec|空闲连接超时 (idle_timeout_sec)]]
- [[concepts/bthread|bthread 协程调度]]

## 相关实体
- [[entities/brpc|brpc Server (brpc::Server)]]
- [[entities/bvar|bvar 多维统计库]]

## 来源提及
- "One server can only listen to one port (not counting ServerOptions.internal_port). To listen to N ports, start N servers." — [[brpc/en_server|en_server]]