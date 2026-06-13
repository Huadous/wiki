---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [method]
aliases:
  - "ProgressiveReader"
  - "渐进式读取"
  - "持续下载"
---


# ProgressiveReader

## 定义
ProgressiveReader 是 [[entities/brpc|brpc]] 提供的用于持续下载超长或无限长 HTTP body（如直播 flv 文件）的接口机制。标准 HTTP 客户端必须等待 body 完整下载后才结束 RPC，过程中 body 会持续驻留在内存中，容易导致内存持续增长。ProgressiveReader 允许客户端在读完 header 部分后就结束 RPC，让用户在 RPC 结束后持续读取仍在增长的 body。

## 关键特征
- **提前结束 RPC**：客户端可在 header 读取完成后立即返回 RPC，不必等待 body 全部下载完成。
- **持续读取 body**：RPC 结束后用户可继续从持续增长的 body 中增量读取数据。
- **回调式接口**：用户实现 `ProgressiveReader` 接口，其中 `OnReadOnePart` 在每段数据到达时被调用，`OnEndOfMessage` 在数据结束或连接断开时被调用。
- **显式声明**：通过 `cntl.response_will_be_read_progressively()` 通知框架本次响应将采用渐进式读取模式。
- **流式启动**：RPC 结束后调用 `cntl.ReadProgressiveAttachmentBy()` 启动后台流式读取流程。
- **与 chunked mode 正交**：该功能解决的是"如何让用户处理超长或无限长 body"的问题，与 HTTP body 是否以 chunked mode 传输无关，brpc 的 HTTP 实现一直支持解析 chunked mode。

## 应用
- **直播流媒体下载**：持续下载直播中的 flv、hls 等无限增长的多媒体流。
- **大文件增量处理**：在不将整个文件缓存到内存的前提下，逐步处理超长 HTTP body。
- **实时数据流消费**：服务端持续推送事件或日志、客户端边收边处理的场景。
- **长时间运行的 HTTP 长连接**：需要长时间保持连接并持续消费响应的客户端场景。

## 相关概念
- [[concepts/streaming-rpc|Streaming RPC]]
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/channel|Channel]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- brpc client支持在读取完body前就结束RPC，让用户在RPC结束后再读取持续增长的body。注意这个功能不等同于"支持http chunked mode"，brpc的http实现一直支持解析chunked mode，这里的问题是如何让用户处理超长或无限长的body，和body是否以chunked mode传输无关。 — [[sources/http_client|http_client]]
- OnReadOnePart在每读到一段数据时被调用，OnEndOfMessage在数据结束或连接断开时被调用，实现前仔细阅读注释。 — [[sources/http_client|http_client]]