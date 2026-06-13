---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions|editions]]"]
tags: [other]
aliases:
  - "protobuf SearchRequest"
  - "SearchRequest 消息"
---


# SearchRequest

## 基本信息
- Type: other
- Source: [[sources/editions|editions]]

## 描述
SearchRequest 是 Protocol Buffers 语言指南（editions 版）中作为示例定义的一个具体消息类型，用于演示 .proto 文件的基本语法。它包含三个字段：一个名为 `query` 的 string 类型字段表示搜索查询字符串，一个名为 `page_number` 的 int32 类型字段表示请求的结果页码，以及一个名为 `results_per_page` 的 int32 类型字段表示每页返回的结果数量。SearchRequest 在指南中作为第一个完整消息示例出现，用来说明如何声明 edition、定义 `message` 关键字以及为字段指定类型和字段编号。它也是后续讨论 [[entities/searchresponse|SearchResponse]] 的基础，两个消息类型经常成对出现以演示请求-响应模式。

## 相关实体
- [[entities/searchresponse|SearchResponse]]

## 相关概念
- [[concepts/message-type|Message Type]]
- [[concepts/proto-file|.proto file]]
- [[concepts/field-number|Field Number]]
- [[concepts/scalar-value-type|Scalar Value Type]]

## 来源提及
- "Let's say you want to define a search request message format, where each search request has a query string, the particular page of results you are interested in, and a number of results per page. Here's the .proto file you use to define the message type." — [[sources/editions|editions]]
- "The first line of the file specifies that you're using edition 2023 of the protobuf language spec." — [[sources/editions|editions]]