---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [product]
aliases:
  - "目录浏览服务"
  - "文件浏览服务"
---


# /dir

## 基本信息
- Type: product
- Source: [[sources/builtin_service|builtin_service]]

## 描述
/dir是brpc框架内置的一个HTTP服务端点，用于通过浏览器浏览服务器上的文件目录结构。该功能提供了极大的便利性，便于开发和调试过程中快速查看服务器文件分布，但同时也带来了严重的安全风险，可能导致服务器上的敏感文件信息泄露。出于安全考虑，/dir服务默认处于关闭状态，管理员需要通过修改brpc配置文件或编译选项显式启用。启用后，任何能够访问该HTTP端点的用户均可遍历服务器上的文件系统，这在开放对外服务的生产环境中是极其危险的。brpc官方强烈建议仅在内部网络或测试环境中谨慎使用该功能，并配合[[entities/connections-监控页面|connections-监控页面]]等内置服务的全局安全模式来隐藏所有内置服务端点。在面向公网的服务场景中，必须彻底禁用/dir以防止潜在的数据泄露和攻击。

## 相关实体
- [[entities/baidu|baidu]]（brpc的创始和维护组织）
- [[entities/curl|curl]]（可用于访问/dir端点的HTTP客户端工具）
- [[entities/connections-监控页面|connections-监控页面]]（另一个brpc内置HTTP服务端点）

## 相关概念
- 安全模式（brpc中用于隐藏所有内置服务的全局开关）
- 内置服务（brpc提供的一系列HTTP调试和管理端点）

## 来源提及
- "/dir: 浏览服务器上的所有文件，方便但非常危险，默认关闭。" — [[sources/builtin_service|builtin_service]]