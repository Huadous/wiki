---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]"]
tags: [standard]
aliases:
  - "Protocol Buffers 2/3"
  - "proto2 and proto3"
---


# proto2/proto3

## 定义
proto2 与 proto3 是 Protocol Buffers（protobuf）的两个主要历史版本，二者在 packed 编码、extensions、`required` 字段、groups、open enums 等行为上存在隐含差异。这些差异历史上通过 `syntax` 关键字进行粗粒度声明（即整文件 `= "proto2"` 或 `= "proto3"`）。在 Editions 体系设计中，proto2/proto3 被视为即将被「editions + features」细粒度机制取代的粗粒度语义模型；Edition Zero 默认采用二者融合后的 Converged Semantics，并允许用户通过显式 opt-out 特定 feature 来可逆地降级回 proto2 或 proto3 语义。

## 关键特征
- **粗粒度语义模型**：以 `syntax = "proto2" | "proto3"` 作为整文件级别的开关，隐式启用/禁用一组相关行为
- **隐含差异众多**：包括 `packed` 默认值、`extensions` 支持、`required` 字段校验、groups、open enums 等多方面行为差异
- **即将被取代**：在 Editions 设计中被定位为需要迁移的遗留模型，由 editions + 显式 features 取代
- **可逆降级路径**：Edition Zero 在 Converged Semantics 之上提供 opt-out 机制，使用户可按需回退到任一历史行为
- **迁移动机**：proto2/proto3 的隐含差异以表格形式被显式列出，作为推动迁移到显式 features 的依据

## 应用
- **存量 proto 文件的语义识别**：通过 `syntax` 关键字判断一个 `.proto` 文件应遵循 proto2 还是 proto3 的隐式行为集合
- **Editions 迁移的基线参考**：作为「粗粒度旋钮」与新版「细粒度 features」体系做对比，量化设计改进幅度
- **Edition Zero 的默认语义底座**：Edition Zero 默认采用 proto2 与 proto3 融合后的 Converged Semantics
- **可逆兼容性场景**：当新版 features 与既有业务不兼容时，用户可通过 opt-out 特定 feature 回到 proto2 或 proto3 的对应行为

## 相关概念
- [[concepts/converged-semantics|Converged Semantics]]
- [[concepts/edition-keyword|edition keyword]]
- [[concepts/syntax-keyword-deprecation|syntax keyword deprecation]]

## 相关实体
- [[entities/protobuf-team|Protobuf Team]]
- [[entities/edition-zero|Edition Zero]]
- [[entities/descriptor-proto|descriptor.proto]]

## 来源提及
- "more granular specification of intent than the existing coarse knob of 'proto2' or 'proto3.'" — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]
- "if needed can reversibly downgrade back to proto2 or proto3 semantics respectively by opt-ing out of the specific features that are incompatible with their existing needs." — [[sources/editions-edition-zero-converged-semantics|editions-edition-zero-converged-semantics]]