---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/json2pb|json2pb]]"]
tags: [standard]
aliases:
  - "IEEE 754"
  - "IEEE754标准"
  - "IEEE 754浮点数标准"
---


# IEEE754浮点数

## 定义
IEEE754 是 [[entities/json2pb|json2pb]] 模块在处理 Protocol Buffers 浮点类型（float、double）与 JSON 之间相互转换时所遵循的二进制浮点数表示标准。该标准除了接受普通数字字面量（如 3.14）之外，还定义了几个特殊值——NaN（Not A Number）、Infinity（正无穷）、-Infinity（负无穷）。由于标准 JSON 格式本身无法直接表示这些非有限数值，[[entities/json2pb|json2pb]] 改以字符串形式（"NaN"、"Infinity"、"-Infinity"）对这些特殊值进行接受和输出。

## 关键特征
- 标准化二进制浮点数表示规范，覆盖普通数值与特殊非有限值
- 定义三个特殊值：NaN（Not A Number）、Infinity（正无穷）、-Infinity（负无穷）
- 在 [[entities/json2pb|json2pb]] 中，特殊值以字符串而非数字字面量的方式在 JSON 中表示
- 支持 JSON 整数类型（Int、UInt、Int64、Uint64）灵活转换至 [[entities/protocol-buffers|Protocol Buffers]] 浮点类型（float、double），扩展了类型间互转范围
- 在 [[entities/rapidjson|rapidjson]] 侧对应的类型为 Float、Double、Int、Uint、Int64、Uint64

## 应用
- [[entities/json2pb|json2pb]] 模块在 JSON 与 [[entities/protocol-buffers|Protocol Buffers]] 双向转换时遵循 IEEE754 规范对浮点数进行解析和序列化
- 处理接口请求或响应中可能出现的 NaN、Infinity、-Infinity 等非有限数值
- 在需要将整型字段临时以浮点形式表达的业务场景中，提供跨整数与浮点类型的灵活转换能力

## 相关概念
- [[concepts/json-protobuf转换规则|JSON-protobuf转换规则]]
- [[concepts/floating-point|Floating Point]]

## 相关实体
- [[entities/rapidjson|rapidjson]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/json2pb|json2pb]]

## 来源提及
- 浮点数(IEEE754)除了普通数字外还接受"NaN", "Infinity", "-Infinity"三个字符串，分别对应Not A Number，正无穷，负无穷。 — [[sources/json2pb|json2pb]]
- json的整数类型也可以转至pb的浮点数类型。 — [[sources/json2pb|json2pb]]
- ```
  // protobuf
  float double
  
  // rapidjson
  Float Double Int Uint Int64 Uint64
  ``` — [[sources/json2pb|json2pb]]