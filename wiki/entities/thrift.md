---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "Apache Thrift"
  - "Thrift协议"
  - "Thrift RPC框架"
---

## Related Entities
- [[entities/brpc|brpc]] — brpc框架支持Thrift集成，提供线程安全且高性能的Thrift客户端
- [[entities/protobuf|protobuf]] — 与Thrift相似的序列化和RPC框架
- [[entities/open-source-oss-community|开源社区]] — Thrift作为Apache开源项目的社区依托
- [[entities/RPC|RPC]] — Thrift所属的分布式通信范式

## Related Concepts
- [[concepts/serialization|serialization]] — Thrift和protobuf共同依赖的核心序列化技术
- [[concepts/RPC|RPC]] — Thrift所属的分布式通信范式
- [[concepts/IDL|IDL]] — Thrift使用接口定义语言描述服务接口
- [[concepts/config_brpc|config_brpc]] — 通过添加 `--with-thrift` 选项启用 Thrift 支持的 brpc 配置脚本
- [[concepts/CMake|CMake]] — 通过传入 `-DWITH_THRIFT=ON` 选项启用 Thrift 支持的构建工具

## Mentions in Source
> **Source: [[sources/en_overview|en_overview]]**
> - "thrift support, thread-safe, more friendly and performant than the official clients."
> - "All sorts of protocols used in Baidu: ... thrift support ..."

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "To enable thrift support, install thrift first and add --with-thrift."
> - "thrift: 0.9.3-0.11.0"

> **Source: [[sources/getting_started|getting_started]]**
> - "要启用 [thrift 支持](../en/thrift.md)，首先安装thrift并且添加选项`--with-thrift`。"
> - "thrift: 0.9.3-0.11.0"
> - "无已知问题。"