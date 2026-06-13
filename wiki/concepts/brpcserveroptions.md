---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|server]]"]
tags: [term]
aliases:
  - "ServerOptions"
  - "brpc ServerOptions"
  - "brpc::ServerOptions"
---


# brpc::ServerOptions

## 定义

`brpc::ServerOptions` 是 brpc 中用于配置 `[[brpc/server|brpc::Server]]` 的选项结构体，封装了服务器启动前可定制的一系列参数。用户在调用 `Server::Start()` 之前构造一个 `ServerOptions` 实例并设置其字段，以覆盖默认行为；当传入 `NULL` 给服务器时，所有参数取默认值。

## 关键特征

- **工作线程数提示**：`num_threads` 字段设定服务器工作线程数，默认值为 CPU 核数（含超线程核心）。
- **并发度控制**：
  - `max_concurrency`：服务器级别的最大并发度，默认值 `0` 表示不限制。
  - `method_max_concurrency`：method 级别的最大并发限制，可对单个方法做更细粒度控制。
- **内部端口**：`internal_port` 可设定为仅允许内网访问的端口，用于内置服务（如 status、vars、threads 等），将管理面与对外服务面分离。
- **身份验证**：`auth` 字段接受一个 `Authenticator` 实例，用于启用服务器端身份验证。
- **SSL/TLS 支持**：`ssl_options` 字段类型为 `[[concepts/ServerSSLOptions|ServerSSLOptions]]`，用于配置 TLS 加密通信。
- **进程标识**：`pid_file` 用于将服务器进程 ID 写入指定文件。
- **数据工厂**：
  - `session_local_data_factory`：为每个连接（session）创建独立的本地数据，参见 [[concepts/session-local data|session-local data]]。
  - `thread_local_data_factory`：为每个工作线程创建独立的线程本地数据，参见 [[concepts/server-thread-local data|server-thread-local data]]。
  - `rpc_pb_message_factory`：用于定制 protobuf 消息的创建行为，默认实现为 `[[entities/defaultrpcpbmessagefactory|Default RpcPBMessageFactory]]`。
- **默认行为**：当 `options` 参数为 `NULL` 时，所有字段取默认值。

## 应用

- **默认场景**：直接以默认配置启动服务器，无需构造 `ServerOptions` 实例。
- **高并发服务**：通过调整 `num_threads` 与 `max_concurrency` 优化吞吐量与资源占用。
- **精细化限流**：在 method 级别设置 `method_max_concurrency`，保护热点方法不被过载。
- **内网管理面分离**：将 `internal_port` 配置为仅监听内网 IP，对外仅暴露业务端口，提高安全性。
- **启用认证与加密**：通过 `auth` 与 `ssl_options` 字段部署鉴权与 TLS，满足安全合规需求。
- **多服务隔离**：使用 `pid_file` 配合进程监控工具实现服务生命周期管理。

## 相关概念

- [[brpc/server|brpc::Server]]
- [[concepts/最大并发控制|最大并发控制]]
- [[concepts/session-local data|session-local data]]
- [[concepts/server-thread-local data|server-thread-local data]]
- [[concepts/身份验证|身份验证]]
- [[concepts/ServerSSLOptions|ServerSSLOptions]]

## 相关实体

- [[entities/defaultrpcpbmessagefactory|Default RpcPBMessageFactory]]

## 来源提及

- "options为NULL时所有参数取默认值" — [[sources/server|server]]
- "ServerOptions.num_threads即可，默认是cpu core的个数（包含超线程的）。" — [[sources/server|server]]
- "设置ServerOptions.max_concurrency，默认值0代表不限制。" — [[sources/server|server]]
- "把ServerOptions.internal_port设为一个仅允许内网访问的端口。" — [[sources/server|server]]