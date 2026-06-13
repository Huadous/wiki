---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_io]]"
  - "[[brpc/io.md]]"
tags:
  - "method"
aliases:
  - "持续写入bthread"
  - "KeepWrite线程"
  - "后台写入bthread"
  - "KeepWrite"
  - "持续写入bthread"
  - "KeepWrite线程"
  - "后台写入bthread"
  - "KeepWrite bthread"
  - "持续写入bthread"
  - "KeepWrite线程"
  - "后台写入bthread"
  - "KeepWrite"
  - "持续写入bthread"
  - "KeepWrite线程"
  - "后台写入bthread"
---

## Related Concepts
- [[concepts/wait-free-mpsc|Wait-free MPSC 链表]]

## Related Entities
- [[entities/socket|Socket]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/bvar|bvar]]
- [[entities/baidu|brpc]]
- [[entities/bthread|bthread]]

## Mentions in Source

> **Source: [[sources/en_io|en_io]]**
> - "In current implementations, if the data cannot be written fully in one call, a KeepWrite bthread is created to write the remaining data."
> - "Since writes in brpc always complete within short time, the calling thread can handle new tasks more quickly and background KeepWrite threads also get more tasks to write in one batch, forming pipelines and increasing the efficiency of IO at high throughputs."
> - "No directly relevant information"

> **Source: [[sources/io|io]]**
> - "在当前的实现中，如果获得写权利的线程一下子无法写出所有的数据，会启动一个KeepWrite线程继续写，直到所有的数据都被写出。"
> - "由于brpc的写出总能很快的返回，调用线程可以更快地处理新任务，后台KeepWrite写线程也能每次拿到一批任务批量写出，在大吞吐时容易形成流水线效应而提高IO效率。"
> - "No directly relevant information"