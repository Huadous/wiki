---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client|http_client]]"]
tags: [project]
aliases:
  - "http_client.cpp 示例"
  - "brpc HTTP 客户端示例"
  - "example/http_c++"
---


# example/http_c++

## 基本信息
- Type: project
- Source: [[sources/http_client|http_client]]

## 描述

example/http_c++ 是 [[entities/brpc|brpc]] 官方仓库中提供的 HTTP 客户端示例代码，位于 `example/http_c++/http_client.cpp` 路径下。该示例作为 [[sources/http_client|http_client]] 文档的参考实现，展示了 brpc HTTP/H2 客户端的标准用法。文档以该示例作为引导读者入门的起点，并基于其代码结构展开后续 Channel 创建、GET、POST 等操作的详细说明。

作为官方推荐的入门示例，example/http_c++ 涵盖了 brpc 客户端编程的核心要素：包括 [[concepts/channel|Channel]] 对象的构造与选项配置、HTTP/H2 协议下的同步与异步请求发送、响应的解析与错误处理等。该示例代码不仅是初学者理解 brpc 客户端 API 的入口，也是验证本地构建环境是否正确的快速参考。

## 相关实体

- [[entities/brpc|brpc]]

## 相关概念

- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/channel|Channel]]

## 来源提及

- [example/http_c++](https://github.com/apache/brpc/blob/master/example/http_c++/http_client.cpp) — [[sources/http_client|http_client]]