---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/overview]]"
  - "[[sources/techniques]]"
  - "[[sources/en_server]]"
  - "[[sources/editions]]"
  - "[[sources/style]]"
  - "[[sources/en_overview]]"
  - "[[sources/encoding]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[sources/en_http_service]]"
  - "[[sources/en_getting_started]]"
tags:
  - "product"
aliases:
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
  - "Protobuf"
  - "protobuf"
  - "Protocol Buffers"
  - "SelfDescribingMessage"
  - "protobuf"
  - "Protocol Buffers"
---

## Related Entities
- [[entities/brpc|brpc]] — 深度依赖Protobuf的RPC框架，利用protobuf定义所有服务接口
- [[entities/google|Google]] — Protobuf的创始者和主要维护者
- [[entities/open-source-oss-community|open-source-oss-community]] — Protobuf的开源社区维护力量
- [[entities/protoc|protoc]] — Protobuf的编译器，负责从.proto文件生成代码
- [[concepts/editions/Protobuf Editions|Protobuf Editions]] — Protobuf的最新语法版本系统

## Related Concepts
- [[concepts/序列化|序列化]] — protobuf的核心能力，将结构化数据转换为线格式
- [[concepts/编码规范|编码规范]] — .proto文件的命名和格式约定
- [[concepts/RPC|RPC]] — protobuf最常见的应用场景
- [[concepts/proto3|proto3]] — 当前主流的protobuf语法版本，brpc 1.8.0后强制要求，其引入曾分裂生态
- [[concepts/editions|editions]] — 继proto3之后的新一代语法版本系统
- [[concepts/字段|字段]] — 消息中的基本数据单元
- [[concepts/字段编号|字段编号]] — 每个字段在二进制编码中的唯一标识号
- [[concepts/线格式|线格式]] — protobuf的二进制编码格式
- [[concepts/变长整数|变长整数]] — 用于紧凑编码整数的关键技术
- [[concepts/标签-长度-值|标签-长度-值]] — protobuf线格式的基本编码单元
- [[concepts/字段基数|字段基数]] — 字段的出现次数规则（optional/repeated/map）
- [[concepts/字段存在性|字段存在性]] — proto3中字段是否存在追踪机制
- [[concepts/保留字段|保留字段]] — 防止已废弃字段编号被重新使用的机制
- [[concepts/打包编码|打包编码]] — repeated字段的压缩编码方式
- [[concepts/features|Features]] — Editions体系下每个版本可独立配置的特性集合
- [[concepts/Edition Zero|Edition Zero]] — Editions项目定义的初始版本基线
- [[concepts/protobuf service|protobuf service]] — 在.proto文件中定义RPC服务接口的方式
- [[concepts/HTTP/h2服务|HTTP/h2服务]] — brpc中需通过.proto文件声明空请求和响应的HTTP服务类型
- [[concepts/Controller|Controller]] — brpc中的控制对象，用于HTTP请求处理
- [[concepts/Restful URL|Restful URL]] — brpc HTTP服务支持的URL模式

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
> - "http/h2 services in brpc have to declare interfaces with empty request and response in a .proto file."
> - "Add the service declaration in a proto file."
> - "option cc_generic_services = true;"
> - "Implement the service by inheriting the base class generated in .pb.h, which is same as protobuf services."

> **Source: [[sources/proto3|proto3]]**
> - (Existing mentions preserved)

> **Source: [[sources/encoding|encoding]]**
> - (Existing mentions preserved)

> **Source: [[sources/style|style]]**
> - (Existing mentions preserved)

> **Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]**
> - "Protobuf is one of Google's oldest and most successful toolchain projects."
> - "The last radical change to Protobuf (syntax = "proto3";) split the ecosystem."