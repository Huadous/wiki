---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [term]
aliases:
  - "FEATURE_PROTO3_OPTIONAL"
  - "Proto3 Optional Feature Flag"
---


# FEATURE_PROTO3_OPTIONAL

## 定义
FEATURE_PROTO3_OPTIONAL 是 [[entities/codegeneratorresponse|CodeGeneratorResponse]] 中定义的一个特性标志常量（feature flag）。代码生成器（[[concepts/Code Generator|Code Generator]]）需要通过返回该标志向 [[entities/protocol-buffers-documentation|protoc]] 声明自身已支持 [[concepts/proto3 optional fields|proto3 optional fields]]。其设计目的是避免未更新的旧代码生成器在不知情的情况下继续生成带有合成 oneof 访问器（synthetic oneof accessors）的已废弃 API，从而防止对历史迁移路径造成污染。

## 关键特征
- 是一个位于 [[entities/codegeneratorresponse|CodeGeneratorResponse]] 中的整型特性常量，由插件协议通过 `supported_features` 字段回传给 [[entities/protocol-buffers-documentation|protoc]]。
- 是一种显式的“能力声明”机制：插件必须主动声明支持，否则 [[entities/protocol-buffers-documentation|protoc]] 不会启用相关功能。
- 区分了两种声明方式：C++ `CodeGenerator` 框架下通过重写 `GetSupportedFeatures()` 方法返回该标志；或在使用原始 [[entities/plugin-proto|plugin.proto]] 协议时调用 `response.set_supported_features(...)`。
- 起到兼容性与防退化（anti-deprecation）双重作用：阻止旧插件在新版 [[entities/protocol-buffers-documentation|protoc]] 下意外产生合成 oneof 的废弃 API，从而保护后续迁移路径。

## 应用
- 在基于 C++ 编写的 Protocol Buffers 代码生成器中，通过重写 `google::protobuf::compiler::CodeGenerator::GetSupportedFeatures()` 方法，使其返回 `FEATURE_PROTO3_OPTIONAL`，向 [[entities/protocol-buffers-documentation|protoc]] 通报已支持 proto3 optional 字段。
- 在基于原始 [[entities/plugin-proto|plugin.proto]]（如其他语言实现的）插件协议中，通过构造 [[entities/codegeneratorresponse|CodeGeneratorResponse]] 并调用 `response.set_supported_features(CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL)` 完成相同的声明。
- 用于在大型代码库迁移至 proto3 optional / [[sources/editions|Editions]] 时，统一所有插件以避免产生带有合成 oneof 的废弃访问器。

## 相关概念
- [[concepts/Code Generator|Code Generator]]
- [[concepts/proto3 optional fields|proto3 optional fields]]

## 相关实体
- [[entities/codegeneratorresponse|codegeneratorresponse]]
- [[entities/plugin-proto|plugin-proto]]
- [[entities/protocol-buffers-documentation|protoc]]（参考 sources 中 protoc 相关条目）

## 来源提及
- "To signal that your code generator supports `optional` fields in proto3, you need to tell `protoc` what features you support." — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "return FEATURE_PROTO3_OPTIONAL;" — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- "response.set_supported_features(CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL);" — [[sources/implementing_proto3_presence|implementing_proto3_presence]]