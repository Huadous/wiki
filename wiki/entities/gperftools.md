---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Google Performance Tools"
  - "gperftools"
---


# gperftools

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
gperftools 是一套由 Google 开发的性能分析工具集，包含 CPU profiler、heap profiler 和 heap checker 等组件。在 [[entities/brpc|brpc]] 框架的文档中，gperftools 被作为可选依赖项提及，用于启用示例程序和运行时中的 CPU 和堆分析功能。用户可以通过系统包管理器安装 gperftools，例如在 [[entities/ubuntu|Ubuntu]] 上安装 `libgoogle-perftools-dev`，在 [[entities/centos|CentOS]]/[[entities/fedora|Fedora]] 上安装 `gperftools-devel`，或在 [[entities/macos|macOS]] 上通过 `brew install gperftools` 安装。brpc 默认不链接 tcmalloc，但 gperftools 包含的 `libtcmalloc_and_profiler.a` 库可供性能分析使用。该工具集在 C++ 性能调优场景中广泛应用。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/tcmalloc|tcmalloc]]
- [[entities/glog|glog]]
- [[entities/ubuntu|ubuntu]]
- [[entities/centos|centos]]
- [[entities/fedora|fedora]]
- [[entities/macos|macos]]
- [[entities/libunwind|libunwind]]

## 相关概念
- [[concepts/CPU-profiler|CPU Profiler]]
- [[concepts/Heap-profiler|Heap Profiler]]

## 来源提及
- "If you need to enable cpu/heap profilers in examples: sudo apt-get install -y libgoogle-perftools-dev" — [[sources/en_getting_started|en_getting_started]]
- "If you need to enable cpu/heap profilers in examples: sudo yum install gperftools-devel" — [[sources/en_getting_started|en_getting_started]]
- "If you need to enable cpu/heap profilers in examples: brew install gperftools" — [[sources/en_getting_started|en_getting_started]]