---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request]]"]
tags: [term]
aliases:
  - "ChannelOptions"
  - "brpc ChannelOptions"
  - "Channel 选项"
---


# ChannelOptions

## 定义
ChannelOptions 是 [[entities/brpc|brpc]] 中用于配置 Channel 行为的选项集合（option set）。其中的 `backup_request_ms` 参数是实现 [[concepts/backup-request|Backup Request]] 机制的关键参数，用于控制客户端在等待首个响应多长时间（毫秒）之后，若仍未收到响应则向另一台服务器发起备份请求。ChannelOptions 同时被普通 [[concepts/channel|Channel]] 和 [[concepts/selectivechannel|SelectiveChannel]] 所使用。

## 关键特征
- 以选项集合（option set）的形式对 Channel 的运行时行为进行配置
- 包含 `backup_request_ms` 等关键参数，用以控制备份请求的触发时机
- `backup_request_ms` 的语义为：客户端等待首个响应超过该毫秒数后，即触发备份请求逻辑
- 在普通 Channel 中：当响应未在该毫秒数内返回时，向另一台服务器发送备份请求
- 在 SelectiveChannel 中：当响应未在该毫秒数内返回时，访问（visit）另一个 sub channel
- 对普通 Channel 与 SelectiveChannel 均适用，具有一致的配置语义

## 应用
- 在 brpc 客户端中启用与调优 [[concepts/backup-request|Backup Request]] 机制，以降低长尾延迟
- 通过设置合适的 `backup_request_ms` 阈值，在延迟敏感场景下提前向备机发送请求，从而提升 P99/P999 等尾部延迟指标
- 配合 [[concepts/load-balancing|负载均衡]] 策略，选择合适的备份目标服务器
- 在使用 [[concepts/selectivechannel|SelectiveChannel]] 时，为各 sub channel 配置统一的备份请求触发时间

## 相关概念
- [[concepts/channel|Channel]]
- [[concepts/selectivechannel|SelectiveChannel]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/backup-request-ms|backup_request_ms]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server" — [[sources/en_backup_request]]
- "If the response is not returned after channelOptions.backup_request_ms ms, then another sub channel is visited." — [[sources/en_backup_request]]