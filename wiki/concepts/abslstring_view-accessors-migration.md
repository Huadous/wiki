---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition|editions-life-of-an-edition]]"]
tags: [method]
aliases:
  - "string_view accessors migration"
  - "legacy_string migration"
  - "absl::string_view Accessors 迁移"
---


# absl::string_view Accessors migration

## 定义
absl::string_view Accessors 迁移是源文档中记载的四大大规模变更模板之一，专注于将 C++ 中 `string` 和 `bytes` 类型字段的访问器返回值从 `const std::string&` 迁移到 `absl::string_view`。该迁移过程通过引入 `features.(proto.cpp).legacy_string` 特性，并在文件或字段粒度上设置该特性以最小化代码差异；待内部改动完成约 95% 后，于下一个 Edition 升级 C++ 后端使该特性默认值为 false；最终在遗留访问器全部消除后彻底移除该特性。

## 关键特征
- 属于四大大规模变更（Large-scale Change）模板之一，针对 C++ 后端 string/bytes 字段访问器返回类型的优化迁移
- 引入 `features.(proto.cpp).legacy_string` 特性（language-scoped feature），用于控制旧版返回 `const std::string&` 的访问器行为
- 特性可在文件级或字段级粒度进行设置，借助工具链将代码差异影响降至最低
- 阶段性推进：先内部灰度 → Edition 升级时将默认值翻转为 false → 遗留代码清零后彻底移除特性
- 解决的是 C++ 中 `const std::string&` 返回值带来的拷贝等已知性能损耗问题

## 应用
- Protobuf C++ 生成的访问器代码中，将 `string`/`bytes` 字段的 getter 返回类型从 `const std::string&` 改为 `absl::string_view`，以减少不必要的内存拷贝
- 在 Protobuf Editions 体系中，配合 Edition 升级节点推进语言后端默认行为的演进
- 作为大规模迁移的样板方法，可参考其"特性门控 + 渐进推进 + 最终移除"的生命周期管理模式

## 相关概念
- [[concepts/features.(proto.cpp).legacy_string|features.(proto.cpp).legacy_string]]
- [[concepts/Large-scale Change|Large-scale Change]]
- [[concepts/Language-scoped features|Language-scoped features]]

## 相关实体
（无相关实体）

## 来源提及
- "In C++, a `string` or `bytes` typed field has accessors that produce `const std::string&`s. The missed optimizations of doing this are well-understood, so we won't rehash that discussion." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "Once we have applied 95% of internal changes, we will upgrade the C++ backend at the next edition to default `legacy_string` to false in the new edition." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]