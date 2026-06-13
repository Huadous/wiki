---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "term"
aliases:
  - "LOG_AT宏"
---

## Related Concepts
- [[concepts/streaming_log|streaming_log]]
- [[concepts/log_if|LOG_IF]]
- [[concepts/vlog|VLOG]]

## Related Entities
- [[entities/stringsink|StringSink]]
- [[entities/logsink|LogSink]]

## Mentions in Source

> **Source: [[sources/streaming_log|streaming_log]]**
> - `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";`
> - `// the file:line part should be using the argument given by us.`
> - `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));`

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - `LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";`
> - `// the file:line part should be using the argument given by us.`
> - `ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));`