---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "OpenSSL"
  - "OpenSSL加密库"
---


# openssl

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
OpenSSL是一个开源的加密库，提供SSL/TLS协议和加密算法的实现。它是互联网安全通信的基础组件，被广泛应用于各类网络应用中。在brpc框架中，OpenSSL用于支持HTTPS通信功能，确保数据传输的加密和安全。brpc支持OpenSSL 0.97至1.1版本，覆盖了较长时期内的稳定版本。在构建brpc时，需要安装`openssl-devel`包以提供必要的头文件和库文件。在MacOS环境下，OpenSSL的安装路径可能因系统版本变化而不同，需要手动配置链接或设置路径。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/protobuf|protobuf]]
- [[entities/gflags|gflags]]

## 相关概念
无

## 来源提及
- "openssl: 0.97-1.1 required by https." — [[sources/en_getting_started|en_getting_started]]
- "Install common deps, ... openssl ..." — [[sources/en_getting_started|en_getting_started]]
- "openssl installed in Monterey may not be found at /usr/local/opt/openssl..." — [[sources/en_getting_started|en_getting_started]]