---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc]]"]
tags: [product]
aliases:
  - "baidu utility"
  - "baidu util"
  - "butil 工具库"
---


# butil

## 基本信息
- Type: product
- Source: [[sources/streaming_rpc]]

## 描述
butil 是 [[entities/brpc|brpc]] 项目的基础工具库，全称为 baidu utility（百度实用工具库），为 brpc 提供日志、字符串处理、文件系统操作等底层基础设施支持。本文档涉及的 streaming_log 完整实现位于 `<butil/logging.h>` 头文件中，所有日志宏和类都定义在该库中。butil 是 streaming_log 的宿主环境，也是 CHECK 宏在断言失败时打印调用栈所依赖的关键组件，其中 `butil::debug::StackTrace` 负责捕获和输出堆栈信息。作为 brpc 的核心依赖库，butil 为上层模块提供统一的日志记录、错误处理和系统调用封装能力。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/streaming_log|streaming_log]]
- [[entities/logsink|LogSink]]

## 相关概念
- [[concepts/流式日志|流式日志]]
- [[concepts/check宏|CHECK宏]]

## 来源提及
- `#include <butil/logging.h>` — [[entities/streaming_log|streaming_log]]
- `#0 0x000000afaa23 butil::debug::StackTrace::StackTrace()` — [[entities/streaming_log|streaming_log]]