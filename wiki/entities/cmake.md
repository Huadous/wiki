---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "cmake"
  - "CMake"
  - "CMake构建工具"
---


# cmake

## 基本信息
- **Type:** product
- **Source:** [[sources/en_getting_started|en_getting_started]]

## 描述

cmake 是一个跨平台的构建系统生成器，广泛应用于 C/C++ 项目的编译管理。在 brpc 项目中，cmake 被作为主要构建方式之一，与传统的 config_brpc.sh 脚本方法并行提供，为用户提供了灵活的选择。brpc 官方文档详细介绍了使用 cmake 构建 brpc 的具体步骤，包括创建 build 目录、运行 cmake 配置命令以及执行 cmake --build 进行编译。

通过 cmake 的 `-D` 选项，用户可以方便地控制编译特性，例如 `-DWITH_DEBUG_SYMBOLS=OFF` 可关闭调试符号链接，`-DWITH_GLOG=ON` 可启用 glog 日志支持，`-DWITH_THRIFT=ON` 可集成 Apache Thrift 协议支持。文档建议使用 CMake 3.13 以上版本，以便使用更简洁的现代命令语法，如 `cmake -B build && cmake --build build -j6`。

cmake 构建流程与 brpc 项目的其他依赖库（如 [[entities/gtest|gtest]]、[[entities/thrift|thrift]]）紧密集成，为 brpc 的跨平台编译提供了标准化、可扩展的解决方案。作为开源社区广泛使用的构建工具，cmake 极大地简化了大型 C++ 项目的编译配置过程。

## 相关实体
- [[entities/brpc|brpc]] — cmake 是 brpc 的主要构建方式之一
- [[entities/thrift|thrift]] — cmake 支持通过 `-DWITH_THRIFT=ON` 集成 Thrift
- [[entities/gtest|gtest]] — brpc 的测试框架通过 cmake 集成在构建流程中
- [[entities/glog|glog]] — cmake 支持通过 `-DWITH_GLOG=ON` 启用 glog

## 相关概念
- [[concepts/构建系统|构建系统]] — cmake 是一个典型的构建系统生成器
- [[concepts/静态链接|静态链接]] — cmake 构建支持灵活控制链接方式

## 来源提及
- "Compile brpc with cmake" — [[sources/en_getting_started|en_getting_started]]
- "mkdir build && cd build && cmake .. && cmake --build . -j6" — [[sources/en_getting_started|en_getting_started]]
- "With CMake 3.13+, we can also use the following commands to build the project: cmake -B build && cmake --build build -j6" — [[sources/en_getting_started|en_getting_started]]