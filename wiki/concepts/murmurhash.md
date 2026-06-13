---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/flatmap|flatmap]]"
  - "[[brpc/consistent_hashing.md]]"
tags:
  - "method"
aliases:
  - "Murmur Hash"
  - "MurmurHash3"
  - "murmurhash3"
  - "Murmur Hash"
  - "MurmurHash3"
---

## Related Concepts
- [[concepts/哈希函数|哈希函数]]
- [[concepts/雪崩效应|雪崩效应]]
- [[concepts/线性同余|线性同余]]
- [[concepts/一致性哈希|一致性哈希]]
- [[concepts/md5|md5]]

## Related Entities
- [[entities/flatmap|FlatMap]]
- [[entities/smalltable|smalltable]]
- [[entities/cowhashmap|CowHashMap]]
- [[entities/alignhashmap|AlignHashMap]]
- [[entities/stdmap|std::map]]
- [[entities/brpc|brpc]]

## Mentions in Source
- 通用算法可选择Murmurhash。 — [[sources/flatmap|flatmap]]
- 对于工程师来说，选用何种算法得看实践效果，一些最简单的方法也许就有很好的效果。 — [[sources/flatmap|flatmap]]

> **Source: [[sources/consistent_hashing|consistent_hashing]]**
> - 我们内置了分别基于murmurhash3和md5两种hash算法的实现，使用要做两件事：在Channel.Init 时指定*load_balancer_name*为 "c_murmurhash" 或 "c_md5"。
> - 其他场景可以选择c_murmurhash以获得更高的性能和更均匀的分布。