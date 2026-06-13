---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/memory_management|memory_management]]"]
tags: [term]
aliases:
  - "guard page (栈保护页)"
  - "guard page"
  - "栈保护页"
---


# guard page

## 定义
guard page（栈保护页）是设置在栈边界的一块保护性内存页（通常大小为 4K），用于检测栈溢出。其核心原理是通过 `mprotect` 将栈边界的一页内存设置为不可访问（PROT_NONE），一旦程序发生栈越界访问，访问行为会立即触发段错误（SIGSEGV），从而使栈溢出能够被及时发现。

## 关键特征
- 页面大小通常为 4K（一个标准内存页），紧贴栈的边界放置。
- 通过 `mprotect` 系统调用将该页设置为不可访问权限。
- 栈越界访问会立即触发段错误，而非悄无声息地破坏相邻内存。
- 实现机制基于 `mmap` + `mprotect`，因此受到操作系统 `max_map_count` 参数的限制（Linux 默认值为 65536）。
- 属于一种轻量的栈溢出检测机制，无需额外的栈深度计数或 canary 值即可工作。

## 应用
- 在 brpc 的 bthread 实现中，为每个 bthread 栈分配一个 4K 的 guard page，以检测栈溢出。
- 当系统中 bthread 数量非常多时，由于 `mmap` + `mprotect` 的总次数受限于 `max_map_count`，需要相应调大该内核参数。
- 广泛应用于各类用户态协程库与线程库中，作为防止栈溢出破坏关键数据的标准手段。

## 相关概念
- [[concepts/bthread 栈管理|bthread 栈管理]]
- [[concepts/mmap|mmap]]
- [[concepts/mprotect|mprotect]]

## 相关实体
_No related entities_

## 来源提及
- "bthread还会用mprotect分配4K的guard page以检测栈溢出。" — [[sources/memory_management|memory_management]]
- "由于mmap+mprotect不能超过max_map_count（默认为65536），当bthread非常多后可能要调整此参数。" — [[sources/memory_management|memory_management]]