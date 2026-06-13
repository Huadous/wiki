---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "term"
aliases:
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread-local data"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread Local Storage"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread-local data"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread_key_create"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread-local data"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread Local Storage"
  - "bthread本地存储"
  - "bthread-local storage"
  - "bthread-local data"
  - "bthread本地存储"
  - "bthread-local storage"
---

## Related Concepts
- [[concepts/session-local-data|session-local data]]
- [[concepts/server-thread-local-data|server-thread-local data]]
- [[concepts/pthread模式|pthread模式]]
- [[concepts/bthread|bthread]]
- [[concepts/bthread-local|bthread-local]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/server|brpc Server端使用文档]]**
> - "在所有情况下，我们需要更通用的thread-local方案。在这种情况下，你可以使用bthread_key_create, bthread_key_destroy, bthread_getspecific, bthread_setspecific等函数，它们的用法类似pthread中的函数。"
> - "用bthread_key_create创建一个bthread_key_t，它代表一种bthread私有变量。"
> - "// in some thread ...\nMyThreadLocalData* tls = static_cast<MyThreadLocalData*>(bthread_getspecific(tls_key));\nif (tls == NULL) {  // First call to bthread_getspecific (and before any bthread_setspecific) returns NULL"
> - "一个server创建的bthread在退出时并不删除bthread-local，而是还回server的一个pool中，以被其他bthread复用。"