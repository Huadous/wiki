---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
tags:
  - "product"
aliases:
  - "braft"
  - "BRPC RAFT"
  - "brpc braft"
---

## Related Entities
- [[entities/brpc|brpc]] — braft所依赖的底层RPC通信框架，两者共同开源，brpc通过braft实现RAFT算法
- [[entities/baidu|baidu]] — 百度公司，braft的主要开发者与使用者
- [[entities/github|github]] — braft代码托管平台
- [[entities/bvar|bvar]] — braft可用bvar进行性能监控与统计
- [[entities/iobuf|iobuf]] — braft通过brpc的IOBuf进行高效的数据传输

## Related Concepts
- [[concepts/raft|RAFT]] — braft所实现的分布式共识算法核心理论
- [[concepts/rpc|RPC]] — braft基于[[entities/brpc|brpc]]使用的远程过程调用通信机制
- [[concepts/raft-consensus-algorithm|Raft共识算法]] — braft实现的工业级共识算法，用于构建高可用分布式服务
- [[concepts/分布式系统|分布式系统]] — braft的应用领域，通过分布式共识构建高可用服务