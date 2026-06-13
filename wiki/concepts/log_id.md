---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [term]
aliases:
  - "log_id"
  - "log-id"
  - "日志标识符"
---


# log_id

## 定义
log_id 是 brpc 中由 [[concepts/Controller|Controller]] 提供的 64 位整数标识符,通过 `Controller::set_log_id()` 设置。该标识符会随请求一起发送到服务端,并常被打印在服务端日志中,以便关联同一会话中由客户端访问的不同服务。字符串类型的 log-id 在设置前必须先转换为 64 位整数。

## 关键特征
- 数据类型为 64 位整数(`uint64_t`),由客户端设置后随请求体一并发送到服务端。
- 通常由上游服务生成(例如最外层入口服务),用于打通分布式调用链中的日志关联。
- 可被服务端打印至访问日志中,使运维人员能够通过同一个 log_id 串联起跨越多个微服务的调用。
- 若业务侧持有的是字符串形式的 log-id,必须先将其转换为 64 位整数再调用 `set_log_id()`。
- 与 [[concepts/Controller|Controller]] 的生命周期绑定,作为 [[concepts/Controller|Controller]] 上众多可配置字段(超时、重试、附件等)之一。
- 是 brpc 实现分布式追踪与日志串联的基础机制,通常与 [[entities/Channel|Channel]] 配合使用。

## 应用
- **分布式调用链追踪**:在最外层入口服务处生成一个全局唯一的 log_id,并通过请求上下文向下游传递,实现跨服务日志串联。
- **服务端日志关联**:服务端在打印访问日志时附带 `controller->log_id()`,便于按会话检索不同节点产生的日志。
- **问题排查与排障**:当一次用户操作涉及多个服务时,可通过单一 log_id 在海量日志中快速定位整条调用路径。
- **业务会话标识透传**:将业务层的会话 ID、订单号或请求流水号编码为 64 位整数后,作为 log_id 透传至后端,实现业务级与系统级的统一标识。

## 相关概念
- [[concepts/Controller|Controller]]
- [[concepts/Timeout|Timeout]]

## 相关实体
- [[entities/Channel|Channel]]
- [[entities/Controller|Controller]]

## 来源提及
- "set_log_id() sets a 64-bit integral log_id, which is sent to the server-side along with the request, and often printed in server logs to associate different services accessed in a session." — [[sources/en_client|en_client]]
- "String-type log-id must be converted to 64-bit integer before setting." — [[sources/en_client|en_client]]