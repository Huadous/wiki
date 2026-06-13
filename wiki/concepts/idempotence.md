---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client|en_client]]"]
tags: [term]
aliases:
  - "幂等性"
  - "idempotency"
  - "Idempotence"
---


# Idempotence

## 定义
Idempotence（幂等性）是指某项操作无论被执行多少次，其产生的结果都与仅执行一次时完全相同的属性。在 brpc 远程过程调用（RPC）的上下文中，幂等性是一个关键的设计考量：客户端的 retry 机制可能导致同一个请求被服务端多次处理，因此具有副作用（side effects）的服务必须显式地保障幂等性，否则可能引发不可预期的行为。

## 关键特征
- **多次执行结果一致**：无论操作被应用一次还是多次，最终的系统状态保持不变。
- **副作用操作的隐性风险**：写入、扣款、写入存储等带副作用的操作天然不是幂等的，必须通过额外设计（例如版本号、序列号、唯一请求 ID）来拒绝已被应用过的请求。
- **只读操作天然幂等**：查询、检索等无副作用的 RPC 通常天然幂等，可以安全地重试。
- **与 retry 机制紧密耦合**：brpc 的 retry、backup request 等机制可能在网络抖动或超时场景下多次发送同一请求，服务端必须为这种重复执行做好准备。
- **需要业务层显式实现**：brpc 框架本身不自动保证幂等性，是否幂等由服务实现者负责。

## 应用
- **只读 RPC 服务**：例如搜索、查询、读取配置等服务天然具备幂等性，客户端可放心启用 retry 机制。
- **写操作 RPC 服务**：例如存储写入、订单创建、支付扣款等服务，必须通过请求去重机制（如基于唯一流水号、版本号或服务端的"已处理集合"）实现幂等性。
- **retry 机制的依赖前提**：在 brpc 中启用 retry 之前，开发者必须先评估目标服务是否幂等；非幂等服务若开启 retry，可能造成数据不一致或重复扣款等问题。
- **backup request 机制的安全前提**：与 [[concepts/backup_request|Backup Request]] 类似，backup request 同样依赖服务幂等性来保证多次并发请求的安全性。

## 相关概念
- [[concepts/retry|Retry]]
- [[concepts/backup-request|Backup Request]]
- [[concepts/controller|Controller]]

## 相关实体
（暂无相关实体）

## 来源提及
- Generally RPC services with side effects must consider idempotence of the service, otherwise retries may make side effects be done more than once and result in unexpected behavior. — [[sources/en_client|en_client]]