---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[brpc/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "PLOG()"
  - "PLOG 宏"
  - "PLOG"
  - "PLOG()"
  - "PLOG 宏"
---

## Related Concepts
- [[concepts/log宏|LOG宏]]

## Related Entities
（暂无相关实体）

## Mentions in Source
- PLOG和LOG的不同之处在于，它会在日志后加上错误码的信息，类似于printf中的%m。在posix系统中，错误码就是errno。 — [[streaming_log|streaming_log]]
- "Fail to open foo.conf: No such file or directory" — [[streaming_log|streaming_log]]

> **Source: [[en_streaming_log|en_streaming_log]]**
> - "The difference of PLOG and LOG is that it will append error information at the end of log. It's kind of like %m in printf."
> - "Under POSIX environment, the error code is errno."

> **Source: [[en_streaming_log|en_streaming_log]]**
> - "No directly relevant information"