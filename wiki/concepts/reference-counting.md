---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_iobuf]]"]
tags: [method]
aliases:
  - "引用计数"
  - "Reference Counting"
  - "Ref-counting"
---


# Reference counting

## 定义
引用计数（Reference counting）是一种用于追踪共享资源引用数量的内存管理技术。在 brpc 的 [[concepts/iobuf|IOBuf]] 中，引用计数用于管理大小为 8K 的内存块的生命周期。通过引用计数，多个 IOBuf 实例可以共享同一块底层载荷数据（payload），拷贝时仅复制管理结构本身，从而实现零拷贝语义。

## 关键特征
- **块大小固定为 8K**：IOBuf 内部的引用计数单元是 8K 大小的内存块
- **结构与数据分离**：复制 IOBuf 时仅复制管理结构（管理结构体），底层载荷数据保持共享
- **共享语义**：多个 IOBuf 实例通过引用计数指向同一块底层数据
- **生命周期管理**：所有引用者释放后，对应的 8K 块才被回收
- **内存压力风险**：若 IOBuf 生命周期过长，引用计数的 8K 块可能持续占用大量内存，导致内存锁死（lock too many memory）

## 应用
- **IOBuf 零拷贝共享**：在网络收发、反序列化等场景中，多个消费者可共享同一块载荷数据，避免冗余拷贝
- **Kylin 中的 BufHandle**：`[[entities/kylin|Kylin]]` 项目的 BufHandle 设计将内部引用计数直接暴露给使用者，要求使用者必须自行谨慎管理引用增减，容错性较差，容易出错

## 相关概念
- [[concepts/iobuf|IOBuf]]
- [[concepts/zero-copy-buffer|Zero-copy buffer]]

## 相关实体
- [[entities/kylin|Kylin]]

## 来源提及
- "Lifetime of IOBuf should be short, to prevent the referentially counted blocks(8K each) in IOBuf lock too many memory." — [[sources/en_iobuf|en_iobuf]]
- "Copy the managing structure of IOBuf only rather the payload." — [[sources/en_iobuf|en_iobuf]]