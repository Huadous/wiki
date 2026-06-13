---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/combo_channel]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "method"
aliases:
  - "file://命名服务"
  - "File Naming Service"
  - "文件命名服务"
  - "file naming service"
  - "file://命名服务"
  - "File Naming Service"
  - "文件命名服务"
---

## Basic Information
- **Type**: concept（命名服务实现机制）
- **Sources**: [[sources/combo_channel|combo_channel]]、[[sources/load_balancing|load_balancing]]
- **Definition**: 文件命名服务是 brpc 中以 `file://<file-path>` 协议形式提供的命名服务实现，地址列表直接来源于一个本地文件，通过 [[entities/filewatcher|FileWatcher]] 监听文件修改时间，在文件更新后重新读取并通过 `NamingServiceActions::ResetServers` 通知框架。

## Description
文件命名服务是 brpc 提供的一种轻量级命名服务实现，地址以 `file://<file-path>` 形式声明，列表内容直接来源于一个本地文本文件，每行一个服务端地址。该机制使用 [[entities/filewatcher|FileWatcher]] 监听文件的修改时间，一旦文件被更新就重新读取，并通过 `NamingServiceActions::ResetServers` 通知框架完成地址列表的刷新，从而避免传统轮询带来的开销。由于整个数据源和变更通知链路都是本地的，它不依赖 etcd、ZooKeeper、bns 等分布式协调服务，部署和测试极其简单，适合配置变更不频繁的场景。在 [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]] 演示中，可以通过手动编辑 `server_list` 文件来模拟后端分库的扩容或缩容，客户端自动发现变更后流量会平滑迁移到新的分库地址。[[entities/namingservicethread|NamingServiceThread]] 为其提供 bthread 容器运行环境，整体机制既可用于测试与演示，也适用于临时或小规模集群的快速原型开发。

## Related Concepts
- [[concepts/命名服务|命名服务]]
- [[concepts/容量计算规则|容量计算规则]]
- [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]]
- [[concepts/PartitionChannel|PartitionChannel]]

## Related Entities
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]
- [[entities/bns|bns]]
- [[entities/filewatcher|FileWatcher]]
- [[entities/namingservicethread|NamingServiceThread]]
- [[entities/namingservicewatcher|NamingServiceWatcher]]

## Mentions in Source
> **Source: [[sources/combo_channel|combo_channel]]**
> - "命名服务"file://server_list"的内容是："
> - "09-06 10:51:10:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 3 unique addresses from `server_list`"
> - "开始修改分库，在server_list中加入4分库的8005："
> - "客户端发现了server_list的变化并重新载入，但qps并没有什么变化。"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "file：列表即文件。合理的方式是在文件更新后重新读取。"
> - "file://<file-path>           # load addresses from the file"