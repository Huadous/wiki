---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "LevelDB"
  - "Google LevelDB"
  - "lvldb"
---


# leveldb

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
LevelDB 是由 Google 开发的轻量级键值对（key-value）存储库，基于 LSM-Tree 结构设计，提供高效的写入性能和有序键值存储能力。它被广泛应用于需要快速本地持久化存储的场景，例如配置管理、数据缓存和日志记录。在 brpc 框架中，leveldb 被用作 /rpcz 功能的底层存储引擎，用于记录和跟踪 RPC 调用，帮助开发者进行分布式系统的性能分析和故障排查。leveldb 是 brpc 的非必需但推荐依赖——brpc 在不安装 leveldb 的情况下仍然可以正常编译和运行，但 /rpcz 功能将不可用。在 Linux 系统上，可通过包管理器便捷安装：Ubuntu 下使用 `apt install libleveldb-dev`，Fedora 下使用 `dnf install leveldb-devel`。如果需要静态链接 leveldb，还需要额外安装 `libsnappy-dev` 以提供 Snappy 压缩支持。

## 相关实体
- [[entities/brpc|brpc]] — leveldb 是 brpc /rpcz 功能的依赖组件
- [[entities/gflags|gflags]] — 与 leveldb 同属 brpc 构建时的常见依赖
- [[entities/protobuf|protobuf]] — 另一个与 leveldb 并列的 brpc 关键依赖

## 相关概念
- [[concepts/rpc|RPC]] — leveldb 所支持的 /rpcz 功能用于记录 RPC 调用跟踪
- [[concepts/存储|存储]] — leveldb 作为键值存储库的核心定位

## 来源提及
- "leveldb: Required by /rpcz to record RPCs for tracing." — [[sources/en_getting_started|en_getting_started]]
- "Install common deps, gflags, protobuf, leveldb." — [[sources/en_getting_started|en_getting_started]]
- "If you need to statically link leveldb: sudo apt-get install -y libsnappy-dev" — [[sources/en_getting_started|en_getting_started]]