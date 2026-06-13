---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "method"
aliases:
  - "Arena分配"
  - "Protobuf Arena内存管理"
---

## Related Concepts
- [[concepts/protobuf|protobuf]]
- [[concepts/rpc-protobuf-message-factory|RPC Protobuf message factory]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/serviceoptions|ServiceOptions]]（包含 `rpc_pb_message_factory` 配置字段）
- [[entities/defaultrpcpbmessagefactory|DefaultRpcPBMessageFactory]]

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "Protobuf arena is a Protobuf message memory management mechanism with the advantages of improving memory allocation efficiency, reducing memory fragmentation, and being cache-friendly."
> - "Users can set `ServerOptions.rpc_pb_message_factory = brpc::GetArenaRpcPBMessageFactory();` to manage Protobuf message memory, with the default `start_block_size` (256 bytes) and `max_block_size` (8192 bytes)."
> - "Note: Since Protocol Buffers v3.14.0, Arenas are now unconditionally enabled..."

> **Source: [[sources/server|server]]**
> - "Protobuf arena是一种Protobuf message内存管理机制，有着提高内存分配效率、减少内存碎片、对缓存友好等优点。"
> - "如果用户希望使用protobuf arena来管理Protobuf message内存，可以设置ServerOptions.rpc_pb_message_factory = brpc::GetArenaRpcPBMessageFactory()"
> - "从Protobuf v3.14.0开始，默认开启arena。但是Protobuf v3.14.0之前的版本，用户需要再proto文件中加上选项：option cc_enable_arenas = true;"
> - "用户可以调用brpc::GetArenaRpcPBMessageFactory<StartBlockSize, MaxBlockSize>();自定义arena大小。"