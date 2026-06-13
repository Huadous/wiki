---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [method]
aliases:
  - "Large-Scale Change"
  - "大规模变更"
---


# LSC

## 定义
LSC（Large-Scale Change，大规模变更）是Google内部用于大规模代码迁移的方法论。它通过自动化批量修改代码的方式，在大型代码库中推广新行为、淘汰旧特性或进行架构升级，从而显著减少人工干预和降低迁移成本。

## 关键特征
- **大规模自动化**：LSC的核心是自动化执行，能够对代码库中成千上万个文件进行批量修改，远超人工处理的规模和速度。
- **模板化流程**：LSC操作遵循统一的模板，确保所有变更具有一致性和可重复性，便于审计和回滚。
- **行为推广**：主要用于推广新的默认行为或淘汰被标记为废弃的特性，例如将显式设置的feature自动转换为默认值。
- **低风险迁移**：通过精心设计的转换规则和验证机制，LSC能够将大规模迁移的风险降至最低，尤其在像Protobuf Editions这样的无操作（no-op）迁移场景中效率极高。

## 应用
- **代码库现代化**：在Google庞大的代码库中，LSC被用于将旧的API调用模式统一升级为新版本。
- **功能淘汰**：如文档所述，“Undesirable features will be LSC'd away”，将不期望的feature通过LSC自动去除，无需开发人员手动逐个修改。
- **协议升级**：在Protobuf Editions中，LSC是版本迁移的关键工具，用于将feature设置从显式改为默认值，反之亦然，实现不同Edition之间的无缝过渡。
- **政策推行**：为跨团队、跨项目的技术政策（如编码规范、安全策略）提供自动化的落地手段。

## 相关概念
- [[concepts/Feature|Feature]]
- [[concepts/Edition|Edition]]

## 相关实体
- [[entities/Google|Google]]
- [[entities/Protobuf Editions|Protobuf Editions]]

## 来源提及
- "Undesirable features will be LSC'd away, using the same template as any other feature/edition migration." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "The migration to edition “2025” across google will move very fast as it is a no-op." — [[protobuf/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]