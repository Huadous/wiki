---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/bvar_c++.md]]"
tags: [bvar::Variable, bvar::Reducer, bvar::Adder, bvar::Maxer, bvar::Miner, bvar::IntRecorder, bvar::LatencyRecorder, bvar::Window, bvar::PerSecond, bvar::WindowEx, bvar::PerSecondEx, bvar::Status, bvar::PassiveStatus, bvar::GFlag, expose, bvar导出, Dumper, DumpOptions, butil::Timer, bvar::Stat, bvar名字归一化, bvar命名规范, 衍生变量, 合并运算符要求, bvar线程安全, expose_as, bvar::WindowExAdapter]
aliases: ["bvar 使用文档（单维度）", "bvar Documentation (Single-Dimension)", "bvar 单维度使用文档"]
---

# bvar 使用文档（单维度） - Summary

## 来源
- Original file: [[brpc/bvar_c++.md]]
- Ingested: 2026-06-13

## 核心内容
本文档介绍了 [[entities/bvar|bvar]] 的使用方法，bvar 是 [[entities/brpc|brpc]] 项目中的一组 C++ 计数器类库，用于程序内部各种统计和监控指标的记录与展示。文档详细描述了 [[concepts/bvarvariable|bvar::Variable]] 基类及其 [[concepts/expose|expose]] / [[concepts/expose_as|expose_as]] 机制，[[concepts/bvarreducer|bvar::Reducer]] 模板及其子类 [[concepts/bvaradder|bvar::Adder]]、[[concepts/bvarmaxer|bvar::Maxer]]、[[concepts/bvarminer|bvar::Miner]]，以及 [[concepts/bvarintrecorder|bvar::IntRecorder]]、[[concepts/bvarlatencyrecorder|bvar::LatencyRecorder]]、[[concepts/bvarstatus|bvar::Status]]、[[concepts/bvarpassivestatus|bvar::PassiveStatus]]、[[concepts/bvargflag|bvar::GFlag]] 等多种计数器类型。文档重点阐述了 [[concepts/衍生变量|衍生变量]]（[[concepts/bvarwindow|bvar::Window]]、[[concepts/bvarpersecond|bvar::PerSecond]]）与独立版本（[[concepts/bvarwindowex|bvar::WindowEx]]、[[concepts/bvarpersecondex|bvar::PerSecondEx]]）的区别，以及 [[concepts/bvar线程安全|bvar线程安全]]、[[concepts/bvar命名规范|bvar命名规范]]、[[concepts/bvar名字归一化|bvar名字归一化]]、[[concepts/合并运算符要求|合并运算符要求]] 等核心约束，并介绍了通过 [[concepts/bvar导出|bvar导出]] 机制（gflags + [[concepts/dumper|Dumper]] + [[concepts/dumpoptions|DumpOptions]]）将 bvar 周期性写入本地文件或通过 brpc 的 /vars HTTP 服务查询的方法。多维度场景需使用 [[entities/mbvar|mbvar]]。

## 关键实体
- [[entities/bvar|bvar]]：Apache brpc 中的 C++ 计数器类库
- [[entities/brpc|brpc]]：bvar 所属的工业级 RPC 框架，提供 /vars HTTP 查询接口
- [[entities/mbvar|mbvar]]：bvar 的多维度版本，支持标签维度查询
- [[entities/gflags|gflags]]：控制 bvar dump 行为的命令行参数库，配合 [[concepts/bvargflag|bvar::GFlag]] 监控

## 关键概念
- [[concepts/bvarvariable|bvar::Variable]]：所有 bvar 的基类，提供全局注册与查询
- [[concepts/bvarreducer|bvar::Reducer]]：模板类，需满足 [[concepts/合并运算符要求|合并运算符要求]]（结合律、交换律、无副作用）
- [[concepts/bvaradder|bvar::Adder]]、[[concepts/bvarmaxer|bvar::Maxer]]、[[concepts/bvarminer|bvar::Miner]]：Reducer 的三个常用子类
- [[concepts/bvarintrecorder|bvar::IntRecorder]]：计算自使用以来的平均值，常配合 Window 使用
- [[concepts/bvarlatencyrecorder|bvar::LatencyRecorder]]：复合计数器，自动输出 latency/max_latency/qps/count
- [[concepts/bvarwindow|bvar::Window]]、[[concepts/bvarpersecond|bvar::PerSecond]]：衍生变量，依赖已存在的 bvar 自动更新
- [[concepts/bvarwindowex|bvar::WindowEx]]、[[concepts/bvarpersecondex|bvar::PerSecondEx]]：独立版本，window_size 通过模板参数传递
- [[concepts/bvarstatus|bvar::Status]]、[[concepts/bvarpassivestatus|bvar::PassiveStatus]]：值显示与按需显示
- [[concepts/bvargflag|bvar::GFlag]]：将 gflag 公开为 bvar
- [[concepts/expose|expose]]、[[concepts/expose_as|expose_as]]：bvar 全局曝光机制
- [[concepts/bvar导出|bvar导出]]、[[concepts/dumper|Dumper]]、[[concepts/dumpoptions|DumpOptions]]：bvar 导出机制
- [[concepts/butiltimer|butil::Timer]]：与 LatencyRecorder 配合的计时器
- [[concepts/bvarstat|bvar::Stat]]：WindowEx/PerSecondEx 在 IntRecorder 上的返回值类型
- [[concepts/衍生变量|衍生变量]]、[[concepts/bvar线程安全|bvar线程安全]]、[[concepts/bvar命名规范|bvar命名规范]]、[[concepts/bvar名字归一化|bvar名字归一化]]、[[concepts/bvarwindowexadapter|bvar::WindowExAdapter]]：贯穿全文的约束与机制
- [[concepts/合并运算符要求|合并运算符要求]]：Reducer 对二元运算符的强制约束

## 要点
- bvar 提供多种计数器类型，[[concepts/bvarreducer|bvar::Reducer]] 模板通过满足结合律、交换律、无副作用的二元运算符合并多线程数据，因此减法不能作为 Reducer 运算符
- [[concepts/衍生变量|衍生变量]]（[[concepts/bvarwindow|bvar::Window]]、[[concepts/bvarpersecond|bvar::PerSecond]]）依赖已有 bvar 自动更新；[[concepts/bvarpersecond|bvar::PerSecond]] 对与时间无关的量无意义，应使用 window_size=1 的 Window
- [[concepts/bvarwindowex|bvar::WindowEx]] 与 [[concepts/bvarpersecondex|bvar::PerSecondEx]] 是独立版本，window_size 通过模板参数传递，需主动推值
- 命名规范推荐 `模块_类名_指标` 格式，个数 `_count`、每秒个数 `_second`、每分钟个数 `_minute`；bvar 自动做[[concepts/bvar名字归一化|名字归一化]]，将 `foo::BarNum`、`foo.bar.num` 等统一为 `foo_bar_num`
- bvar 线程兼容：不同线程操作不同 bvar 安全，同一 bvar 的非读写接口（如 expose/hide）线程不安全
- **不要跨文件定义全局 Window 或 PerSecond**，不同编译单元中全局变量初始化顺序未定义
- 通过 `bvar_dump` 系列 gflags 可周期性将 bvar 写入本地文件；通过 [[entities/brpc|brpc]] 的 `/vars` HTTP 服务可实时查询
- [[concepts/bvarpassivestatus|bvar::PassiveStatus]] 是最有用的 bvar 之一，适用于按需打印已存在但无法 set_value 的统计量