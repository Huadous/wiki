---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "LevelDB"
  - "Google LevelDB"
  - "lvldb"
---

## Related Entities
- [[entities/brpc|brpc]] — leveldb 是 brpc /rpcz 功能的依赖组件
- [[entities/gflags|gflags]] — 与 leveldb 同属 brpc 构建时的常见依赖
- [[entities/protobuf|protobuf]] — 另一个与 leveldb 并列的 brpc 关键依赖

## Related Concepts
- [[concepts/rpcz|rpcz]] — 基于 leveldb 实现的 RPC 调用记录与追踪功能
- [[concepts/rpc|RPC]] — leveldb 所支持的 /rpcz 功能用于记录 RPC 调用跟踪
- [[concepts/存储|存储]] — leveldb 作为键值存储库的核心定位
- [[concepts/静态链接|静态链接]] — brpc 推荐使用支持 snappy 压缩的 leveldb 静态链接版本