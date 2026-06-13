---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [term]
aliases:
  - "protobuf extension numbers"
  - "Extension numbers"
---


# Extension numbers

## 定义
Extension numbers 是 Protocol Buffers 中用于标识自定义扩展字段的数字标识符，类似于消息字段的 tag number。在 protobuf 中，自定义选项必须通过全局唯一的扩展编号进行注册，以避免不同项目之间的冲突。该注册表集中管理所有已分配的扩展编号（从 1000 开始），通过 GitHub 上的 Pull Request 流程进行协调和分配。

## 关键特征
- 作为 protobuf 扩展机制的核心标识，每个扩展字段必须被分配一个全局唯一的 extension number
- 注册表从 1000 号段开始集中管理已分配的扩展编号
- 通过 GitHub Pull Request 流程进行协调和分配，确保透明和可追溯
- 每个项目可以占用单个扩展号或连续的扩展号段（例如 1026 → 1030、1157–1166）
- 全局唯一性保证：使用多个第三方项目的开发者可以确信不会出现扩展号冲突

## 应用
- **自定义选项注册**：在 protobuf 中定义 `extend` 语句以扩展 `FileOptions`、`MessageOptions`、`FieldOptions` 等选项时，需要申请扩展号
- **descriptor.proto 扩展**：为 `descriptor.proto` 添加自定义元数据信息
- **跨组织协作**：不同团队或开源项目可以安全地定义各自的扩展，而不必担心编号冲突
- **工具链与框架集成**：Buf、Connect、protoc-gen-validate 等工具通过分配专属扩展号段来实现各自的功能增强

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor.proto|descriptor.proto]]

## 相关实体
- [[entities/protocolbuffersprotobuf|protocolbuffers/protobuf]]
- [[entities/buf|buf]]
- [[entities/connect|connect]]

## 来源提及
- "any developer who wishes to use multiple 3rd party projects, each with their own extensions, can be confident that there won't be collisions in extension numbers." — [[sources/options|options]]
- "Extensions: 1000" — [[sources/options|options]]
- "Extensions: 1026 -> 1030" — [[sources/options|options]]
- "Extension: 1157-1166" — [[sources/options|options]]