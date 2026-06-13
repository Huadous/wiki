---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [method]
aliases:
  - "validation layers"
  - "运行时验证层"
---


# Validation Layer

## 定义
Validation Layer（验证层）是源文档中针对支持动态消息（Dynamic Messages）的运行时所提出的一种运行时侧检查机制。其目标是确保在运行时不会处理那些携带了"在特性版本存在窗口之外被覆写"（features overridden outside their edition existence window）的无效描述符（descriptor）。该验证层通过在 `FeatureSetEditionDefault` 中新增两个字段 —— `overridable_features` 与 `fixed_features` —— 来启用，同时保留原有的 `features` 字段以供迁移过渡使用。

## 关键特征
- **面向动态消息运行时**：仅在支持 dynamic messages 的 runtime 中启用，作为运行时的额外检查层。
- **新增 FeatureSet 字段**：在 `FeatureSetEditionDefault` 中扩展 `overridable_features` 与 `fixed_features` 两个字段；原有 `features` 字段被临时保留以支持迁移。
- **剥离未知字段与不支持的扩展**：推荐算法首先从入站 `FeatureSet` 中剥离未知字段以及不受支持的扩展。
- **合并可覆写的默认值并断言相等**：将剥离后的 `FeatureSet` 与 overridable 默认值合并，然后进行相等性断言。
- **最小化反射开销**：该方案尽可能减少运行时的反射工作量，条件是每个 feature 仍是标量值（scalar value）。
- **依赖 protoc 的编译产物**：运行时与编译器共享 `protoc` 编译产出的默认 IR，可在 IR 中打包尽量多的信息以减少重复。

## 应用
- 在支持 dynamic messages 的 protobuf runtime（如 upb）中对接收或构造的描述符进行合法性校验，拦截跨 edition 生命周期被非法覆写的 FeatureSet。
- 作为 editions 迁移期的安全网：即便 descriptor 由旧版工具链生成，也能在运行时识别并拒绝非法覆写。
- 配合 `protoc` 编译输出的 defaults IR 做客户端侧校验，减少运行时反射调用、降低对反射 API 的依赖。

## 相关概念
- [[concepts/Dynamic Messages|Dynamic Messages]]
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/FeatureSetEditionDefault|FeatureSetEditionDefault]]
- [[concepts/Reflection-Based Validation|Reflection-Based Validation]]
- [[concepts/Predictability|Predictability]]
- [[concepts/Feature Lifetimes|Feature Lifetimes]]

## 相关实体
- [[entities/protoc|protoc]]
- [[entities/upb|upb]]

## 来源提及
- "We likely will want to add validation layers to runtimes that support dynamic messages though, to make sure there are no invalid descriptors floating around." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "Since they all have access to protoc's compiled defaults IR, we can pack as much information in there as possible to minimize duplication." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]