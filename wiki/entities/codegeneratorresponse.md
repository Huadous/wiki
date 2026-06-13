---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/implementing_proto3_presence|implementing_proto3_presence]]"]
tags: [other]
aliases:
  - "CodeGeneratorResponse message"
  - "CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL"
---


# CodeGeneratorResponse

## 基本信息
- Type: other
- Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]

## 描述
CodeGeneratorResponse 是 [[entities/plugin-proto|plugin.proto]] 中定义的一个 proto 消息,是 protoc 代码生成器插件用于将生成的代码返回给 protoc 的标准响应消息。该文档指出,当开发者直接使用原始的 `CodeGeneratorRequest` 和 `CodeGeneratorResponse` 消息(而非基于 C++ `CodeGenerator` 框架)来实现代码生成时,生成器必须通过 `set_supported_features` 方法设置 `supported_features` 字段,以声明其对 proto3 optional 字段的支持。这一调用通过 `response.set_supported_features(CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL);` 完成。该机制与基于 C++ `CodeGenerator` 框架构建的插件中所使用的 `GetSupportedFeatures()` 覆写方法相平行,是 protoc 允许生成器处理包含 proto3 optional 字段的文件所必需的,否则会抛出 "hasn't been updated to support optional fields in proto3" 错误。

## 相关实体
- [[entities/plugin-proto|plugin.proto]]
- [[entities/protoc|protoc]]

## 相关概念
- [[concepts/feature-proto3-optional|FEATURE_PROTO3_OPTIONAL]]
- [[concepts/code-generator|Code Generator]]
- [[concepts/codegenerator-framework|CodeGenerator framework]]

## 来源提及
- If you are generating code using raw `CodeGeneratorRequest` and `CodeGeneratorResponse` messages from `plugin.proto`, the change will be very similar: — [[sources/implementing_proto3_presence|implementing_proto3_presence]]
- ```cpp
void GenerateResponse() {
  CodeGeneratorResponse response;
  response.set_supported_features(CodeGeneratorResponse::FEATURE_PROTO3_OPTIONAL);

  // Generate code...
}
— [[sources/implementing_proto3_presence|implementing_proto3_presence]]