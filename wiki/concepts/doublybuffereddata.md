---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/lalb]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/consistent_hashing.md]]"
tags:
  - "method"
aliases:
  - "DBD"
  - "双重缓冲数据"
  - "双缓冲数据"
  - "Double Buffered Data"
  - "DBD"
  - "双重缓冲数据"
  - "双缓冲数据"
---

## Description
DoublyBufferedData（DBD）是 brpc 中用于解决读多写少场景下并发性能问题的核心数据结构。它将数据分为前台和后台两个副本：检索线程只读前台数据，无需加锁；当需要修改数据时，写线程修改后台副本，修改完成后切换前后台角色，再睡眠一段时间以等待旧前台上的读操作全部退出。由于节点变更等写操作发生频率较低，这种双缓冲方案避免了读写锁带来的性能开销，使 brpc 中所有 load balancer 在分流时几乎不会互斥。在一致性哈希场景中，brpc 的 Hash Ring 采用修改复杂度为 O(n) 的有序数组实现，结合 DBD 的双缓冲机制，可以在节点变更时由一个缓冲区提供服务、另一个缓冲区被修改，既保证了请求路由的正确性，又通过连续的内存存储和二分查找实现了高效的节点查找。读线程之间相互无竞争，写线程需要获取所有 thread-local 锁以保证与读同步，是一种典型的读-复制-更新（RCU）思想的变体。

## Related Concepts
- [[concepts/locality-aware-load-balancing|Locality-aware load balancing]]
- [[concepts/weight-tree|Weight tree]]
- [[concepts/thread-local-storage|Thread-local storage]]
- [[concepts/load-balancing|Load balancing]]
- [[concepts/loadbalancer|LoadBalancer]]
- [[concepts/hash-ring|Hash Ring]]
- [[concepts/consistent-hashing|一致性哈希]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/lalb|lalb]]**
> - "完成这些功能的数据结构是DoublyBufferedData<>，我们常简称为DBD。brpc中的所有load balancer都使用了这个数据结构，使不同线程在分流时几乎不会互斥。"
> - "数据分前台和后台。检索线程只读前台，不用加锁。只有一个写线程：修改后台数据，切换前后台，睡眠一段时间……"
> - "我们需要写以某种形式和读同步，但读之间相互没竞争。一种解法是，读拿一把thread-local锁，写需要拿到所有的thread-local锁。"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "Load balancer最重要的是如何让不同线程中的负载均衡不互斥，解决这个问题的技术是DoublyBufferedData。"

> **Source: [[sources/consistent_hashing|consistent_hashing]]**
> - "线程安全性请参照Double Buffered Data章节."
> - "由于节点故障和变化不常发生，我们选择了修改复杂度为O(n)的有序数组来存储hash ring，每次分流使用二分查找来选择对应的机器，由于存储是连续的，查找效率比基于平衡二叉树的实现高。"