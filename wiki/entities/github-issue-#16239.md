---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues]]"]
tags: [other]
aliases:
  - "protobuf issue 16239"
  - "protocolbuffers/protobuf#16239"
---


# GitHub issue #16239

## 基本信息
- Type: other
- Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]

## 描述
GitHub issue #16239 是由 [[entities/joshua-humphries|Joshua Humphries]] 在 protocolbuffers/protobuf 仓库提交的一个问题报告，提交于 Protocol Buffers Edition 2023 早期发布版本的实验阶段。该 issue 指出，Edition 2023 中新增的 delimited message 编码功能在实现上过度依赖原有的 proto2 group 逻辑（[[concepts/group-fields|Group fields]]），导致该功能在通用场景下几乎无法使用。Humphries 的报告时机恰好，配合 [[sources/editions-group-migration-issues|editions-group-migration-issues]] 源文件所记录的后续分析与修复工作。由于此前的测试和迁移工作都聚焦于保留旧有 proto2 行为，该缺陷未能被早期发现。该 issue 触发了对 [[concepts/delimited-encoding|delimited encoding]] 与 [[concepts/edition-2023|Edition 2023]] 编码路径的重新审视，并推动了 [[concepts/smooth-extension|Smooth Extension]] 方案的形成与落地。

## 相关实体
- [[entities/joshua-humphries|Joshua Humphries]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 相关概念
- [[concepts/edition-2023|Edition 2023]]
- [[concepts/delimited-encoding|delimited encoding]]
- [[concepts/group-fields|Group fields]]
- [[concepts/smooth-extension|Smooth Extension]]

## 来源提及
- Joshua Humphries reported some well-timed issues discovered while experimenting with our early release of Edition 2023. — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- He discovered that our new message encoding feature piggybacked a bit too much on the old group logic, and actually ended up being virtually useless in general. — [[sources/editions-group-migration-issues|editions-group-migration-issues]]