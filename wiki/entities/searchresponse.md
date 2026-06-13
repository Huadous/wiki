---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions]]"]
tags: [other]
aliases:
  - "protobuf SearchResponse"
  - "SearchResponse message"
---


# SearchResponse

## 基本信息
- Type: other
- Source: [[sources/editions]]

## 描述
SearchResponse 是 Protocol Buffers Editions 语言指南中与 [[entities/searchrequest|SearchRequest]] 配对使用的示例消息类型，用于演示如何在同一个 [[concepts/proto-file|.proto file]] 中定义多个相关消息类型。它代表对应于 SearchRequest 的搜索响应消息格式，在指南的"Adding More Message Types"一节中被引用，作为展示多消息类型组合模式的示例。虽然指南中未展示其具体字段定义，但通过示例说明了如何将回复消息添加到与 SearchRequest 相同的文件中。该消息类型也被用于说明将多个相关消息放在同一文件中可能带来的依赖膨胀问题，因此建议每个 .proto 文件只包含尽量少的类型。

## 相关实体
- [[entities/searchrequest|SearchRequest]]

## 相关概念
- [[concepts/message-type|Message Type]]
- [[concepts/proto-file|.proto file]]
- [[concepts/enum|Enum]]

## 来源提及
- "Multiple message types can be defined in a single .proto file. This is useful if you are defining multiple related messages – so, for example, if you wanted to define the reply message format that corresponds to your SearchResponse message type, you could add it to the same .proto" — [[sources/editions]]
- "if you wanted to define the reply message format that corresponds to your SearchResponse message type, you could add it to the same .proto" — [[sources/editions]]