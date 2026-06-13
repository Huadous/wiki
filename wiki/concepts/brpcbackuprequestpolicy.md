---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [standard]
aliases:
  - "BackupRequestPolicy接口"
  - "备份请求策略接口"
---


# brpc::BackupRequestPolicy

## 定义
brpc::BackupRequestPolicy 是 brpc 提供的备份请求策略接口，用户可以通过继承该接口来自定义备份请求的行为策略。该接口定义了备份请求的发送时机判断、是否发送备份请求的决策逻辑以及 RPC 结束时的回调处理。

## 关键特征
- 接口包含三个核心方法：
  - `GetBackupRequestMs`：返回发送备份请求的时间（毫秒）。
  - `DoBackup`：判断是否应该发送备份请求。
  - `OnRPCEnd`：在 RPC 结束时被调用，用于收集调用信息。
- 用户可通过继承该接口实现自定义策略，例如：
  - 根据延时动态调节 `backup_request_ms`。
  - 根据错误率熔断部分 backup request。
- `ChannelOptions.backup_request_policy` 字段影响该 Channel 上所有 RPC。
- `Controller.set_backup_request_policy()` 可修改某次 RPC 的策略。
- 备份请求策略（`backup_request_policy`）的优先级高于 `backup_request_ms`。

## 应用
- 动态延时调节：根据实时观测到的请求延时，动态调整发送备份请求的等待时间，以在延时与成功率之间取得平衡。
- 错误率熔断：当检测到目标服务错误率升高时，通过策略熔断部分 backup request，避免无效重试加剧下游压力。
- 细粒度控制：在 Channel 级别设置默认策略，同时在 Controller 级别针对特定 RPC 进行策略覆盖，满足多样化的容灾需求。

## 相关概念
- [[concepts/backup-request|backup request]]
- [[concepts/circuit-breaker|熔断]]

## 相关实体
- [[entities/brpc-channel-options|brpc::ChannelOptions]]
- [[entities/brpc-controller|brpc::Controller]]

## 来源提及
- 用户可以通过继承brpc::BackupRequestPolicy自定义策略（backup_request_ms和熔断backup request）。比如根据延时调节backup_request_ms或者根据错误率熔断部分backup request。 — [[sources/client|client]]
- ChannelOptions.backup_request_policy同样影响该Channel上所有RPC。Controller.set_backup_request_policy()可修改某次RPC的策略。backup_request_policy优先级高于backup_request_ms。 — [[sources/client|client]]