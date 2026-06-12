---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "method"
aliases:
  - "Arena分配"
  - "Protobuf Arena内存管理"
---

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/serviceoptions|ServiceOptions]]（包含 `rpc_pb_message_factory` 配置字段）

## Mentions in Source

> **Source: [[sources/en_server|en_server]]**
> - "Protobuf arena is a Protobuf message memory management mechanism with the advantages of improving memory allocation efficiency, reducing memory fragmentation, and being cache-friendly."
> - "Users can set `ServerOptions.rpc_pb_message_factory = brpc::GetArenaRpcPBMessageFactory();` to manage Protobuf message memory, with the default `start_block_size` (256 bytes) and `max_block_size` (8192 bytes)."
> - "Note: Since Protocol Buffers v3.14.0, Arenas are now unconditionally enabled..."