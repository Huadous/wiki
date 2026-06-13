---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std|baidu_std]]"]
tags: [other]
aliases:
  - "Chunk Info"
  - "ChuckInfo"
---


# ChunkInfo

## 基本信息
- Type: other
- Source: [[sources/baidu_std|baidu_std]]

## 描述
ChunkInfo 是一个在 baidu_std 协议中定义的 Protobuf 消息类型，用于在 RpcMeta 元数据中描述分块（chunk）传输的相关信息。它通过 RpcMeta 中的 chuck_info 字段（注意原文拼写为 chuck 而非 chunk）引用，支持将较大的数据包分割为多个块进行传输。ChunkInfo 是 baidu_std 协议 Chunk模式 的核心数据结构组成部分。其具体字段定义在源文档中未完整展开，而是通过锚链接指向 Chunk模式 小节进行详细说明。

## 相关实体
- [[entities/rpc-meta|RpcMeta]]

## 相关概念
- [[concepts/chunk模式|Chunk模式]]
- [[concepts/元数据|元数据]]
- [[concepts/包|包]]

## 来源提及
- `optional ChunkInfo chuck_info = 6;` — [[sources/baidu_std|baidu_std]]
- `| chuck_info          | 详见[Chunk模式](#chunk-mode)                 |` — [[sources/baidu_std|baidu_std]]