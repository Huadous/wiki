---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "M1"
  - "M2"
  - "Apple M系列芯片"
---


# Apple Silicon

## 基本信息
- **Type**: product
- **Source**: [[brpc/en_getting_started|brpc 构建指南]]

## 描述
Apple Silicon 是 Apple 基于 ARM 架构自主研发的芯片系列，取代了此前与 Intel 合作的 x86 处理器。该系列包括 M1、M2 及后续迭代产品，广泛应用于 Mac 电脑和 iPad 等设备。在 [[brpc/en_getting_started|brpc 构建指南]] 中，Apple Silicon 被特别提及：主分支代码已支持 M1 系列芯片，但 M2 系列尚未经过测试。由于 Apple Silicon 的 Homebrew 安装路径与 Intel Mac 不同，用户在 [[entities/macos|macOS]] 上构建时可能需要手动调整 [[entities/openssl|OpenSSL]] 库的路径。这体现了 brpc 对新兴硬件平台的积极适配，以及 ARM 生态在服务器端计算领域的扩展趋势。

## 相关实体
- [[entities/macos|macOS]]
- [[entities/openssl|OpenSSL]]

## 相关概念
暂无相关概念。

## 来源提及
- "The code at master HEAD already supports M1 series chips. M2 series are not tested yet. Please feel free to report remaining warnings/errors to us by issues." — [[brpc/en_getting_started|brpc 构建指南]]
- "openssl installed in Monterey may not be found at `/usr/local/opt/openssl`, instead it's probably put under `/opt/homebrew/Cellar`." — [[brpc/en_getting_started|brpc 构建指南]]