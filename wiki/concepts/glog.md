---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/getting_started|getting_started]]"]
tags: [term]
aliases:
  - "Google Logging Library"
  - "libglog"
---


# glog

## 定义
glog 是 Google 开源的 C++ 日志库（Google Logging Library，又称 libglog），是 [[entities/brpc|brpc]] 可选的日志后端。[[entities/brpc|brpc]] 自身实现了一个默认的日志功能（位于 `src/butil/logging.h`），该实现与 glog 存在符号冲突。[[entities/brpc|brpc]] 支持 glog 3.3 及以上版本。

## 关键特征
- 由 Google 开源的 C++ 日志库，提供 `LOG(INFO)`、`LOG(WARNING)`、`LOG(ERROR)`、`LOG(FATAL)` 等分级宏。
- 与 [[entities/brpc|brpc]] 内置的默认日志实现（`src/butil/logging.h`）存在符号冲突，二者不能同时启用。
- [[entities/brpc|brpc]] 兼容 glog 3.3+ 版本。
- 可通过构建选项替换 [[entities/brpc|brpc]] 的默认日志后端。

## 应用
- 在 [[entities/brpc|brpc]] 中将默认日志后端替换为 glog：给 `config_brpc.sh` 增加 `--with-glog` 选项，或给 CMake 传递 `-DWITH_GLOG=ON` 选项。
- 与 [[concepts/tcmalloc|tcmalloc]] 类似，作为 [[entities/brpc|brpc]] 可选的三方依赖用于构建配置。
- 在 [[entities/brpc|brpc]] 的 Getting Started 构建指南中被列为可选项之一。

## 相关概念
- [[concepts/config_brpc.sh|config_brpc.sh]]
- [[concepts/CMake|CMake]]
- [[concepts/tcmalloc|tcmalloc]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- 使用glog版的brpc，添加选项`--with-glog`。 — [[sources/getting_started|getting_started]]
- glog: 3.3+ — [[sources/getting_started|getting_started]]
- brpc实现了一个默认的日志功能它和glog冲突。要替换成glog，可以给config_brpc.sh增加`--with-glog`选项或者给cmake增加`-DWITH_GLOG=ON`选项。 — [[sources/getting_started|getting_started]]