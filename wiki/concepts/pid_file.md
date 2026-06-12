---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [term]
aliases:
  - "PID文件"
  - "进程ID文件"
---


# pid_file

## 定义
`pid_file` 是 `ServerOptions` 中的一个字段，用于指定一个 PID（进程标识符）文件路径。当该字段非空时，brpc 服务器在启动时会创建该文件，并将当前进程的 PID 写入其中，方便外部脚本或监控系统获取服务器进程 ID。默认值为空字符串，表示不创建 PID 文件。这是一个简单的运维辅助功能，用于进程管理和自动重启等场景。

## 关键特征
- **可选配置**：默认值为空，仅在显式设置非空路径时生效。
- **自动创建和写入**：服务器启动时自动在指定路径创建文件，并写入当前进程 PID。
- **运维辅助**：不参与核心 RPC 逻辑，仅用于外部进程管理工具（如监控、自动重启脚本）获取服务器 PID。
- **单一用途**：文件内容仅为 PID 数字，无额外元数据或格式化信息。

## 应用
- **进程监控**：监控系统通过读取 PID 文件，追踪 brpc 服务器进程是否存活。
- **自动重启**：在服务异常退出时，外部调度工具通过 PID 文件标识目标进程，执行重启操作。
- **服务编排**：在容器化或集群管理环境中，PID 文件辅助注册服务进程身份。

## 相关概念
- [[concepts/serveroptions|ServerOptions]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "If this field is non-empty, Server creates a file named so at start-up, with pid as the content. Empty by default." — [[sources/en_server|en_server]]