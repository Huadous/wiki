---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-stricter-schemas-with-editions.md]]"]
tags: [standard]
aliases:
  - "loose bool options"
  - "Strict Boolean Options"
---


# Strict Boolean Options

## 定义
严格布尔选项（Strict Boolean Options）是 Protobuf Editions 提案中的一项语言标准化措施，旨在收紧布尔类型选项（boolean options）的取值语法，只允许 `true` 和 `false` 两个字面量，拒绝当前在 `option` 语句中合法但宽松的 `True`、`False`、`T`、`F` 等变体形式。该变更通过 `features.loose_bool_options` 特性标志进行门控，是利用 Editions 机制对语言进行渐进式收紧的典型示例。

## 关键特征
- **取值收窄**：布尔选项的值语法由当前的 `true / false / True / False / T / F` 收紧为只接受 `true / false`。
- **特性门控**：通过 `features.loose_bool_options` 控制行为，初始默认值为 `true`（保持向后兼容），在未来的 edition 中切换为 `false`（启用严格模式）。
- **渐进式过渡**：依赖 Protobuf Editions 机制，使得旧 proto 文件仍然可以解析，而新 edition 文件则启用更严格的校验。
- **错误信息示例**：当前合法的写法 `option my_bool = T;` 在严格模式下将被拒绝。

## 应用
- 在新一代 Protobuf Editions 中作为默认的布尔选项语法规范，统一代码风格并减少歧义。
- 在 protobuf 编译器（protoc）中对 option 解析器进行校验，确保仅接受规范的 `true` / `false` 字面量。
- 作为 Editions 特性门控模式的参考案例：先以 feature flag 默认开启（兼容旧行为），再在后续 edition 中默认关闭（启用严格行为）。
- 在 IDE、lint 工具和代码生成器中提示用户使用规范的布尔字面量，避免在不同工具链下产生解析差异。

## 相关概念
- [[concepts/feature-gating|Feature Gating]]
- [[concepts/protobuf-editions|Protobuf Editions]]

## 相关实体
- [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- [[sources/editions|editions]]
- [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- [[sources/features|features]]

## 来源提及
- Boolean options can use true, false, True, False, T, or F as a value: `option my_bool = T;`. We should restrict to only `true` and `false`. — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]
- We would introduce a feature like `features.loose_bool_options`, which would switch from true to false. — [[sources/editions-stricter-schemas-with-editions|editions-stricter-schemas-with-editions]]