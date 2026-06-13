---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [standard]
aliases:
  - "RetryPolicy"
  - "重试策略接口"
---


# brpc::RetryPolicy

## 定义
brpc::RetryPolicy 是 brpc 框架定义的重试策略接口，用户可以通过继承该接口并实现 `DoRetry` 方法来自定义重试条件。`DoRetry` 方法依据 `brpc::Controller` 中的错误码等信息判断当前请求是否应当进行重试。

## 关键特征
- **可扩展接口**：通过继承 `brpc::RetryPolicy` 并实现 `DoRetry` 方法，用户可完全自定义重试判定逻辑。
- **默认行为**：brpc 默认不重试 http/h2 相关的错误，用户可定制策略使其在特定 HTTP 错误码（如 `HTTP_STATUS_FORBIDDEN (403)`）时重试。
- **生命周期管理**：赋值给 `ChannelOptions.retry_policy` 的 `retry_policy` 必须在 `Channel` 使用期间始终保持有效，`Channel` 不会负责删除该策略对象，因此实际使用中通常以单例模式创建。
- **内置实现**：brpc 提供了 `RpcRetryPolicyWithFixedBackoff`（固定退避重试策略）和 `RpcRetryPolicyWithJitteredBackoff`（带抖动的退避重试策略）两个内置实现。

## 应用
- 为 brpc 客户端配置统一的请求重试行为，应对临时性网络错误或服务端异常。
- 针对 HTTP/H2 协议定制重试逻辑，例如在接收到 403 状态码时触发重试。
- 结合 [[concepts/重试退避|重试退避]] 策略，控制重试间隔与抖动，避免雪崩效应。
- 与 [[concepts/backup request|backup request]] 配合使用，区分主请求与备份请求的重试语义。
- 在不同 [[concepts/连接方式|连接方式]] 下保持一致的重试判定。

## 相关概念
- [[concepts/重试退避|重试退避]]
- [[concepts/backup request|backup request]]
- [[concepts/连接方式|连接方式]]

## 相关实体
- [[entities/brpc::ChannelOptions|brpc::ChannelOptions]]
- [[entities/brpc::Controller|brpc::Controller]]

## 来源提及
- 用户可以通过继承brpc::RetryPolicy自定义重试条件。比如brpc默认不重试http/h2相关的错误，而你的程序中希望在碰到HTTP_STATUS_FORBIDDEN (403)时重试，可以这么做： — [[sources/client|client]]
- // 给ChannelOptions.retry_policy赋值就行了。// 注意：retry_policy必须在Channel使用期间保持有效，Channel也不会删除retry_policy，所以大部分情况下RetryPolicy都应以单例模式创建。 — [[sources/client|client]]