---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request]]"]
tags: [project]
aliases:
  - "cancel_c++ 示例"
  - "brpc cancel_c++ 示例"
---


# example/cancel_c++

## 基本信息
- Type: project
- Source: [[sources/en_backup_request]]

## 描述
example/cancel_c++ 是 [[entities/brpc|brpc]] 仓库中的一个 C++ 代码示例项目，展示了"取最快响应"（race two requests）的一种实现模式：通过发起两个异步 RPC 调用，并在各自的 done callback 中互相取消对方，以保留先返回的那个响应。该示例在 brpc 的备份请求文档中被明确标记为 **Not Recommended**（不推荐），因为程序在每次调用时都会无条件地发出两个请求，给后端服务带来双倍压力，无论从延迟、带宽还是服务端负载的角度来看都不经济，应当尽量避免。

文档指出，真正推荐的做法是使用 [[entities/brpc|brpc]] Channel 内置的 `backup_request` 机制，或者更进一步的 [[concepts/selective-channel|SelectiveChannel]]，后者仅在主请求耗时超过阈值时才发送备份请求，"在大多数情况下只发一个请求"，从而显著降低对后端服务的压力。example/cancel_c++ 因此在文档中主要起到反面教材的作用，用于对比和衬托 `backup_request` 与 SelectiveChannel 的优势。

## 相关实体
- [[entities/brpc]]

## 相关概念
- [[concepts/asynchronous-rpc|Asynchronous RPC]]
- [[concepts/backup-request|Backup Request]]

## 来源提及
- "Issue two asynchronous RPC calls and join them. They cancel each other in their done callback. An example is in example/cancel_c++." — [[sources/en_backup_request]]
- "The problem of this method is that the program always sends two requests, doubling the pressure to back-end services. It is uneconomical in any sense and should be avoided as much as possible." — [[sources/en_backup_request]]