---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]"]
tags: [other]
aliases:
  - "Exposing Editions Feature Sets"
  - "EEFS"
  - "Editions Feature Sets 早期设计文档"
---


# Exposing Editions Feature Sets

## 基本信息
- Type: other
- Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]

## 描述
Exposing Editions Feature Sets 是一份早期的内部设计文档，是将 [[concepts/FeatureSet|FeatureSet]] 可见性在 [[entities/protoc|protoc]]、代码生成器（generators）以及运行时（runtimes）之间进行切分的首次形式化尝试。该文档确立了"用户应仅通过代码生成产物或运行时辅助函数间接接触 feature"的核心理念，以避免在 [[concepts/Hyrum's Law|Hyrum's Law]] 下将每一个设计选择都固化下来。文档假设 [[entities/protoc|protoc]] 前端能够计算并向下传递全部四套 [[concepts/FeatureSet|FeatureSet]]，但后续被证明不可行——因为生成器侧的 feature 无法在不执行 import 的前提下被静态发现。尽管该文档标注为"not available externally"，它仍是 [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]（即"editions-editions-life-of-a-featureset"）一文所讨论的设计演进路径中的奠基性参考。该文档由 [[entities/mkruskal-google|mkruskal-google]] 主导，并在涉及 [[entities/descriptor.proto|descriptor.proto]] 层面的 [[concepts/Option Retention|Option Retention]] 与 [[concepts/Feature Resolution|Feature Resolution]] 机制时被反复引用。

## 相关实体
- [[entities/mkruskal-google|mkruskal-google]]
- [[entities/protoc|protoc]]
- [[entities/descriptor.proto|descriptor.proto]]

## 相关概念
- [[concepts/FeatureSet|FeatureSet]]
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/Hyrum's Law|Hyrum's Law]]
- [[concepts/Generator Features|Generator Features]]
- [[concepts/Option Retention|Option Retention]]

## 来源提及
- *Exposing Editions Feature Sets* (not available externally) was a first attempt to try to define some of these concepts. — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]