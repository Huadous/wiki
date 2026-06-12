---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_io]]"
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