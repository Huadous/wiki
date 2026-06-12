---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [term]
aliases:
  - "VLOG控制服务"
  - "brpc VLOG接口"
---


# /vlog

## 定义
`/vlog` 是 brpc 内置服务中用于查看和动态调整程序中当前可开启的 VLOG（详细日志）模块及其日志级别的 HTTP 接口。它允许开发者在不重启服务的情况下，通过浏览器交互式地控制特定模块的详细日志输出，从而方便线上问题的排查。

## 关键特征
- **动态控制**：允许在运行时启用或禁用特定模块的 VLOG，无需重启服务进程。
- **模块化可见性**：展示所有支持 VLOG 的模块及其当前日志级别，便于开发者识别可调试的组件。
- **交互式界面**：通过浏览器可查看可用 VLOG 模块列表，并支持交互操作（如调整模块日志级别）。
- **框架特定性**：仅适用于 brpc 的流式日志系统，对 glog 无效。

## 应用
- **线上问题排查**：在生产环境中，动态开启某个模块的详细日志，捕获偶发问题的调试信息。
- **模块调试**：在开发和测试阶段，快速定位特定模块的日志输出，验证代码逻辑。
- **运维管理**：作为 brpc 内置监控系统的一部分，与 `/health`、`/version` 等服务配合使用，形成微服务可观测性方案。

## 相关概念
- [[concepts/builtin_service|内置服务]]
- [[concepts/version|/version]]
- [[concepts/health|/health]]
- [[concepts/protobufs|/protobufs]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "/vlog: 查看程序中当前可开启的VLOG（对glog无效）。" — [[sources/builtin_service|builtin_service]]
- "作为其他服务之一，/vlog帮助在不重启服务的情况下开启特定模块的调试日志，极大方便了线上问题排查。" — [[sources/builtin_service|builtin_service]]