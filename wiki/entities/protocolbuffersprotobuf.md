---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/options|options]]"
  - "[[brpc/server.md]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
tags:
  - "project"
aliases:
  - "protobuf"
  - "Protocol Buffers"
  - "Google Protocol Buffers"
---

## Mentions in Source
> **Source: [[sources/options|options]]**
> - "This file contains a global registry of known extensions for descriptor.proto, so that any developer who wishes to use multiple 3rd party projects, each with their own extensions, can be confident that there won't be collisions in extension numbers."
> - "please send us a pull request to add an entry to this doc, or create an issue with info about your project (name and website) so we can add an entry for you."

> **Source: [[sources/server|server]]**
> - "请求、回复、服务的接口均定义在proto文件中。"
> - "protoc运行后会生成echo.pb.cc和echo.pb.h文件"
> - "protobuf中有类似的限制"
> - "brpc移除了protobuf中的限制，全交由此选项控制，只要-max_body_size足够大，用户就不会看到错误日志。"

> **Source: [[sources/java-lite|java-lite]]**
> - No directly relevant information

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - No directly relevant information