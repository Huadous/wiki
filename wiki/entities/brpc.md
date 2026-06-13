---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_redis_client]]"
  - "[[sources/lalb]]"
  - "[[sources/en_rdma]]"
  - "[[concepts/单线程反应器]]"
  - "[[sources/en_streaming_rpc]]"
  - "[[sources/en_server]]"
  - "[[sources/rdma]]"
  - "[[sources/redis_client]]"
  - "[[sources/en_overview]]"
  - "[[sources/combo_channel]]"
  - "[[sources/en_io]]"
  - "[[sources/circuit_breaker]]"
  - "[[sources/en_http_service]]"
  - "[[sources/backup_request]]"
  - "[[sources/builtin_service]]"
  - "[[sources/en_getting_started]]"
  - "[[brpc/streaming_rpc.md]]"
  - "[[brpc/streaming_log.md]]"
  - "[[brpc/server.md]]"
  - "[[brpc/rdma.md]]"
  - "[[brpc/memory_management.md]]"
  - "[[brpc/load_balancing.md]]"
  - "[[brpc/json2pb.md]]"
  - "[[brpc/io.md]]"
  - "[[brpc/iobuf.md]]"
  - "[[brpc/http_service.md]]"
tags:
  - "product"
aliases:
  - "baidu-rpc"
  - "Apache brpc"
  - "brpc (Apache brpc)"
  - "baidu-rpc"
  - "Apache brpc"
  - "Apache"
  - "baidu-rpc"
  - "Apache brpc"
  - "brpc (Apache brpc)"
  - "baidu-rpc"
  - "Apache brpc"
---

## Related Entities
- [[entities/json2pb]]
- [[entities/rapidjson]]
- [[entities/protocol-buffers]]
- [[entities/eventdispatcher|EventDispatcher]]
- [[entities/inputmessenger|InputMessenger]]
- [[entities/socket|Socket]]
- [[entities/iobuf|butil::IOBuf]]
- [[entities/nginx|nginx]]
- [[entities/node.js-http-parser|node.js http parser]]

## Related Concepts
- [[concepts/tcmalloc]]
- [[concepts/jemalloc]]
- [[concepts/load-balancer|负载均衡]]
- [[concepts/naming-service|命名服务]]
- [[concepts/health-check|健康检查]]
- [[concepts/doubly-buffered-data|DoublyBufferedData]]
- [[concepts/bthread|bthread]]
- [[concepts/json-protobuf-conversion|JSON-protobuf双向转化]]
- [[concepts/http-json-access|HTTP + JSON 访问 protobuf 服务]]
- [[concepts/protobuf-version-compat|protobuf 2.x/3.x 兼容性]]
- [[concepts/json-protobuf-conversion-rules|JSON-protobuf转换规则]]
- [[concepts/repeated-field-json-encoding|repeated字段JSON编码]]
- [[concepts/json-map-encoding|JSON map编码]]
- [[concepts/unknown-fields-handling|Unknown fields处理]]
- [[concepts/non-blocking-io|Non-blocking IO]]
- [[concepts/wait-free-mpsc|Wait-free MPSC 链表]]
- [[concepts/edge-triggered|Edge triggered 模式]]
- [[concepts/bthread-work-stealing|bthread work stealing]]
- [[concepts/socketid|SocketId]]
- [[concepts/zero-copy-buffer|零拷贝缓冲]]
- [[concepts/iobuf-builder|IOBufBuilder]]
- [[concepts/http-h2-service|HTTP/H2服务]]
- [[concepts/restful-url-mapping|Restful URL映射]]
- [[concepts/protobuf-service-definition|protobuf服务定义]]
- [[concepts/progressive-attachment|ProgressiveAttachment]]

## Mentions in Source

> **Source: json2pb**
> - brpc支持json和protobuf间的**双向**转化，实现于[json2pb](https://github.com/apache/brpc/tree/master/src/json2pb/)，json解析使用[rapidjson](https://github.com/miloyip/rapidjson)。
> - 此功能对pb2.x和3.x均有效。
> - by design, 通过HTTP + json访问protobuf服务是对外服务的常见方式，故转化必须精准，转化规则列举如下。

> **Source: load_balancing**
> - Naming Service提供了服务的发现和负载均衡功能。

> **Source: memory_management**
> - brpc使用jemalloc作为默认内存分配器以提升多线程场景下的内存分配性能。

> **Source: server**
> - brpc Server基于bthread构建，支持多种并发模型和协议。

> **Source: io**
> - brpc使用一个或多个EventDispatcher(简称为EDISP)等待任一fd发生事件。
> - 可以看出，Socket类似shared_ptr，SocketId类似weak_ptr，但Socket独有的SetFailed可以在需要时确保Socket不能被继续Address而最终引用计数归0，单纯使用shared_ptr/weak_ptr则无法保证这点，当一个server需要退出时，如果请求仍频繁的到来，对应Socket的引用计数可能迟迟无法清0而导致server无法退出。

> **Source: iobuf**
> - brpc使用butil::IOBuf作为一些协议中的附件或http body的数据结构，它是一种非连续零拷贝缓冲，在其他项目中得到了验证并有出色的性能。
> - 如果你之前使用Kylin中的BufHandle，你将更能感受到IOBuf的便利性：前者几乎没有实现完整，直接暴露了内部结构，用户得小心翼翼地处理引用计数，极易出错。

> **Source: http_service**
> - 这里指我们通常说的http/h2服务，而不是可通过http/h2访问的pb服务。
> - brpc把HTTP/2协议统称为"h2"，不论是否加密。
> - brpc中http和h2的编程接口基本没有区别。除非特殊说明，所有提到的http特性都同时对h2有效。
> - brpc 服务端通过 Controller 对象将 HTTP 请求和响应的 header、body 暴露给业务代码。
> - 本文档专门介绍 brpc 中的 HTTP/H2 服务特性，包括 URL 路由、参数处理、压缩、HTTPS、性能优化以及持续发送等高级功能。