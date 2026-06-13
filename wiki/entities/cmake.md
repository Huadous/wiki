---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "cmake"
  - "CMake"
  - "CMake构建工具"
---

## Related Entities
- [[entities/brpc|brpc]] — cmake 是 brpc 的主要构建方式之一
- [[entities/thrift|thrift]] — cmake 支持通过 `-DWITH_THRIFT=ON` 集成 Thrift
- [[entities/gtest|gtest]] — brpc 的测试框架通过 cmake 集成在构建流程中
- [[entities/glog|glog]] — cmake 支持通过 `-DWITH_GLOG=ON` 启用 glog
- [[entities/vcpkg|vcpkg]] — cmake 与 vcpkg 协同管理 brpc 的依赖库
- [[entities/libunwind|libunwind]] — cmake 构建流程集成 libunwind 作为 brpc 的依赖之一

## Related Concepts
- [[concepts/构建系统|构建系统]] — cmake 是一个典型的构建系统生成器
- [[concepts/静态链接|静态链接]] — cmake 构建支持灵活控制链接方式

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "Compile brpc with cmake"
> - "mkdir build && cd build && cmake .. && cmake --build . -j6"
> - "With CMake 3.13+, we can also use the following commands to build the project: cmake -B build && cmake --build build -j6"

> **Source: [[sources/getting_started|getting_started]]**
> - "使用cmake编译brpc"
> - "mkdir build && cd build && cmake .. && cmake --build . -j6"
> - "要帮助VSCode或Emacs(LSP)去正确地理解代码，添加`-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`选项去生成`compile_commands.json`。"