---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [product]
aliases:
  - "RPC视图工具"
  - "rpc-view"
---


# rpc_view

## 基本信息
- Type: product
- Source: [[sources/builtin_service|builtin_service]]

## 描述
rpc_view 是 [[baidu|百度]][[brpc|brpc框架]] 提供的一个命令行工具，用于在受限网络环境下转发HTTP请求，以访问 brpc 服务器的内置服务。当运行 brpc 服务的端口无法直接访问时（例如百度内网中笔记本无法访问某些端口），用户可以通过 rpc_view 将请求转发到可访问的端口上，从而查看内置服务页面。该工具在 brpc 文档中有专门的页面说明，通常与 brpc 的内置服务配合使用，增强了服务的可调试性。rpc_view 的典型使用场景是在开发或测试阶段绕过端口限制，间接查看服务器的 [[status|/status]] 页面等内部信息。它本身不提供图形界面，而是作为代理转发请求，类似于 [[curl|curl]] 等网络工具的功能定位。

## 相关实体
- [[entities/baidu|baidu]]
- [[entities/brpc|brpc]]
- [[entities/status|/status]]
- [[entities/curl|curl]]

## 相关概念
- [[concepts/内置服务|内置服务]]
- [[concepts/安全模式|安全模式]]

## 来源提及
- "如果服务端口被限（比如百度内不是所有的端口都能被笔记本访问到），可以使用[rpc_view](rpc_view.md)转发。" — [[sources/builtin_service|builtin_service]]