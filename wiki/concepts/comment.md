---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions|editions]]"]
tags: [term]
aliases:
  - ".proto 注释"
  - "proto file comments"
  - "Comment"
---


# Comment

## 定义
Comment（注释）是 .proto 文件中用于添加代码文档的语法元素，属于 .proto 文件语言语法的一部分。它允许开发者为消息定义、字段及其他代码元素附加说明性文字，以提升可读性并促进团队协作。

## 关键特征
- 支持两种注释语法：C/C++/Java 风格的行尾注释 `//`，以及 C 风格的内联/多行注释 `/* ... */`
- 指南推荐优先使用 `//` 注释，并将其放在 .proto 代码元素的前一行
- 多行注释推荐使用 `*` 作为边距线以保持格式美观
- 属于 .proto 语言语法的一部分，非可选装饰

## 应用
- 为消息定义添加语义说明，便于团队理解字段用途
- 在大型 .proto 文件中划分模块或功能区域，提高可维护性
- 自动生成文档的辅助手段（部分工具可提取注释生成 API 文档）
- 标记字段的取值约束或业务规则，减少沟通成本

## 相关概念
- [[concepts/.proto-file|.proto file]]
- [[concepts/message-type|Message Type]]

## 相关实体
- [[entities/searchrequest|searchrequest]]
- [[entities/searchresponse|searchresponse]]

## 来源提及
- "To add comments to your .proto files:" — [[sources/editions|editions]]
- "Prefer C/C++/Java line-end-style comments '//' on the line before the .proto code element" — [[sources/editions|editions]]
- "C-style inline/multi-line comments '/* ... */' are also accepted." — [[sources/editions|editions]]
- "When using multi-line comments, a margin line of '*' is preferred." — [[sources/editions|editions]]
- "* SearchRequest represents a search query, with pagination options to indicate which results to include in the response." — [[sources/editions|editions]]