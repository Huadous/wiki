---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_log|streaming_log]]"]
tags: [method]
aliases:
  - "logging::noflush"
  - "noflush 哨兵对象"
---


# noflush

## 定义
noflush 是 brpc `streaming_log` 提供的一个特殊哨兵对象（sentinel object）。当写入日志流时，它本身不会产生任何输出，而是作为一个信号，告知日志系统暂时不要将内容刷入屏幕，而是将其保留在线程局部（thread-local）缓冲中。

## 关键特征
- **哨兵对象（sentinel）**：`noflush` 是一个占位标记，写入时不会产生可见的日志输出。
- **延迟刷入**：携带 `noflush` 的日志条目会被暂存到 thread-local 缓冲中，而不是立即输出。
- **自动合并**：下一次使用普通 LOG（不附带 `noflush`）时，之前累积的缓冲内容会随这一次日志一并刷入屏幕。
- **bthread 兼容**：`noflush` 支持 bthread，可在 bthread 环境下实现类 UB pushnotice 的批量输出效果。
- **glog 限制**：如果编译时开启了 glog 选项，则不支持 `noflush`。

## 应用
- **循环日志合并**：在循环中打印日志时，使用 `noflush` 可以避免每个循环元素都产生独立的日志行，而是把所有元素合并为一行输出。
- **批量输出通知**：在 bthread 场景下使用 `noflush`，可实现类似 UB pushnotice 的批量日志输出效果。
- **减少日志碎片化**：通过延迟刷入降低短时间内大量小日志条目对屏幕和后端的冲击。

## 相关概念
- [[concepts/thread-local缓冲|thread-local 缓冲]]
- [[concepts/LOG宏|LOG 宏]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "如果你暂时不希望刷到屏幕，加上noflush。这一般会用在打印循环中" — [[sources/streaming_log|streaming_log]]
- "前两次TRACE日志都没有刷到屏幕，而是还记录在thread-local缓冲中，第三次TRACE日志则把缓冲都刷入了屏幕。" — [[sources/streaming_log|streaming_log]]
- "> 注意：如果编译时开启了glog选项，则不支持noflush。" — [[sources/streaming_log|streaming_log]]