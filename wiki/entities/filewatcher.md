---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/load_balancing|load_balancing]]"]
tags: [other]
aliases:
  - "FileWatcher 文件变更监听"
  - "brpc FileWatcher"
---


# FileWatcher

## 基本信息
- Type: other
- Source: [[sources/load_balancing|load_balancing]]

## 描述
FileWatcher 是 brpc 中定义于 `src/butil/files/file_watcher.h` 的文件变更监听工具，用于监控指定文件的修改时间变化。file 协议的 [[entities/namingservicewatcher|NamingServiceWatcher]] 实现借助 FileWatcher 关注目标文件的修改时间戳，当被监听文件发生修改时，FileWatcher 触发预先注册的回调函数。回调被触发后，file naming service 重新读取文件内容，并通过 [[entities/namingserviceactions|NamingServiceActions]] 调用 `ResetServers` 将最新的服务器列表交付给 brpc 框架，从而完成一次动态配置刷新。该机制是 brpc 基于文件的服务发现（file naming service）实现热加载的关键环节。

## 相关实体
- [[entities/namingserviceactions|NamingServiceActions]]
- [[entities/namingservicewatcher|NamingServiceWatcher]]
- [[entities/namingservicethread|NamingServiceThread]]

## 相关概念
- [[concepts/file-naming-service|file naming service]]
- [[concepts/naming-service|命名服务]]

## 来源提及
- 使用[FileWatcher]关注文件的修改时间，当文件修改后，读取并调用NamingServiceActions::ResetServers告诉框架。 — [[sources/load_balancing|load_balancing]]