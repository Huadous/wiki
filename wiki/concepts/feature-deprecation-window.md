---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [term]
aliases:
  - "Deprecation Window"
  - "功能弃用窗口"
---


# Feature Deprecation Window

## 定义
Feature Deprecation Window（特征弃用窗口）是 Protobuf Editions 生命周期中从特征被标记为弃用到最终移除之间的缓冲阶段。在该窗口期内，编译器会发出弃用警告，但不会强制用户升级，外部用户可以继续使用旧特征，从而获得从容迁移的时间。

## 关键特征
- **非破坏性警告**：弃用窗口期间，编译器仅发出弃用警告，不会阻止编译或运行。
- **外部用户缓冲**：内部迁移完成后，才会向外部用户开放弃用窗口，外部用户可在该窗口内继续使用旧特征。
- **分阶段移除**：弃用标记与移除动作分别在两个不同的 Edition 中执行。
- **内部强制优先**：内部团队通过 allowlist 机制管控旧特征的使用，确保最难迁移的案例先被处理后再公开弃用。
- **时长未严格限定**：弃用窗口的具体时长未在源文件中明确定义，取决于迁移完成进度。

## 应用
- **Protobuf Editions 特征生命周期管理**：在发布新 Edition 时，对需要移除的旧特征先进行弃用标记，给予用户至少一个 Edition 版本的迁移窗口。
- **内部大规模迁移协调**：当大型代码库（如 Google 内部 Protobuf 用户）需要移除旧特征时，利用弃用窗口让不同团队按节奏完成迁移。
- **借鉴 Rust 语言实践**：该机制设计参考了 Rust 的弃用策略，旨在最小化对用户生产环境的影响。

## 相关概念
- [[concepts/Feature-Lifecycle|Feature Lifecycle]]
- [[concepts/Edition|Edition]]
- [[concepts/Feature|Feature]]
- [[concepts/Incremental-Migration|Incremental Migration]]

## 相关实体
- [[entities/protobuf-team|protobuf-team]]

## 来源提及
- "Internally, `features.(pb.cpp).opaque_repeated_fields` usage will be blocked with allowlists while we remove the hardest to migrate case." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Externally, `features.(pb.cpp).opaque_repeated_fields` will be marked deprecated in a public edition and removed in a later one." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]