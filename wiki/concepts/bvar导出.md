---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [method]
aliases:
  - "bvar dump"
  - "Export all variables"
  - "bvar_dump"
---


# bvar导出

## 定义
bvar导出是指将进程内所有已曝光（exposed）的 [[entities/bvar|bvar]] 写入文件或 HTTP 接口的功能。它既可以通过 gflag 开启内置的后台线程周期性地把 bvar 写入本地文件，也可以通过实现自定义的 [[concepts/Dumper|Dumper]] 接口并调用 `Variable::dump_exposed()` 来导出。HTTP 形式的导出由 brpc 的 `/vars` 服务提供，文件形式的导出则由 bvar 自带的功能实现（默认不开启）。

## 关键特征
- 导出行为由多个 gflag 共同控制：
  - `bvar_dump`：总开关。
  - `bvar_dump_file`：导出文件路径，默认为 `monitor/bvar.<app>.data`，非空时启动后台导出线程。
  - `bvar_dump_include`：白名单 wildcard。
  - `bvar_dump_exclude`：黑名单 wildcard。
  - `bvar_dump_interval`：导出周期，默认 10 秒。
  - `bvar_dump_prefix`、`bvar_dump_tabs`：导出格式控制。
- 过滤规则：仅写入被 `bvar_dump_include` 匹配、且不被 `bvar_dump_exclude` 匹配的 bvar。
- 自定义导出：用户可实现 [[concepts/Dumper|Dumper]] 接口，并使用 [[concepts/DumpOptions|DumpOptions]] 进行白名单/黑名单 wildcard 过滤。
- gflag 设置禁忌：请勿直接通过 `FLAGS_bvar_dump_file` / `FLAGS_bvar_dump_include` / `FLAGS_bvar_dump_exclude` 赋值。一方面这些 gflag 类型是 `std::string`，直接覆盖是线程不安全的；另一方面不会触发 validator（检查正确性的回调），因此也不会启动后台导出线程。

## 应用
- 周期性将进程内 bvar 落盘，便于后续离线分析、监控采集与历史回溯。
- 通过 HTTP `/vars` 接口实时查询 bvar 状态，配合监控/告警系统使用。
- 实现自定义 Dumper，将 bvar 输出到非默认目标（如远程存储、消息队列、Prometheus exporter 等），并基于 `DumpOptions` 做精细的 wildcard 过滤。

## 相关概念
- [[concepts/expose]]
- [[concepts/Dumper]]
- [[concepts/DumpOptions]]

## 相关实体
- [[entities/bvar]]
- [[entities/brpc]]

## 来源提及
- 最常见的导出需求是通过HTTP接口查询和写入本地文件。前者在brpc中通过[/vars](vars.md)服务提供，后者则已实现在bvar中，默认不打开。 — [[sources/bvar_c++|bvar_c++]]
- 当bvar_dump_file不为空时，程序会启动一个后台导出线程以bvar_dump_interval指定的间隔更新bvar_dump_file，其中包含了被bvar_dump_include匹配且不被bvar_dump_exclude匹配的所有bvar。 — [[sources/bvar_c++|bvar_c++]]
- 请勿直接设置FLAGS_bvar_dump_file / FLAGS_bvar_dump_include / FLAGS_bvar_dump_exclude。
一方面这些gflag类型都是std::string，直接覆盖是线程不安全的；另一方面不会触发validator（检查正确性的回调），所以也不会启动后台导出线程。 — [[sources/bvar_c++|bvar_c++]]