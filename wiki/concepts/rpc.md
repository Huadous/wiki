---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_getting_started]]"
tags:
  - "method"
aliases:
  - "远程过程调用"
  - "Remote Procedure Call"
  - "RPC (Remote Procedure Call)"
  - "远程过程调用"
  - "Remote Procedure Call"
---

## Related Concepts
- [[concepts/serialization|serialization]]
- [[concepts/naming-service|naming service]]
- [[concepts/load-balancing|load balancing]]
- [[concepts/tcp-ip|TCP/IP]]
- [[concepts/序列化|序列化]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protobuf|protobuf]]
- [[entities/gRPC|gRPC]]
- [[entities/bns|bns]]
- [[entities/thrift|thrift]]
- [[entities/leveldb|leveldb]]

## Mentions in Source

> **Source: [[sources/en_overview|en_overview]]**
> - "RPC addresses the above issues by abstracting network communications as 'clients accessing functions on servers': client sends a request to server, wait until server receives -> processes -> responds to the request, then do actions according to the result."
> - "RPC needs serialization which is done by protobuf pretty well."

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "leveldb: Required by /rpcz to record RPCs for tracing."
> - "protobuf: Serializations of messages, interfaces of services."
> - "No directly relevant information" [Note: 该源文件中未提供与 RPC 概念直接相关的新信息]