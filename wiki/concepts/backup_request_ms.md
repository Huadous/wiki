---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request|en_backup_request]]"]
tags: [term]
aliases:
  - "backup_request_ms"
  - "ChannelOptions.backup_request_ms"
---


# backup_request_ms

## 定义
backup_request_ms 是 brpc 中 `ChannelOptions` 的一个毫秒级参数，用于控制备份请求（Backup Request）触发的时机。当请求在指定的毫秒数内未收到响应时，客户端会向另一台服务器发送备份请求，以降低长尾延迟。

## 关键特征
- 是 `ChannelOptions` 中的时间阈值参数，单位为毫秒。
- 触发逻辑：当主请求超过该时间未返回响应时，自动向其他服务器发起备份请求。
- 取值参考依据：建议参考 brpc 提供的默认 CDF（累积分布函数）图，或用户基于自身业务统计的自定义延迟分布来选取。
- 数值与覆盖率关系示例（来自文档示例数据）：
  - `backup_request_ms = 2ms` 时，约可覆盖 95.5% 的请求。
  - `backup_request_ms = 10ms` 时，约可覆盖 99.99% 的请求。
- 取值权衡：较小的值能更早触发备份请求以降低延迟，但会增加后端服务器压力；较大的值则减少后端压力，但可能在更长时间内承受单点慢请求的影响。

## 应用
- 在对延迟敏感且后端服务具备冗余副本的 RPC 调用场景中，通过合理设置 `backup_request_ms` 平衡可用性与后端负载。
- 根据业务实际的请求延迟分布（参考 CDF 图或自采数据）选择合适的阈值。
- 作为 brpc 备份请求机制中的关键调参项，常用于优化 P99/P999 等长尾延迟指标。

## 相关概念
- [[concepts/ChannelOptions|ChannelOptions]]
- [[concepts/Backup-Request|Backup Request]]
- [[concepts/CDF|CDF]]
- [[concepts/Channel|Channel]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "when the response is not returned after ChannelOptions.backup_request_ms ms, it sends to another server" — [[sources/en_backup_request|en_backup_request]]
- "Choosing backup_request_ms=2ms could approximately cover 95.5% of the requests, while choosing backup_request_ms=10ms could cover 99.99% of the requests." — [[sources/en_backup_request|en_backup_request]]