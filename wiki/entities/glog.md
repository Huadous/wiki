---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "Google glog"
  - "glog日志库"
---


# glog

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
glog 是 Google 开发的日志库，广泛用于 C++ 项目。它提供了一个灵活且高效的日志框架，支持不同级别（如 INFO、WARNING、ERROR、FATAL）的日志输出。在 [[entities/brpc|brpc]] 框架中，glog 可用于替换默认的日志实现。由于 brpc 自带的日志工具与 glog 功能重叠，两者在编译时会产生冲突，因此需要显式启用 glog 支持。启用方法为在 [[entities/config_brpc.sh|config_brpc.sh]] 中添加 `--with-glog` 参数，或通过 [[entities/cmake|cmake]] 构建系统添加 `-DWITH_GLOG=ON` 选项。glog 的版本要求为 3.3 或更高。启用后，brpc 的所有日志输出将交由 glog 管理，这对于已经使用 glog 进行日志集成的项目尤为有利。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/cmake|cmake]]
- [[entities/config_brpc.sh|config_brpc.sh]]

## 相关概念
- [[concepts/日志系统|日志系统]]

## 来源提及
- "To use brpc with glog, add --with-glog." — [[sources/en_getting_started|en_getting_started]]
- "brpc implements a default logging utility which conflicts with glog. To replace this with glog, add --with-glog to config_brpc.sh or add -DWITH_GLOG=ON to cmake." — [[sources/en_getting_started|en_getting_started]]
- "glog: 3.3+" — [[sources/en_getting_started|en_getting_started]]