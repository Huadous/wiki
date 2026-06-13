---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std|baidu_std]]"]
tags: [product]
aliases:
  - "Sofa"
  - "Sofa协议实现"
  - "baidu_std Sofa"
---


# Sofa

## 基本信息
- Type: product
- Source: [[sources/baidu_std|baidu_std]]

## 描述
Sofa 是 [[sources/baidu_std|baidu_std]] 协议规范的另一个实现。它已被接口规范委员会分配了序号 101，用于存放其专有的元数据扩展字段。Sofa 与 [[entities/Hulu|Hulu]] 一样，可以自由地使用该序号来添加自定义的扩展字段，而其他不识别该序号字段的实现会将其作为 Unknown 字段忽略，从而在 [[concepts/元数据|元数据]] 层面实现不同实现之间的互不干扰。Sofa 与 [[sources/baidu_std|baidu_std]] 主实现以及其他自定义实现共享同一套协议骨架，但在私有扩展字段上保持独立。

## 相关实体
- [[entities/baidu_std|baidu_std]]
- [[entities/Hulu|Hulu]]

## 相关概念
- [[concepts/RpcMeta|RpcMeta]]
- [[concepts/元数据|元数据]]

## 来源提及
- "101  | Sofa | — baidu_std" — [[sources/baidu_std|baidu_std]]
- "某些实现需要在元数据中增加自己专有的字段。为了避免冲突，并保证不同实现之间相互调用的兼容性，所有实现都需要向接口规范委员会申请一个专用的序号用于存放自己的扩展字段。" — [[sources/baidu_std|baidu_std]]