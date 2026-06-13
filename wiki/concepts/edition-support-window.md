---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-lifetimes|editions-edition-lifetimes]]"]
tags: [term]
aliases:
  - "Edition Support Range"
  - "edition support window"
---


# Edition Support Window

## 定义
Edition Support Window（Edition 支持窗口）是指一个二进制文件（如 protoc 自身或任意 generator 插件）所声明支持的 Edition 范围。由于每个 generator 插件和 protoc 都会声明自身的 Edition 支持窗口，客户端可以据此拒绝处于窗口范围之外的 proto 文件，从而使新 Edition 的引入在当下能够被较好地处理。Edition 支持窗口同时约束了 OSS 等无法强制升级 proto 的场景下，与某 Edition 绑定的特性代码何时可以被安全地清理（垃圾回收），以及运行时所能识别的最大 Edition。

## 关键特征
- **声明式范围**：每个二进制文件（protoc 或 generator 插件）显式声明其最低支持 Edition 与最高支持 Edition。
- **客户端校验依据**：客户端利用该窗口判断输入的 proto 是否落在二进制可处理的 Edition 范围内，超出范围即拒绝。
- **新 Edition 引入的容错机制**：因为存在声明窗口，引入新 Edition 在当下已得到良好处理，无需依赖隐式兼容性假设。
- **移除 Edition 的方式**：移除对一个 Edition 的支持，本质上等价于在一次 breaking release 中提升二进制的最低支持 Edition。
- **特性-Edition 绑定的约束**：当特性支持直接绑定到 Edition 时，Edition 支持窗口决定了特性相关代码可以安全清理（GC）的时机。
- **OSS 场景的关键约束**：在无法强制用户升级 proto 的开源生态中，Edition 支持窗口成为运行时能识别的最大 Edition 的硬性上限。

## 应用
- **protoc 与 generator 插件的版本协商**：当用户传入某个 Edition 的 proto 时，工具链依据各二进制声明的 Edition Support Window 校验兼容性。
- **Edition 演进决策**：在提案 [[sources/editions-edition-lifetimes|editions-edition-lifetimes]] 中，决定是否、何时、如何下线一个旧 Edition，需要评估其对下游各二进制 Edition Support Window 的影响。
- **特性代码生命周期管理**：当一个特性仅在特定 Edition 范围内生效时，Edition Support Window 给出了特性实现代码可被移除（GC）的时间窗口下界。
- **运行时的 Edition 上限界定**：运行时（runtime）所能识别、解析的最大 Edition 受限于其 Edition Support Window 的上界。
- **Breaking Release 规划**：提升最低支持 Edition 通常被归类为 breaking 变更，需要在主版本升级中处理。

## 相关概念
- [[concepts/Editions|Editions]]
- [[concepts/Feature-Removal|Feature Removal]]
- [[concepts/Dynamic-Messages|Dynamic Messages]]
- [[concepts/Behavior-Preserving-Editions|Behavior-Preserving Editions]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Because every generator plugin (and protoc) advertises its edition support window, introducing a new Edition is well-handled today." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]
- "Dropping support for an edition doesn't really mean that much today. We *could* do it simply by bumping up the minimum supported edition of a binary in a breaking release." — [[sources/editions-edition-lifetimes|editions-edition-lifetimes]]