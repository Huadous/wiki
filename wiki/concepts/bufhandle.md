---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/iobuf.md]]"
  - "[[brpc/en_iobuf.md]]"
tags:
  - "term"
aliases:
  - "Kylin BufHandle"
  - "Apache Kylin BufHandle"
---

## Related Concepts
- [[concepts/零拷贝缓冲]]
- [[concepts/butil::IOBuf]]
- [[concepts/引用计数]]

## Related Entities
- [[entities/brpc]]
- [[entities/kylin|Kylin 项目]]

## Mentions in Source

> **Source: [[sources/iobuf|iobuf]]**
> - "如果你之前使用Kylin中的BufHandle，你将更能感受到IOBuf的便利性：前者几乎没有实现完整，直接暴露了内部结构，用户得小心翼翼地处理引用计数，极易出错。"
> - "brpc使用butil::IOBuf作为一些协议中的附件或http body的数据结构，它是一种非连续零拷贝缓冲，在其他项目中得到了验证并有出色的性能。"

> **Source: [[sources/en_iobuf|en_iobuf]]**
> - "If you've used the BufHandle in Kylin before, you should notice the convenience of IOBuf: the former one is badly encapsulated, leaving the internal structure directly in front of users, who must carefully handle the referential countings, very error prone and leading to bugs."