---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [other]
aliases:
  - "DoNothing()"
  - "brpc::DoNothing()"
---


# brpc::DoNothing

## 基本信息
- Type: other
- Source: [[sources/en_client]]

## 描述
brpc::DoNothing() 是 brpc 框架提供的一个工具函数，它返回一个不执行任何操作的闭包，专门用于半同步 RPC 调用模式。当开发者以该闭包作为 `done` 参数发起异步 RPC 时，框架仍会正常完成 RPC 流程，但不会调用任何用户自定义的回调函数。其生命周期完全由 brpc 自身管理，意味着被调用时不会删除关联的 Controller，这一特性至关重要，因为它允许调用线程在 RPC 完成后安全地访问 `Controller.call_id()`。这与典型的用户自定义回调（例如文档中的 `on_rpc_done`）形成鲜明对比——后者通常在完成时删除 Controller 和 Response。

## 相关实体
- 无相关实体

## 相关概念
- [[concepts/semi-synchronous-call|Semi-synchronous call]]
- [[concepts/brpc-join|brpc::Join]]
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/controller|Controller]]

## 来源提及
- brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc. — [[sources/en_client]]
- Note that in above example, we access `controller.call_id()` after completion of RPC, which is safe right here, because DoNothing does not delete controller as in `on_rpc_done` in previous example. — [[sources/en_client]]
- stub2.method2(&cntl2, &request2, &response2, brpc::DoNothing()); — [[sources/en_client]]