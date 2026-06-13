---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_iobuf]]"]
tags: [project]
aliases:
  - "Kylin 项目"
  - "Apache Kylin"
---


# Kylin

## 基本信息
- Type: project
- Source: [[sources/en_iobuf]]

## 描述
Kylin 是文档中提及的一个先前项目，其中实现了 [[concepts/bufhandle|BufHandle]] 数据结构。在 brpc 的 [[sources/en_iobuf|en_iobuf]] 文档中，作者将 Kylin 的 BufHandle 与 [[concepts/iobuf|IOBuf]] 进行对比，指出 BufHandle 封装不佳，将内部结构直接暴露给使用者，用户必须谨慎处理 [[concepts/reference-counting|引用计数]]，因而容易出错并导致 bug。这一对比旨在凸显 IOBuf 在封装便利性与内存安全方面的设计优势。Kylin 在该文档中仅作为历史参照项目出现，并未展开描述其整体架构或功能。

## 相关实体
无相关实体。

## 相关概念
- [[concepts/iobuf|IOBuf]]
- [[concepts/bufhandle|BufHandle]]
- [[concepts/reference-counting|Reference counting]]

## 来源提及
- "If you've used the BufHandle in Kylin before, you should notice the convenience of IOBuf: the former one is badly encapsulated, leaving the internal structure directly in front of users, who must carefully handle the referential countings, very error prone and leading to bugs." — [[sources/en_iobuf|en_iobuf]]