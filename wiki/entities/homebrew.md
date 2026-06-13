---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/getting_started]]"]
tags: [product]
aliases:
  - "Homebrew"
  - "brew"
  - "macOS Homebrew"
---


# Homebrew

## 基本信息
- Type: product
- Source: [[sources/getting_started|getting_started]]

## 描述
Homebrew 是 macOS 平台上广泛使用的软件包管理器，在 brpc 文档中被推荐作为在 [[brpc/getting_started|MacOS]] 上安装编译依赖的首选工具。用户通过 `brew install` 命令可以方便地安装 brpc 编译和测试所需的各类依赖，包括 [[entities/openssl|openssl]]、git、gflags、leveldb、gperftools 等。在 Apple Silicon (M1) 设备上，Homebrew 的默认安装路径为 `/opt/homebrew`，而在传统 Intel Mac 上则安装于 `/usr/local`，这一路径差异会影响后续依赖库链接路径的配置。Homebrew 同时也支持通过本地 formula 文件（如 `brew install ./homebrew-formula/protobuf.rb`）安装自定义版本的 protobuf，以满足 brpc 对特定 protobuf 版本的需求。

## 相关实体
- [[entities/openssl|openssl]]
- [[brpc/getting_started|brpc Getting Started 文档]]

## 相关概念
无相关概念。

## 来源提及
- `brew install ./homebrew-formula/protobuf.rb` — [[sources/getting_started|getting_started]]
- `brew install openssl git gnu-getopt coreutils gflags leveldb` — [[sources/getting_started|getting_started]]