---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [other]
aliases:
  - "config_brpc.sh"
  - "BRPC 配置脚本"
---


# config_brpc.sh

## 基本信息
- Type: other
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述

`config_brpc.sh` 是 [[entities/brpc|brpc]] 项目提供的 shell 配置脚本，用于简化编译流程。它通过 `--headers` 和 `--libs` 选项指定头文件与库路径，通过 `--cxx` 和 `--cc` 指定 C++ 和 C 编译器。该脚本支持 `--nodebugsymbols` 去除调试符号、`--with-glog` 启用 [[entities/glog|glog]] 日志集成，以及 `--with-thrift` 启用 [[entities/thrift|thrift]] 支持。在 Ubuntu、Fedora、MacOS 等系统上，推荐用户克隆 brpc 代码后直接运行此脚本并执行 `make` 完成构建。文档中针对不同操作系统提供了详细的参数示例，帮助开发者快速适配本地环境。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/gflags|gflags]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/cmake|cmake]]
- [[entities/glog|glog]]
- [[entities/thrift|thrift]]

## 相关概念
- [[concepts/静态链接|静态链接]]
- [[concepts/构建系统|构建系统]]

## 来源提及
- "sh config_brpc.sh --headers=/usr/include --libs=/usr/lib --cc=clang --cxx=clang++" — [[sources/en_getting_started|en_getting_started]]
- "To not link debugging symbols, add --nodebugsymbols" — [[sources/en_getting_started|en_getting_started]]
- "To use brpc with glog, add --with-glog." — [[sources/en_getting_started|en_getting_started]]
- "To enable thrift support, install thrift first and add --with-thrift." — [[sources/en_getting_started|en_getting_started]]