---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/bthread|bthread]]"]
tags: [term]
aliases:
  - "Non-Uniform Memory Access"
  - "非一致性内存访问"
---


# NUMA

## 定义
NUMA（Non-Uniform Memory Access，非一致性内存访问）是一种多处理器系统中的内存访问架构。在NUMA架构下，各处理器访问其本地内存（local memory）的速度要快于访问其他处理器关联的远程内存（remote memory），因此内存访问延迟与处理器和内存的物理位置相关，呈现出"非一致性"的特征。NUMA通常作为多核系统设计目标中的一个可选特性被提及，例如在[[brpc/bthread|bthread]]的设计目标中，better cache locality 与 supporting NUMA is a plus 被并列提出。

## 关键特征
- 内存访问延迟取决于处理器与目标内存之间的物理位置关系：本地访问快，远程访问慢。
- 是多核/多插槽服务器系统中常见的内存组织方式，与SMP（对称多处理）形成对比。
- 在线程库设计中，支持NUMA通常意味着需要考虑将线程绑定到特定CPU核心、尽量使用本地内存以提升性能。
- 良好的cache locality（缓存局部性）是减少NUMA架构下远程内存访问开销的关键因素。
- 在brpc的[[brpc/bthread|bthread]]设计中，NUMA被列为一个加分项（plus），属于更高的优化目标层级。

## 应用
- **操作系统与运行时**：Linux内核提供NUMA感知的内存分配策略（如`numactl`、`mbind`等接口），调度器可将进程/线程绑定到特定NUMA节点。
- **高性能线程库**：线程库（如[[brpc/bthread|bthread]]）在设计目标中关注NUMA支持，以提升大规模并发场景下的内存访问效率。
- **数据库与中间件**：在高并发数据库、缓存系统等场景下，NUMA感知的数据放置和线程绑定能够显著降低远程内存访问延迟。
- **HPC与服务器应用**：科学计算、内存密集型服务器等场景广泛利用NUMA架构特性进行性能调优。
- 与bthread的关联：[[brpc/bthread|bthread]]通过将大量用户级线程映射到少量pthread上，使线程对资源（如thread-local cache）的需求被稀释——独立bthread没有自身独立的thread-local cache（不像每个pthread都拥有的tcmalloc thread-local cache），其底层最终仍映射到少量pthread，从而实现更集中的线程资源使用，获得更好的cache locality，这也是对NUMA等高级内存架构特性的间接优化路径。

## 相关概念
- [[concepts/m-n-threading|M:N threading]]

## 相关实体
- [[entities/bthread|bthread]]

## 来源提及
- better cache locality, supporting NUMA is a plus. — [[brpc/bthread|bthread]]
- 拥有大量pthread后，每个线程对资源的需求被稀释了，基于thread-local cache的代码效果会很差，比如tcmalloc。而独立的bthread不会有这个问题，因为它最终还是被映射到了少量的pthread。bthread相比pthread的性能提升很大一部分来自更集中的线程资源。 — [[brpc/bthread|bthread]]