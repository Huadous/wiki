---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/proto3]]"]
tags: [method]
aliases:
  - "字段删除方法"
  - "Deleting Fields Procedure"
  - "field deletion procedure"
---


# Deleting Fields

## 定义
Deleting Fields 是 proto3 消息类型中用于安全移除字段的标准操作方法。当某个字段不再需要,并且所有客户端代码中的引用均已删除时,可从消息中删除该字段定义。但必须将被删除字段的字段编号加入 reserved 列表,以防止未来被复用;同时应保留字段名称,以保证 JSON 和 TextFormat 编码能够继续解析旧消息。

## 关键特征
- 必须先清除客户端代码中对该字段的所有引用,才能执行删除操作
- 被删除字段的字段编号必须通过 `reserved` 声明保留,避免被未来开发者误用
- 被删除字段的名称也应通过 `reserved` 声明保留,以保持对旧消息的兼容解析
- 不正确的字段删除会导致严重的兼容性问题,包括数据损坏与 PII(个人身份信息)泄露
- 复用过期的字段编号是引发上述问题的根本原因

## 应用
- 在 proto3 消息的迭代演进过程中,移除已废弃的业务字段
- 防止新字段无意中复用旧字段编号,避免 wire format 不兼容
- 保留已删除字段名称以确保 JSON 和 TextFormat 编码对历史消息的解析能力
- 配合 [[concepts/Reserved-Field-Numbers|Reserved Field Numbers]] 与 [[concepts/Reserved-Field-Names|Reserved Field Names]] 共同实施消息演进策略

## 相关概念
- [[concepts/Reserved-Field-Numbers|Reserved Field Numbers]]
- [[concepts/Reserved-Field-Names|Reserved Field Names]]
- [[concepts/Field-Number|Field Number]]
- [[concepts/Message-Type|Message Type]]

## 相关实体
No related entities

## 来源提及
- "Deleting fields can cause serious problems if not done properly." — [[sources/proto3|proto3]]
- "When you no longer need a field and all references have been deleted from client code, you may delete the field definition from the message. However, you must reserve the deleted field number. If you do not reserve the field number, it is possible for a developer to reuse that number in the future." — [[sources/proto3|proto3]]