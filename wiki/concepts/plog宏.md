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

## Description
PLOG 是 LOG 宏的扩展变种，它在保留 LOG 全部基础行为的同时，会在日志尾部自动追加当前错误码的可读描述信息。在 POSIX 系统中，该错误码对应 `errno`，PLOG 会读取并格式化 `errno` 的字符串形式附加在日志末尾，从而省去开发者手动查阅 `errno` 含义并拼接字符串的工作量。从使用语义上看，PLOG 的行为与 `printf` 中的 `%m` 占位符一致：当 `errno=ENOENT` 时，调用 `PLOG(FATAL) << "Fail to open foo.conf"` 会输出形如 `"Fail to open foo.conf: No such file or directory"` 的日志，将系统级错误原因直接翻译为可读文本。PLOG 主要面向调用失败时需要快速记录并定位 `errno` 的场景，是底层系统调用错误排查的便捷手段。需要注意的是，PLOG 仅在 POSIX 环境下有意义，依赖 `errno` 机制的平台才能发挥其自动追加错误信息的作用。

## Related Concepts
- [[concepts/log宏|LOG宏]]

## Related Entities
（暂无相关实体）

## Mentions in Source
- PLOG和LOG的不同之处在于，它会在日志后加上错误码的信息，类似于printf中的%m。在posix系统中，错误码就是errno。 — [[sources/streaming_log|streaming_log]]
- "Fail to open foo.conf: No such file or directory" — [[sources/streaming_log|streaming_log]]

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "The difference of PLOG and LOG is that it will append error information at the end of log. It's kind of like %m in printf."
> - "Under POSIX environment, the error code is errno."