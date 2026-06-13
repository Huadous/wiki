---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [other]
aliases:
  - "plugin.proto"
  - "Protocol Buffers plugin.proto"
  - "protoc plugin protocol"
---


# plugin.proto

## 基本信息
- Type: other
- Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]

## 描述
plugin.proto 是 Protocol Buffers 中用于定义代码生成器插件协议的 protobuf 文件,它规定了 [[entities/protoc|protoc]] 与外部代码生成器之间通信的消息格式。该文件定义了 `CodeGeneratorRequest` 和 `CodeGeneratorResponse` 两个核心消息,作为 protoc 与插件进程之间通过 stdin/stdout 交换数据的协议基础。文档指出,基于原始 `CodeGeneratorRequest` 和 `CodeGeneratorResponse` 消息(而非 C++ `CodeGenerator` 框架)实现代码生成器时,需要通过 `response.set_supported_features()` 显式声明对 [[concepts/feature-proto3-optional|FEATURE_PROTO3_OPTIONAL]] 的支持,否则 [[entities/protoc|protoc]] 会报错提示代码生成器尚未更新以支持 [[concepts/proto3-optional-fields|proto3 optional fields]]。该文件由 [[entities/google-gnostic|Google]] 维护,是 protoc 插件生态的核心协议定义。

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/google-gnostic|Google]]

## 相关概念
- [[concepts/feature-proto3-optional|FEATURE_PROTO3_OPTIONAL]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/codegenerator-framework|CodeGenerator framework]]

## 来源提及
- "If you are generating code using raw `CodeGeneratorRequest` and `CodeGeneratorResponse` messages from `plugin.proto`, the change will be very similar:" — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- ```
  void GenerateResponse() {
    CodeGeneratorResponse response;
    response.set_supported_features(CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL);
  ``` — [[sources/implementing_proto3_presence|implementing_proto3_presence]]