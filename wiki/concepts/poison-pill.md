---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-minimum-required-edition|editions-minimum-required-edition]]"]
tags: [method]
aliases:
  - "Poison Pill"
  - "毒丸机制"
---


# Poison Pill

## 定义
毒丸机制（Poison Pill）是一种版本控制语境下的兼容性策略。其核心做法是在描述符中嵌入版本信息（例如 Edition 编号），使得旧版运行时在遇到自身无法理解的"过新"描述符时直接拒绝加载，从而避免因解析未知特性而产生未定义行为或数据损坏。Protobuf Editions 按年递增的特性使其天然适合充当毒丸——运行时需要定期更新以支持新版本的 edition，否则将无法加载新编译的描述符。

## 关键特征
- **拒绝式兼容策略**：旧版运行时遇到"过新"描述符时主动拒绝加载，而非尝试兼容解析
- **嵌入版本信息**：在描述符中携带版本标记（如 Edition 编号），作为判断"过新"的依据
- **天然递增的版本号**：Protobuf Editions 按年递增，使版本号自然单调上升，无需额外设计
- **无需运行时特性探测**：运行时不需实现复杂的特性探测逻辑，仅通过版本号比对即可决定是否加载
- **强制运行时更新**：促使消费者定期升级运行时以支持最新版本的描述符

## 应用
- **Protobuf Editions 版本兼容控制**：利用 Edition 编号作为毒丸，使旧版运行时在加载超过其支持范围的 edition 描述符时直接失败
- **描述符加载的前置校验**：在运行时解析任何描述符之前，先校验其携带的版本信息是否在自身支持范围内
- **分布式系统中的服务兼容性管理**：编译期嵌入版本号，部署期通过运行时加载行为自动隔离不兼容的组件

## 相关概念
- [[concepts/minimum-required-edition|Minimum Required Edition]]
- [[concepts/edition|Edition]]

## 相关实体
- [[entities/protobuf-editions|Protobuf Editions]]
- [[entities/protobuf|Protobuf]]

## 来源提及
- "we can use them as a poison pill for old runtimes that try to load descriptors that are 'too new.'" — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]
- "Rather than using the editions value, use some other version number." — [[sources/editions-minimum-required-edition|editions-minimum-required-edition]]