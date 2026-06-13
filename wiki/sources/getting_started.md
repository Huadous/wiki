---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/getting_started.md]]"
tags: [config_brpc.sh, 静态链接, tcmalloc, thrift, rpcz, 实例追踪, glog, libunwind, valgrind, CMake, cpu profiler, heap profiler, contention profiler, c++11]
aliases: ["brpc Getting Started", "brpc 构建与编译指南"]
---

# brpc 构建与编译指南 - Summary

## 来源
- Original file: [[brpc/getting_started.md]]
- Ingested: 2026-06-13

## 核心内容

本文件是 [[entities/brpc|brpc]] 项目的官方构建与编译指南，详细介绍如何在不同操作系统和环境下编译 brpc。brpc 鼓励[[concepts/静态链接|静态链接]]依赖，以简化部署流程，其核心依赖包括 [[entities/gflags|gflags]]（全局选项）、[[entities/protobuf|protobuf]]（消息序列化与服务接口）以及 [[entities/leveldb|leveldb]]（[[concepts/rpcz|rpcz]] 追踪功能所需）。文档涵盖了 [[entities/ubuntu|Ubuntu/LinuxMint/WSL]]、[[entities/centos|Fedora/CentOS]]、自构建依赖的 Linux、 [[entities/macos|MacOS]]（含 Apple Silicon）以及 [[entities/docker|Docker]] 等多种环境下的依赖准备和编译方法。提供两套编译方案：传统的 [[concepts/config_brpc-sh|config_brpc.sh]] 脚本与现代的 [[concepts/cmake|CMake]] 构建系统，并介绍了 [[entities/vcpkg|vcpkg]] 包管理器方案。同时列出了 brpc 各依赖的版本范围、已知问题及 [[entities/trackme_server|trackme_server]] 实例追踪工具的使用方法。

## 关键实体

- [[entities/brpc|brpc]]：Apache 开源 RPC 框架
- [[entities/gflags|gflags]]：全局选项解析库
- [[entities/protobuf|protobuf]]：消息序列化库
- [[entities/leveldb|leveldb]]：键值存储库（rpcz 依赖）
- [[entities/trackme_server|trackme_server]]：brpc 实例追踪工具
- [[entities/vcpkg|vcpkg]]：Microsoft 开源的 C++ 包管理器
- [[entities/openssl|openssl]]：HTTPS 加密库依赖
- [[entities/docker|docker]]：容器化构建环境
- [[entities/homebrew|homebrew]]：macOS 包管理器
- [[entities/gcc|gcc]]：推荐编译器（4.8-11.2，推荐 8.2+）
- [[entities/clang|clang]]：可选编译器（3.5-4.0）
- [[entities/gtest|gtest]]：测试框架（运行测试时需要）
- [[entities/ubuntu|ubuntu]]：主要支持的 Linux 发行版
- [[entities/centos|centos]]：Fedora/CentOS 系列发行版
- [[entities/macos|macos]]：开发与测试平台（性能可能差于 Linux）
- [[entities/wsl|wsl]]：Windows Linux 子系统

## 关键概念

- [[concepts/config_brpc-sh|config_brpc-sh]]：传统构建配置脚本
- [[concepts/静态链接|静态链接]]：brpc 推荐的依赖链接方式
- [[concepts/cmake|cmake]]：现代构建系统
- [[concepts/c++11|c++11]]：默认启用的 C++ 标准
- [[concepts/tcmalloc|tcmalloc]]：高性能内存分配器（默认不链接）
- [[concepts/thrift|thrift]]：Apache 跨语言 RPC 框架（可选支持）
- [[concepts/rpcz|rpcz]]：brpc 内置 RPC 追踪模块
- [[concepts/实例追踪|实例追踪]]：通过 trackme_server 实现的运维功能
- [[concepts/glog|glog]]：可选日志后端
- [[concepts/libunwind|libunwind]]：栈展开库（bthread tracer 需要）
- [[concepts/valgrind|valgrind]]：内存调试工具
- [[concepts/cpu-profiler|cpu-profiler]]：CPU 性能分析器
- [[concepts/heap-profiler|heap-profiler]]：堆分析器
- [[concepts/contention-profiler|contention-profiler]]：锁竞争分析器

## 要点

- brpc 鼓励[[concepts/静态链接|静态链接]]依赖，核心依赖为 [[entities/gflags|gflags]]、[[entities/protobuf|protobuf]] 和 [[entities/leveldb|leveldb]]；支持 [[entities/ubuntu|Ubuntu/LinuxMint/WSL]]、[[entities/centos|Fedora/CentOS]]、[[entities/macos|MacOS]] 及 [[entities/docker|Docker]] 多种环境
- 提供两套编译方案：传统 [[concepts/config_brpc-sh|config_brpc.sh]] 脚本（支持 --headers/--libs、--with-glog、--with-thrift 等选项）和现代 [[concepts/cmake|CMake]] 构建系统；[[entities/vcpkg|vcpkg]] 可一步完成安装
- 依赖版本范围：[[entities/gcc|GCC]] 4.8-11.2（推荐 8.2+）、[[entities/clang|Clang]] 3.5-4.0、protobuf 3.0-5.29（不再兼容 2.x）、gflags 2.1-2.2.2、openssl 0.97-1.1、tcmalloc 1.7-2.5、glog 3.3+、valgrind 3.8+、thrift 0.9.3-0.11.0、libunwind 1.3-1.8.1
- [[concepts/tcmalloc|tcmalloc]] 默认不链接但可显著提升多线程性能；不同版本差异大，2.1 存在自旋锁问题，且不及时归还内存给系统可能导致内存问题排查困难
- [[entities/trackme_server|trackme_server]] 是 brpc 自带的[[concepts/实例追踪|实例追踪]]工具，通过 -trackme_server=SERVER 参数启用，可周期性接收实例 ping 消息并辅助运维聚合实例地址