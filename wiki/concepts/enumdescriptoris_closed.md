---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]"]
tags: [method]
aliases:
  - "is_closed"
  - "EnumDescriptor.is_closed()"
  - "EnumDescriptor::is_closed()"
---


# EnumDescriptor::is_closed

## 定义
`EnumDescriptor::is_closed()` 是 Protocol Buffers Editions 提案（Tier 1 C++ API）中新引入的布尔方法，定义于 `EnumDescriptor` 类中。该方法用于判断某个枚举类型是否为 proto2 风格的封闭枚举（closed enum），其返回值直接表达枚举的"封闭性"语义，而非通过语法版本间接推断。

## 关键特征
- **C++ 端点 API**：声明为 `bool is_closed() const;`，返回布尔值，无参数。
- **语义与语法版本解耦**：返回值仅反映"封闭/开放"行为，不依赖于 `syntax() == PROTO3` 这类基于语法版本的反向判断。
- **替代旧检测模式**：在迁移策略中被明确指定为"封闭/开放枚举"用途的目标 API，用以取代依赖 `syntax()` 的间接判断方式。
- **Tier 1 新增接口**：作为提案 Tier 1 中的新方法之一，与 Editions 体系下的其他判定类 API 一同引入。
- **面向 Edition Zero 演进**：服务于使行为语义独立于 `proto2` / `proto3` 语法标签的关键设计目标。

## 应用
- **代码迁移**：将现有通过 `syntax() == PROTO3`（或等价逻辑）判断"开放枚举"的代码，迁移到 `is_closed()` 上，从而获得与语法版本无关的稳定语义。
- **运行时判定**：在反射、动态消息处理或代码生成产物中，根据枚举封闭性选择不同的序列化或校验路径。
- **API 现代化**：作为 Editions 体系 Tier 1 C++ API 的一部分，统一封闭/开放枚举的访问方式。

## 相关概念
- [[concepts/proto2-syntax|proto2 syntax]]
- [[concepts/syntax-deprecation-migration|syntax() deprecation migration]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-zero|Edition Zero]]

## 来源提及
- `class EnumDescriptor { // Returns whether this enum is a proto2-style closed enum. bool is_closed() const; };` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]
- `2. Closed/open enum (use new API).` — [[sources/editions-cpp-apis-for-edition-zero|editions-cpp-apis-for-edition-zero]]