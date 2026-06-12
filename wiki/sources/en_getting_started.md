---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[brpc/en_getting_started.md]]"
tags: [静态链接, RPC]
aliases: ["brpc 构建指南", ""]
---

# brpc 构建指南 - Summary

## 来源
- Original file: [[brpc/en_getting_started.md]]
- Ingested: 2026-06-12

## 核心内容
本文档是 [[entities/brpc|brpc]] 高性能 RPC 框架的完整构建指南。它详细介绍了如何在多种操作系统和环境下从源代码编译 brpc。文档强调 brpc 倾向于使用 [[concepts/静态链接|静态链接]] 依赖库，以简化部署：所有依赖（包括 [[entities/gflags|gflags]]、[[entities/protobuf|protobuf]] 和 [[entities/leveldb|leveldb]]）将直接嵌入最终可执行文件，避免在每台运行机器上单独安装。支持四种主要构建方式：使用自带的 [[entities/config_brpc-sh|config_brpc.sh]] 脚本、使用 [[entities/cmake|cmake]]、使用 [[entities/vcpkg|vcpkg]] 包管理器，以及使用 [[entities/docker|Docker]]。文档还提供了在不同环境（[[entities/ubuntu|Ubuntu]]/[[entities/linuxmint|LinuxMint]]/[[entities/wsl|WSL]]、[[entities/fedora|Fedora]]/[[entities/centos|CentOS]]、[[entities/macos|macOS]]、自建依赖的 Linux）中的具体安装命令，并详列了编译器（[[entities/gcc|GCC]] 4.8-11.2、[[entities/clang|Clang]] 3.5-4.0）和关键库（[[entities/openssl|OpenSSL]] 0.97-1.1、[[entities/tcmalloc|tcmalloc]] 1.7-2.5、[[entities/glog|glog]] 3.3+、[[entities/thrift|thrift]] 0.9.3-0.11.0）的版本兼容性矩阵。最后介绍了 [[entities/trackme_server|trackme_server]] 这一实例跟踪工具，用于监控所有 brpc 实例的运行状态。

## 关键实体
- [[entities/brpc|brpc]] — 构建的核心对象，一个高性能 RPC 框架
- [[entities/protobuf|protobuf]] — 用于消息序列化和服务接口定义
- [[entities/gflags|gflags]] — 用于定义全局命令行选项
- [[entities/leveldb|leveldb]] — 用于 /rpcz 功能记录 RPC 调用追踪
- [[entities/cmake|cmake]] — 主要的跨平台构建工具
- [[entities/config_brpc-sh|config_brpc.sh]] — brpc 自带的配置脚本
- [[entities/gtest|gtest]] — 单元测试框架
- [[entities/glog|glog]] — 可选的日志库，可替换默认日志
- [[entities/openssl|OpenSSL]] — 支持 HTTPS 所需的加密库
- [[entities/tcmalloc|tcmalloc]] — 可选的高性能内存分配器
- [[entities/thrift|thrift]] — 可选的跨语言 RPC 框架支持
- [[entities/gperftools|gperftools]] — 可选的性能分析工具集
- [[entities/trackme_server|trackme_server]] — 实例跟踪监测工具

## 关键概念
- [[concepts/静态链接|静态链接]] — brpc 推荐的依赖链接方式，减少运行时部署负担
- [[concepts/rpc|RPC]] — 远程过程调用，brpc 框架的核心概念

## 要点
- brpc 倾向于使用静态链接，将依赖库直接嵌入可执行文件，便于部署
- 核心依赖链：gflags（配置）→ protobuf（序列化/接口）→ leveldb（追踪存储）
- 支持四种构建方式：config_brpc.sh、cmake、vcpkg 和 Docker
- 构建环境覆盖 Ubuntu、Fedora/CentOS、macOS、Docker，以及通过自建依赖的通用 Linux
- 编译器和库必须满足严格的版本兼容性要求（如 GCC 4.8-11.2、protobuf 3.0-5.29）
- 可选功能可通--with-glog、--with-thrift 等编译选项启用