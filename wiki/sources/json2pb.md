---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/json2pb.md]]"
tags: [JSON-protobuf转换规则, repeated字段JSON编码, JSON map编码, Unknown fields处理, Pb2JsonOptions, base64编码, IEEE754浮点数, HTTP+JSON访问protobuf模式]
aliases: ["brpc json2pb转换规则", "JSON与protobuf双向转化"]
---

# brpc json2pb: JSON与protobuf双向转化规则 - Summary

## 来源
- Original file: [[brpc/json2pb.md]]
- Ingested: 2026-06-13

## 核心内容
本文介绍了 [[entities/brpc|brpc]] 框架中 [[entities/json2pb|json2pb]] 子模块对 JSON 与 [[entities/protocol-buffers|Protocol Buffers]] 之间双向转化的支持。brpc 使用 [[entities/rapidjson|rapidjson]] 作为底层 JSON 解析器，对 protobuf 2.x 和 3.x 两个版本均有效。由于通过 HTTP+JSON 访问 protobuf 服务是对外服务的常见方式（详见 [[concepts/http+json访问protobuf模式|HTTP+JSON访问protobuf模式]]），转化规则必须精准。文档详细列举了各类型对应规则：message 对应 JSON Object，repeated 字段对应 JSON Array（支持 [[concepts/repeated字段json编码|single_repeated_to_array]] 优化），满足特定条件的 repeated message 被视为 [[concepts/json-map编码|JSON map]]；整数类型自动适配并识别溢出，浮点数接受 NaN、Infinity 等特殊字符串（遵循 [[concepts/ieee754浮点数|IEEE754]] 标准）；bytes 默认 [[concepts/base64编码|base64]] 编码；enum 转换形式由 [[concepts/pb2jsonoptions|Pb2JsonOptions]] 控制。[[concepts/unknown-fields处理|Unknown fields]] 的双向转换目前均不支持。

## 关键实体
- [[entities/brpc|brpc]] — Apache 开源 RPC 框架，json2pb 的宿主项目
- [[entities/json2pb|json2pb]] — brpc 子模块，源码位于 src/json2pb/
- [[entities/rapidjson|rapidjson]] — JSON 解析库，提供类型标记能力
- [[entities/protocol-buffers|Protocol Buffers]] — Google 开发的结构化数据序列化格式
- [[entities/brpccontroller|brpc::Controller]] — 提供 set_pb_single_repeated_to_array() 启用开关

## 关键概念
- [[concepts/json-protobuf转换规则|JSON-protobuf转换规则]] — 各类型与 JSON 的精准映射机制
- [[concepts/repeated字段json编码|repeated字段JSON编码]] — repeated 字段对应 Array，支持单字段优化
- [[concepts/json-map编码|JSON map编码]] — 满足条件的 repeated message 被视为 map
- [[concepts/unknown-fields处理|Unknown fields处理]] — 目前不支持，根因是字段数字标识缺失
- [[concepts/pb2jsonoptions|Pb2JsonOptions]] — 控制 enum 转换形式的配置对象
- [[concepts/base64编码|base64编码]] — bytes 类型的默认编码方式
- [[concepts/ieee754浮点数|IEEE754浮点数]] — 浮点数转换遵循的标准
- [[concepts/http+json访问protobuf模式|HTTP+JSON访问protobuf模式]] — brpc 对外服务的常见方式

## 要点
- brpc 通过 [[entities/json2pb|json2pb]] 实现 JSON 与 protobuf 的双向转换，支持 protobuf 2.x 和 3.x，使用 [[entities/rapidjson|rapidjson]] 作为解析器
- message 对应 JSON Object（花括号），repeated 字段对应 JSON Array（方括号），元素递归解析
- 满足三个条件（key 字段 tag=1、value 字段 tag=2、无其他字段）的 repeated message 被视为 JSON map，且与 protobuf 3.x map 二进制兼容
- rapidjson 的类型标记机制使整数类型自动适配，overflow 和 underflow 自然被识别为转化失败
- 浮点数除普通数字外接受 "NaN"、"Infinity"、"-Infinity" 三个字符串；bytes 字段默认 base64 编码
- unknown_fields 双向转换均不支持，根本原因是 protobuf 的 key 是字段后的数字标识而非字段名