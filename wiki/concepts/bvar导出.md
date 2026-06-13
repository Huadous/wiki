---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/bvar_c++|bvar_c++]]"
  - "[[brpc/bvar.md]]"
tags:
  - "method"
aliases:
  - "bvar dump"
  - "Export all variables"
  - "bvar_dump"
  - "dump功能"
  - "bvar dump"
  - "Export all variables"
  - "bvar_dump"
---

## Description
bvar 导出（dump 功能）是 bvar 提供的一项导出机制，能够将进程中所有已注册的 bvar 变量以"名字:值"的格式定期写入指定文件。该功能需要通过 [[sources/bvar_c++|bvar_c++]] 中描述的 export 接口显式打开，开启后会在 `monitor/` 目录下生成类似 `bvar.<app>.data` 的数据文件（如 `bvar.echo_client.data`），打开后应检查该目录下是否有数据文件生成。dump 功能的输出格式简洁，每行一个键值对（"名字:值"），便于监控系统的采集脚本解析；并且每次导出都会覆盖之前的文件，这与普通 log 添加在后面的追加写入方式是不同的，因此不会无限增长文件大小。百度内部的 noah 监控系统会定期抓取这些 dump 文件，将单机数据汇总到一起后形成历史曲线展示。

导出行为由多个 gflag 共同控制：`bvar_dump` 为总开关；`bvar_dump_file` 指定导出文件路径（默认为 `monitor/bvar.<app>.data`，非空时启动后台导出线程）；`bvar_dump_include` 与 `bvar_dump_exclude` 分别定义白名单和黑名单 wildcard；`bvar_dump_interval` 控制导出周期（默认 10 秒）；`bvar_dump_prefix` 与 `bvar_dump_tabs` 用于输出格式控制。过滤规则下，仅写入被 `bvar_dump_include` 匹配、且不被 `bvar_dump_exclude` 匹配的 bvar。

除了内置的文件导出，用户也可以通过实现自定义的 [[concepts/Dumper|Dumper]] 接口并调用 `Variable::dump_exposed()` 来完成导出，配合 [[concepts/DumpOptions|DumpOptions]] 做精细的 wildcard 过滤；HTTP 形式的导出则由 brpc 的 `/vars` 服务提供。需要特别注意的是，请勿直接通过 `FLAGS_bvar_dump_file` / `FLAGS_bvar_dump_include` / `FLAGS_bvar_dump_exclude` 赋值，因为这些 gflag 类型均为 `std::string`，直接覆盖是线程不安全的，且不会触发 validator，从而也不会启动后台导出线程。

## Related Concepts
- [[concepts/expose]]
- [[concepts/Dumper]]
- [[concepts/DumpOptions]]
- [[concepts/noah]]
- [[concepts/vars|/vars]]
- [[concepts/brpc_metrics|/brpc_metrics]]

## Related Entities
- [[entities/bvar]]
- [[entities/brpc]]

## Mentions in Source

> **Source: [[sources/bvar_c++|bvar_c++]]**
> - 最常见的导出需求是通过HTTP接口查询和写入本地文件。前者在brpc中通过[/vars](vars.md)服务提供，后者则已实现在bvar中，默认不打开。
> - 当bvar_dump_file不为空时，程序会启动一个后台导出线程以bvar_dump_interval指定的间隔更新bvar_dump_file，其中包含了被bvar_dump_include匹配且不被bvar_dump_exclude匹配的所有bvar。
> - 请勿直接设置FLAGS_bvar_dump_file / FLAGS_bvar_dump_include / FLAGS_bvar_dump_exclude。一方面这些gflag类型都是std::string，直接覆盖是线程不安全的；另一方面不会触发validator（检查正确性的回调），所以也不会启动后台导出线程。

> **Source: [[sources/bvar|bvar]]**
> - 打开bvar的dump功能以导出所有的bvar到文件，格式就如上文一样，每行是一对"名字:值"。
> - 打开dump功能后应检查monitor/目录下是否有数据，比如：
> - 每次导出都会覆盖之前的文件，这与普通log添加在后面是不同的。
> - 监控系统应定期搜集每台单机导出的数据，并把它们汇总到一起。