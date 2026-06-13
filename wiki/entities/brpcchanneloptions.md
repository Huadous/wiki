---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/client|client]]"]
tags: [other]
aliases:
  - "ChannelOptions"
---


# brpc::ChannelOptions

## 基本信息
- Type: other
- Source: [[sources/client|client]]

## 描述
brpc::ChannelOptions 是 brpc 中用于初始化 [[entities/brpc-channel|brpc::Channel]] 的配置结构体，定义在 `src/brpc/channel.h` 中。它包含了 Channel 创建时的所有可配置参数，例如协议类型、连接方式、超时时间、最大重试次数、backup request 时间、连接超时、SSL 选项、命名服务过滤器、健康检查选项以及重试策略等。一旦 [[entities/brpc-channel|brpc::Channel]] 初始化成功，ChannelOptions 中的字段便无法再被修改。用户可以在栈上创建 ChannelOptions 对象，传入非默认值，然后调用 `channel.Init(..., &options)`。[[entities/brpc-channel|brpc::Channel]] 本身不会修改 options，Init 结束后也不再访问 options。运行时可通过 `Channel.options()` 获取当前生效的所有选项。

## 相关实体
- [[entities/brpc-channel|brpc::Channel]]
- [[entities/brpc-controller|brpc::Controller]]

## 相关概念
- [[concepts/ssl|SSL]]
- [[concepts/连接方式|连接方式]]
- [[concepts/重试退避|重试退避]]
- [[concepts/备份请求|备份请求]]
- [[concepts/健康检查|健康检查]]
- [[concepts/命名服务过滤器|命名服务过滤器]]

## 来源提及
- 就像大部分类那样，Channel必须在Init之后才能使用，options为NULL时所有参数取默认值，如果你要使用非默认值，这么做就行了： — [[sources/client|client]]
- 注意Channel不会修改options，Init结束后不会再访问options。所以options一般就像上面代码中那样放栈上。Channel.options()可以获得channel在使用的所有选项。 — [[sources/client|client]]