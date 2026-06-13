---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [standard]
aliases:
  - "nshead"
  - "NsheadMessage"
  - "PROTOCOL_NSHEAD_CLIENT"
  - "PROTOCOL_NSHEAD_MCPACK"
---


# PROTOCOL_NSHEAD

## 定义
PROTOCOL_NSHEAD 是 brpc 中用于发送 NsheadMessage 的协议标识符，其字符串形式为 `"nshead"`。它是 brpc 兼容百度历史 nshead 协议体系的标准协议类型，属于 brpc 客户端 `ChannelOptions::protocol` 字段可取的合法取值之一。

## 关键特征
- 协议字符串取值为 `"nshead"`，对应的枚举常量名为 `PROTOCOL_NSHEAD`
- 专用于发送 `NsheadMessage` 类型的消息
- 默认使用 **pooled connection**（连接池）作为底层连接方式
- 存在两个变体：
  - **`PROTOCOL_NSHEAD_CLIENT`**（字符串 `"nshead_client"`）：baidu-rpc-ub 中 `UBXXXRequest` 请求所需，默认使用 pooled connection
  - **`PROTOCOL_NSHEAD_MCPACK`**（字符串 `"nshead_mcpack"`）：即 nshead + mcpack 的组合，负载由 mcpack2pb 转换为 protobuf 进行解析，默认使用 pooled connection
- 三个变体（`PROTOCOL_NSHEAD`、`PROTOCOL_NSHEAD_CLIENT`、`PROTOCOL_NSHEAD_MCPACK`）一致地默认采用 pooled connection，构成 brpc 兼容百度历史协议体系的关键组成

## 应用
- 在百度内部历史业务（如 baidu-rpc-ub）中使用 `UBXXXRequest` 与后端服务通信时，应将 `ChannelOptions.protocol` 设为 `PROTOCOL_NSHEAD_CLIENT`
- 在需要以 nshead 协议封装、但负载使用 mcpack 编码（后端可通过 mcpack2pb 解析为 protobuf）的场景，应选择 `PROTOCOL_NSHEAD_MCPACK`
- 在通用的 nshead 消息发送场景下，应使用 `PROTOCOL_NSHEAD`
- 与 brpc 的 `Channel` 配合配置，常用于接入遗留 nshead 服务或跨协议互通场景

## 相关概念
- [[concepts/connection-type|Connection Type]]
- [[concepts/channeloptions|ChannelOptions]]

## 相关实体
- [[entities/channel|Channel]]
- [[entities/controller|Controller]]

## 来源提及
- "PROTOCOL_NSHEAD or "nshead", which is required by sending NsheadMessage, using pooled connection by default." — [[sources/en_client|en_client]]
- "PROTOCOL_NSHEAD_CLIENT or "nshead_client", which is required by UBXXXRequest in baidu-rpc-ub, using pooled connection by default." — [[sources/en_client|en_client]]
- "PROTOCOL_NSHEAD_MCPACK or "nshead_mcpack", which is as the name implies, nshead + mcpack (parsed by protobuf via mcpack2pb), using pooled connection by default." — [[sources/en_client|en_client]]