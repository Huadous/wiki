---
type: entity
created: 2026-06-12
updated: 2026-06-12
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

## Related Concepts
- [[concepts/HTTP/h2服务|HTTP/h2服务]]
- [[concepts/RESTful URL|RESTful URL]]
- [[concepts/Gzip压缩|Gzip压缩]]
- [[concepts/Chunked transfer encoding|分块传输编码]]
- [[concepts/Server-Sent Events|Server-Sent Events]]
- [[concepts/SSL/TLS|SSL/TLS]]
- [[concepts/HTTP headers|HTTP headers]]
- [[concepts/Content-Type|Content-Type]]
- [[concepts/Status Code|Status Code]]
- [[concepts/Query String|Query String]]
- [[concepts/HTTP/2|HTTP/2]]
- [[concepts/Progressive attachment|Progressive attachment]]
- [[concepts/静态链接|静态链接]]
- [[concepts/RPC|RPC]]
- [[concepts/glog|glog]]
- [[concepts/tcmalloc|tcmalloc]]

## 概述
brpc是一个高性能RPC框架，支持HTTP/h2服务。它通过proto文件定义服务接口，并使用Controller对象访问HTTP请求和响应的头信息与体数据。brpc的HTTP实现基于[[entities/node.js|Node.js HTTP解析器]]和[[entities/rapidjson|rapidjson]]，保证了高效的性能。

## 功能特性
- 支持三种URL映射方式：/ServiceName/MethodName、/ServiceName前缀以及[[concepts/RESTful URL|RESTful风格]]
- 支持[[concepts/Gzip压缩|Gzip压缩]]和渐进式发送（[[concepts/Progressive attachment|Progressive attachment]]）
- 提供[[concepts/Server-Sent Events|Server-Sent Events]]和[[concepts/Chunked transfer encoding|分块传输编码]]功能
- 支持[[concepts/HTTP/2|HTTP/2]]协议（brpc中称为"h2"）
- 被广泛用于需要HTTP协议的场景，尤其是移动产品

## 使用方式
用户通过.proto文件定义服务，声明空请求和响应的接口来创建http/h2服务。brpc提供Controller对象用于访问HTTP请求的头信息、Query String、Body数据以及状态码等。

## Mentions in Source
> **Source: [[sources/en_http_service|en_http_service]]**
> - "This document talks about ordinary http/h2 services rather than protobuf services accessible via http/h2."
> - "brpc names the HTTP/2 protocol to 'h2', no matter encrypted or not."
> - "http/h2 services in brpc have to declare interfaces with empty request and response in a .proto file."

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "brpc prefers static linkages of deps, so that they don't have to be installed on every machine running the app."
> - "brpc depends on following packages: gflags, protobuf, leveldb."
> - "Compile brpc with config_brpc.sh: git clone brpc, cd into the repo and run sh config_brpc.sh --headers=/usr/include --libs=/usr/lib"