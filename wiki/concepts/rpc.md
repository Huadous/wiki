---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_overview]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/bthread.md]]"
  - "[[brpc/baidu_std.md]]"
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
- [[concepts/上下文切换|上下文切换]]
- [[concepts/二进制编码|二进制编码]]
- [[concepts/数据压缩|数据压缩]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/protobuf|protobuf]]
- [[entities/gRPC|gRPC]]
- [[entities/bns|bns]]
- [[entities/thrift|thrift]]
- [[entities/leveldb|leveldb]]
- [[entities/bthread|bthread]]
- [[entities/baidu_std|baidu_std]]

## Mentions in Source

> **Source: [[sources/en_overview|en_overview]]**
> - "RPC addresses the above issues by abstracting network communications as 'clients accessing functions on servers': client sends a request to server, wait until server receives -> processes -> responds to the request, then do actions according to the result."
> - "RPC needs serialization which is done by protobuf pretty well."

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "leveldb: Required by /rpcz to record RPCs for tracing."
> - "protobuf: Serializations of messages, interfaces of services."
> - "No directly relevant information" [Note: 该源文件中未提供与 RPC 概念直接相关的新信息]

> **Source: [[sources/bthread|bthread]]**
> - "除非你需要在一次RPC过程中让一些代码并发运行，你不应当直接调用bthread函数，把这些留给brpc做更好。"
> - "比如有8个pthread worker，当有8个bthread都调用了系统usleep()后，处理网络收发的RPC代码就暂时无法运行了。"
> - "比如所有的用户代码都lock在一个pthread mutex上，并且这个mutex需要在某个RPC回调中unlock，如果所有的worker都被阻塞，那么就没有线程来处理RPC回调了，整个程序就死锁了。"
> - "No directly relevant information" [Note: 该源文件中未提供与 RPC 概念直接相关的新信息]

> **Source: [[sources/baidu_std|baidu_std]]**
> - "baidu_std是一种基于TCP协议的二进制RPC通信协议。它以Protobuf作为基本的数据交换格式，并基于Protobuf内置的RPC Service形式，规定了通信双方之间的数据交换协议，以实现完整的RPC调用。"
> - "四元组唯一地标识了一个RPC方法。"
> - "请求包中的该域由请求方设置，用于唯一标识一个RPC请求。请求方有义务保证其唯一性，协议本身对此不做任何检查。"
> - "No directly relevant information" [Note: 该源文件中未提供与 RPC 概念直接相关的新信息]