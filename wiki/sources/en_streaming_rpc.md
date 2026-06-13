---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_streaming_rpc.md]]"
tags: [Streaming RPC, Stream, Flow Control, Head-of-line blocking, StreamOptions, StreamInputHandler, Stream API, baidu_std protocol, 消息边界, 全双工, 空闲超时, 自动分段]
aliases: ["流式 RPC 概述", "Streaming RPC Overview"]
---

# Streaming RPC 概述 - Summary

## 来源
- Original file: [[brpc/en_streaming_rpc.md]]

## 核心内容
本文档介绍了 Apache BRPC 框架中的流式 RPC 通信模型，旨在解决分布式场景下传输大量数据时多次普通 RPC 带来的顺序不可控和延迟问题。[[concepts/streaming-rpc|Streaming RPC]] 允许在客户端和服务端之间建立用户空间的 [[concepts/stream|Stream]] 连接，多个 Stream 可复用同一 TCP 连接，基本传输单元为消息。该模型保证消息顺序、消息边界（[[concepts/消息边界|消息边界]]）、[[concepts/streaming-rpc|streaming-rpc]]通信、[[concepts/流控|流控]]和超时通知，并自动对大消息进行 [[concepts/head-of-line-blocking|head-of-line-blocking]] 以避免 [[concepts/head-of-line-blocking|队头阻塞]]。文档详细描述了 [[concepts/stream-api|Stream API]] 的使用方式，包括 `StreamCreate`、`StreamAccept`、`StreamWrite`、`StreamWait` 和 `StreamClose`，并定义了 [[concepts/streamoptions|StreamOptions]] 配置结构和 [[concepts/streaminputhandler|StreamInputHandler]] 回调接口。当前实现仅支持客户端主动创建 Stream，服务端通过 `StreamAccept` 接受连接。

## 关键实体
- [[entities/brpc|Apache BRPC]] — 实现流式 RPC 框架的产品，通过 [[concepts/baidu_std-protocol|baidu_std 协议]] 支持 Stream 通信。

## 关键概念
- [[concepts/streaming-rpc|Streaming RPC]] — 通信模型，支持大量数据的流式传输。
- [[concepts/stream|Stream]] — 用户空间连接的基本抽象，由唯一 `StreamId` 标识。
- [[concepts/流控|流控]] — 基于 `max_buf_size` 的缓冲区限制机制，防止发送方过载。
- [[concepts/head-of-line-blocking|Head-of-line blocking]] — 通过自动分段避免的问题。
- [[concepts/streamoptions|StreamOptions]] — 配置 max_buf_size、idle_timeout_ms、messages_in_batch 和 handler 的结构体。
- [[concepts/streaminputhandler|StreamInputHandler]] — 定义 on_received_messages、on_idle_timeout、on_closed 回调的接口。
- [[concepts/stream-api|Stream API]] — 操作 Stream 的函数集合（创建、接受、读写、关闭）。
- [[concepts/baidu_std-protocol|baidu_std 协议]] — BRPC 默认协议，支持流式通信。
- [[concepts/消息边界|消息边界]] — 保证消息作为独立单元传输的特性。
- [[concepts/streaming-rpc|streaming-rpc]] — 支持双向同时数据传输。
- [[concepts/空闲超时|空闲超时]] — 通过 `on_idle_timeout` 回调通知空闲状态。
- [[concepts/head-of-line-blocking|head-of-line-blocking]] — 自动分割大消息避免队头阻塞。

## 要点
- Streaming RPC 通过 Stream 提供有序、有边界的消息传输，支持全双工和流量控制。
- Stream 由客户端主动创建（`StreamCreate`），服务端被动接受（`StreamAccept`）。
- 发送方通过 `StreamWrite` 写入消息，接收方通过实现 `StreamInputHandler::on_received_messages` 接收消息。
- 流量控制基于 `max_buf_size`：超出后 `StreamWrite` 返回 `EAGAIN`，需调用 `StreamWait` 等待。
- 大消息自动分段以消除队头阻塞问题。
- Stream 关闭后触发 `on_closed` 回调通知双方。