---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/baidu_std|baidu_std]]"]
tags: [method]
aliases:
  - "Chunk Mode"
  - "块传输模式"
---


# Chunk模式

## 定义
Chunk模式 是 baidu_std 协议中用于处理大块数据传输的方法。该方法通过将大数据包拆分为多个小块（chunk）进行传输，以解决单包过大带来的传输与协议层处理难题。在协议层面，Chunk模式 通过 RpcMeta 中的 `chuck_info` 字段（`ChunkInfo` 类型，字段编号为 6）来描述分块传输的相关元信息。

## 关键特征
- **协议级分块传输机制**：定义于 baidu_std 协议的 RpcMeta 中，作为可选字段携带分块描述信息
- **基于 ChunkInfo 元数据**：使用 `optional ChunkInfo chuck_info = 6` 字段标识分块传输上下文
- **解决大包传输问题**：避免单次 RPC 调用中传输超大消息体（例如大文件、多媒体数据）造成的协议层限制
- **源文档设有专门章节**：协议规范中通过 `#chunk-mode` 锚链接提供详细的拆分与重组说明
- **与标准包传输共存**：作为可选的扩展传输方式，与普通 baidu_std 包传输并存

## 应用
- **大文件传输**：在 RPC 调用中传递超出单包大小限制的文件内容
- **多媒体数据传输**：用于传输音视频、图片等大体积二进制负载
- **附件类负载**：配合 [[concepts/附件|附件]] 概念，作为承载附件数据的传输方式
- **超出默认消息尺寸限制的场景**：当负载超出 baidu_std 默认包大小时，通过 Chunk模式 拆分传输

## 相关概念
- [[concepts/ChunkInfo|ChunkInfo]]
- [[concepts/附件|附件]]
- [[concepts/包|包]]

## 相关实体
- 无相关实体

## 来源提及
- "chuck_info          | 详见[Chunk模式](#chunk-mode)                 |" — [[brpc/baidu_std|baidu_std]]
- "optional ChunkInfo chuck_info = 6;" — [[brpc/baidu_std|baidu_std]]