---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/techniques]]"]
tags: [term]
aliases:
  - "textproto"
  - "文本格式"
  - "Protocol Buffers Text Format"
---


# Text Format

## 定义
Protocol Buffers 的文本表示格式，提供人类可读的消息描述，主要用于调试和配置场景。文件后缀推荐使用 `.txtpb`，旧称 `.textproto`。

## 关键特征
- 人类可读：以文本形式呈现 Protocol Buffers 消息的字段值，便于理解和编辑
- 简洁性：推荐使用短后缀 `.txtpb` 以提高简洁性
- 与二进制格式（Wire Format）互补：文本格式适合人工操作，但编码效率较低

## 应用
- 调试：在开发过程中直接查看和验证消息内容
- 配置：用于定义配置文件，替代 JSON 或 YAML 等通用格式
- 教学：作为示例展示 Protocol Buffers 消息的层次结构

## 相关概念
- [[concepts/wire-format|Wire Format]]
- [[concepts/json-format|JSON Format]]（若页面不存在，Lint 系统将自动处理）

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "For Text Format specifically, `.textproto` is also fairly common, but we recommend `.txtpb` for its brevity." — [[sources/techniques|techniques]]
- "Text Format, Extension: `.txtpb`" — [[sources/techniques|techniques]]