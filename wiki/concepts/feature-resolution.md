---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-legacy-syntax-editions]]"]
tags: [method]
aliases:
  - "feature resolution"
  - "功能解析"
---


# Feature Resolution

## 定义
Feature Resolution（功能解析）是指在 Protocol Buffers 中，根据给定的 edition 或 syntax，为每一个 feature（功能）确定其实际生效值的过程。该机制将底层的 syntax（语法）与上层的功能配置联系起来，是 Editions 体系中 FeatureSet 生命周期管理的关键环节。在将 proto2/proto3 视为特殊 edition 的方案下，Feature Resolution 必须能够作用于这些 legacy syntax，从而保证 descriptor 在不同版本之间的一致性。

## 关键特征
- **输入驱动**：以给定的 edition 或 syntax 作为输入，决定每个 feature 的取值
- **失败回退机制**：当功能解析失败（feature resolution fails）时，对于预先序列化的 descriptor.proto 快照需要提供回退路径
- **legacy syntax 支持**：必须能正确处理 proto2 与 proto3，将其纳入统一的 feature 解析框架
- **默认值兜底**：在 proto2/proto3 场景下解析失败时，应回退到现有的硬编码默认值（hardcoded defaults）
- **桥接作用**：是连接底层 syntax 与上层 FeatureSet 配置的核心方法

## 应用
- 在 protoc 编译器中，为尚未完成迁移的 edition 提供解析路径，避免阻塞 edition zero 的发布
- 对预先序列化的 descriptor.proto 快照执行功能解析，确保反序列化后的特征集合与原始 syntax 一致
- 在 proto2/proto3 仍需支持的过渡期内，作为统一的 feature 求值机制，将 legacy syntax 映射到 Editions 体系
- 配合 FeatureSet 生命周期管理（"Editions: Life of a FeatureSet"），完成功能配置的初始化与回溯

## 相关概念
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Feature Inference|Feature Inference]]
- [[concepts/Bootstrapping|Bootstrapping]]
- [[concepts/Serialized Descriptors|Serialized Descriptors]]
- [[concepts/Legacy Syntax Editions|Legacy Syntax Editions]]

## 相关实体
- [[entities/descriptor.proto|descriptor.proto]]

## 来源提及
- "In order to avoid blocking edition zero for that long, we may need fallbacks in protoc for the case where feature resolution *fails*." — [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]
- "If the file is proto2/proto3, failure should result in a fallback to the existing hardcoded defaults." — [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]
- "Editions: Life of a FeatureSet"（作为 Feature Resolution 所关联的 FeatureSet 生命周期阶段名称） — [[sources/editions-legacy-syntax-editions|editions-legacy-syntax-editions]]