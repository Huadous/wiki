---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bthread|bthread]]"]
tags: [project]
aliases:
  - "Distributed Process"
  - "DP"
  - "百度分布式处理项目"
---


# Distributed Process

## 基本信息
- Type: project
- Source: [[sources/bthread|bthread]]

## 描述
Distributed Process（简称DP）是百度内部的一个项目，其中包含 fiber 库。fiber 是一个 N:1 的合作式线程库，其在功能上等价于 event-loop 库，但允许开发者以同步方式编写代码，从而简化异步编程模型。由于纯合作式的 fiber 无法充分利用多核资源，[[entities/bthread|bthread]] 在 fiber 的基础上演进为 M:N 线程模型，成为 brpc 的核心线程库。

## 相关实体
- [[entities/bthread|bthread]]

## 相关概念
- [[concepts/fiber|fiber]]
- [[concepts/m-n-threading|M:N threading]]

## 来源提及
- bthread的前身是Distributed Process(DP)中的fiber，一个N:1的合作式线程库，等价于event-loop库，但写的是同步代码。 — [[sources/bthread|bthread]]