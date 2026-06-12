---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/combo_channel]]"]
tags: [method]
aliases:
  - "file://命名服务"
  - "File Naming Service"
  - "文件命名服务"
---


# 文件命名服务（File Naming Service）

## 定义
文件命名服务是 brpc 中一种轻量级的命名服务实现方式，通过读取本地文件（格式通常为 `file://server_list`）来动态获取服务端地址列表。当文件内容发生变化时，客户端能够自动检测变更并重新加载，从而实现服务地址的实时更新。该机制常用于测试、演示以及简单的服务发现场景。

## 关键特征
- **基于本地文件**：通过读取指定路径的文本文件获取服务端地址列表，文件每行一个地址。
- **自动监听与刷新**：支持自动监听文件变化（inode修改时间等），当文件内容更新时，客户端自动重新加载地址列表，无需重启进程。
- **无外部依赖**：无需依赖 etcd、ZooKeeper 等分布式协调服务，部署和测试极其简单。
- **支持动态扩缩容**：通过修改文件内容（添加或移除地址行），即可在运行态动态改变后端服务集群，客户端平滑迁移流量。
- **适合测试与演示**：典型使用模式是在测试或演示环境中，通过手动编辑 `server_list` 文件模拟后端扩容或缩容。

## 应用
- **测试与演示环境**：在 DynamicPartitionChannel 演示中，Client 使用 `file://server_list` 作为命名服务。初始文件仅包含 3 个分库的地址，修改文件后加入第 4 分库的地址（如 `8005`），Client 自动发现变更并重新载入，流量逐渐从旧分库迁移到新分库，实现平滑扩容。
- **临时或小型集群**：适用于不频繁变更且规模较小的后端服务集群，避免部署维护 etcd 等外部服务。
- **快速原型开发**：在功能验证阶段，通过修改本地文件即可快速调整后端配置，加速迭代。

## 相关概念
- [[concepts/命名服务|命名服务]]
- [[concepts/容量计算规则|容量计算规则]]
- [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]]
- [[concepts/PartitionChannel|PartitionChannel]]

## 相关实体
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]
- [[entities/bns|bns]]

## 来源提及
- "命名服务"file://server_list"的内容是：" — [[brpc/combo_channel|combo_channel]]
- "09-06 10:51:10:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 3 unique addresses from `server_list`" — [[brpc/combo_channel|combo_channel]]
- "开始修改分库，在server_list中加入4分库的8005：" — [[brpc/combo_channel|combo_channel]]
- "客户端发现了server_list的变化并重新载入，但qps并没有什么变化。" — [[brpc/combo_channel|combo_channel]]