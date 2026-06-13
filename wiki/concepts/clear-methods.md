---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/field_presence]]"]
tags: [method]
aliases:
  - "clear methods"
  - "clear_foo"
  - "ClearField"
---


# Clear methods

## 定义
Clear methods 是 Protocol Buffers 生成 API 中的一类与显式存在（explicit presence）配套使用的方法，名称形如 `clear_foo` 或 `ClearField('foo')`（不同语言命名风格略有不同）。在显式存在语义下，要将一个字段"未设置"（即取消其显式存在状态），必须通过调用该字段对应的 clear 方法，而不是将字段赋值为默认值。

## 关键特征
- 与显式存在语义绑定：仅在使用 explicit presence（`optional` 标签或 editions 中的显式存在特性）的字段上生成
- 命名风格因语言而异：C++ 生成 `clear_foo()`，Java/Python 生成 `clear_foo()` / `ClearField('foo')`，C# 生成 `ClearField()` 等
- 语义明确为"取消显式存在状态"：将字段从"已设置"变回"未设置"，而非将其置为默认值
- 与 hazzer methods（`has_foo`）共同构成显式存在 API 的两大支柱，二者配对使用以查询和修改字段的存在状态
- 不允许通过赋默认值来"清除"字段：在显式存在语义下，赋值默认值得出的仍是"已设置默认值的字段"

## 应用
- 在 C++、C#、Java、Python、Ruby 等多种语言的示例代码中反复出现，是显式存在使用模式的核心组成部分
- 典型用法示例：`m.clear_foo();` 用于清除（unset）消息 `m` 中的 `foo` 字段
- 在应用代码中替代"将字段设为默认值"的旧式清除做法，配合 hazzer 方法判断字段是否存在
- 在 Proto3 中通过 `optional` 关键字引入显式存在后，clear 方法成为管理字段存在状态的标准途径
- 在 Protocol Buffers Editions 中，作为显式存在特性（explicit presence feature）启用后自动生成的辅助方法之一

## 相关概念
- [[concepts/hazzer-methods|Hazzer methods]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/field-presence|Field presence]]
- [[concepts/optional-label|`optional` label]]

## 相关实体
（暂无相关实体）

## 来源提及
- A generated `clear_foo` method must be used to clear (i.e., un-set) the value. — [[sources/field_presence]]
- Use the generated "hazzer" methods and "clear" methods in application code, instead of comparing or setting default values. — [[sources/field_presence]]
- `// Clear the field:
m.clear_foo();` — [[sources/field_presence]]