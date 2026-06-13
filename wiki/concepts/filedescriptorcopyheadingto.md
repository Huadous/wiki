---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]"]
tags: [method]
aliases:
  - "CopyHeadingTo"
  - "FileDescriptor::CopyHeadingTo"
---


# FileDescriptor::CopyHeadingTo

## 定义
`FileDescriptor::CopyHeadingTo(FileDescriptorProto*)` 是 Protocol Buffers（protobuf）Editions 提案 Tier 1 中新增的 C++ 方法，定义于 `descriptor.h` 中的 `FileDescriptor` 类。该方法用于将源文件描述符中的 `package`、`syntax`、`edition`、`dependencies` 以及文件级 `options` 复制到目标 `FileDescriptorProto` 实例中。其设计目的是简化在自定义修改描述符之前复制 proto 文件头部信息的常见且容易出错的操作模式。

## 关键特征
- 签名：`void CopyHeadingTo(FileDescriptorProto*) const;`，属于 `FileDescriptor` 类的 const 成员方法。
- 复制范围明确限定为文件头部字段：`package`、`syntax`、`edition`、`dependencies`、文件级 `options`。
- 是提案 Tier 1 中纳入了四个新增 API 之一，旨在消除调用方手动处理这些头部字段时的潜在错误。
- 仅负责头部信息的复制，不涉及 message、field、enum 等描述符体的拷贝。

## 应用
- 当用户需要在 `FileDescriptor` 基础上对内部描述符做自定义处理（例如修改 message、field、enum）时，先用 `CopyHeadingTo` 将原始文件头部写入目标 `FileDescriptorProto`，再进行后续修改。
- 适用于基于 protobuf 反射机制或代码生成器构建的二次工具，避免手动逐字段拷贝 `package`、`syntax`、`edition`、`dependencies`、`options`。
- 在 [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]] 提案中作为面向 Edition Zero 的 C++ API 一部分被引入，配套支持 [[entities/Edition Zero|Edition Zero]] 场景下 descriptors 的处理。

## 相关概念
- [[concepts/syntax-deprecation-migration|syntax() deprecation migration]]
- [[concepts/proto2-syntax|proto2 syntax]]

## 相关实体
- [[entities/Protocol Buffers|Protocol Buffers]]
- [[entities/Edition Zero|Edition Zero]]

## 来源提及
- `class FileDescriptor { // Copies package, syntax, edition, dependencies, and file-level options. void CopyHeadingTo(FileDescriptorProto*) const; };` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]
- `CopyHeadingTo is intended to simplify the common, easy-to-get-wrong pattern of copying the heading of a proto file before doing custom manipulation of descriptors within.` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]