---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/en_backup_request.md]]"
tags: [Backup Request, Channel, ChannelOptions, backup_request_ms, SelectiveChannel, Naming Service, CDF, bvar::LatencyRecorder, Asynchronous RPC, /rpcz]
aliases: ["brpc Backup Request Mechanism", "brpc 备份请求机制"]
---

# brpc 备份请求 (Backup Request) 机制 - Summary

## 来源
- Original file: [[brpc/en_backup_request.md]]
- Ingested: 2026-06-13

## 核心内容
本文档介绍了 [[entities/brpc|brpc]] 框架中用于保障服务可用性的**备份请求 (Backup Request)** 机制。当后端服务器可通过 [[concepts/naming-service|命名服务]] 挂载时，[[concepts/channel|Channel]] 会在发送请求后等待 [[concepts/backup_request_ms|backup_request_ms]] 毫秒，若未收到响应则向另一台服务器发送备份请求，最终采用最先返回的响应。文档建议参考 [[entities/brpc|brpc]] 提供的默认 [[concepts/cdf|CDF]] 图或通过 [[concepts/bvarlatencyrecorder|bvar::LatencyRecorder]] 自定义的延迟分布来选取合适的参数值，例如 2ms 约可覆盖 95.5% 请求，10ms 约可覆盖 99.99% 请求。当后端无法通过命名服务挂载时，文档推荐使用 [[concepts/selectivechannel|SelectiveChannel]] 在两个子 Channel 之间互为备份。文档还提及并明确**不推荐**使用「双 [[concepts/asynchronous-rpc|异步 RPC]] + 互取消」方案，因其会无条件发送两次请求而使后端压力翻倍。

## 关键实体
- [[entities/brpc|brpc]] —— Apache 旗下高性能 RPC 框架，本文档的核心主题
- [[entities/bvar|bvar]] —— brpc 生态中的监控与统计 C++ 库，提供 LatencyRecorder 等工具
- [[entities/vars|vars]] —— brpc 内置的 HTTP 监控端点，自动暴露 bvar 记录的统计数据
- [[entities/examplebackup_request_c++|examplebackup_request_c++]] —— 演示 Channel 级别 backup_request_ms 配置行为的 C++ 示例
- [[entities/exampleselective_echo_c++|exampleselective_echo_c++]] —— 演示 SelectiveChannel 在两个子通道间实现备份的 C++ 示例
- [[entities/examplecancel_c++|examplecancel_c++]] —— 演示「双异步 RPC 互相取消」的不推荐方案

## 关键概念
- [[concepts/backup-request|backup-request]] —— brpc 中用于保障可用性的核心机制
- [[concepts/channel|channel]] —— brpc 中客户端与服务端通信的核心抽象
- [[concepts/channeloptions|channeloptions]] —— 用于配置 Channel 行为的选项集合
- [[concepts/backup_request_ms|backup_request_ms]] —— 控制备份请求触发时机的毫秒级参数
- [[concepts/selectivechannel|selectivechannel]] —— 用于跨命名服务场景的通道类型
- [[concepts/naming-service|naming-service]] —— 后端服务器的挂载与服务发现机制
- [[concepts/cdf|cdf]] —— 累积分布函数图，用于辅助选择 backup_request_ms
- [[concepts/bvarlatencyrecorder|bvarlatencyrecorder]] —— 自定义延迟统计的记录器
- [[concepts/asynchronous-rpc|asynchronous-rpc]] —— 文档中作为不推荐替代方案提及
- [[concepts/rpcz|rpcz]] —— brpc 用于展示 RPC 调用详细信息的内省端点

## 要点
- brpc 的备份请求机制通过 [[concepts/channeloptions|channeloptions]] 中的 [[concepts/backup_request_ms|backup_request_ms]] 控制：等待指定毫秒数后未收到响应即向另一台服务器发送请求，以最快返回的响应为准。
- 合理设置 [[concepts/backup_request_ms|backup_request_ms]] 可使绝大多数请求只发送一次，避免对后端服务造成额外压力。
- 建议参考 [[concepts/cdf|CDF]] 延迟分布图来选取参数，例如 2ms 约可覆盖 95.5% 请求，10ms 约可覆盖 99.99% 请求。
- 后端可在 [[concepts/naming-service|命名服务]] 中挂载时，使用普通 [[concepts/channel|Channel]] + backup_request；无法挂载时推荐使用 [[concepts/selectivechannel|SelectiveChannel]] 实现两个子通道间互为备份。
- **不推荐**通过双 [[concepts/asynchronous-rpc|异步 RPC]] 互相取消的方式实现备份请求，因其会始终发送两次请求而使后端压力翻倍。