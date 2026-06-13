---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-group-migration-issues|editions-group-migration-issues]]"]
tags: [method]
aliases:
  - "Nerf Delimited Encoding"
  - "2023 版削弱 Delimited Encoding 方案"
---


# Nerf Delimited Encoding in 2023

## 定义
Nerf Delimited Encoding in 2023 是 protobuf edition 2023 提案中的备选方案之一，用于在 edition 2024 之前无法落地更优方案时作为快速修复（fallback）。其核心思路是通过限制消息名与字段名的匹配规则来削弱 delimited encoding 的能力，使其在功能上退化为"类似 group 但更差"的形态，从而在 protoc 中以验证逻辑的方式强制收敛行为，解除 edition 2023 发布的阻塞。

## 关键特征
- 作为 edition 2023 发布的快速修复（fallback）方案存在
- 禁止消息名（message name）与字段名（field name）不匹配的情况，从而限制 delimited encoding 的使用方式
- 可在 protoc 中加入相应的验证逻辑来强制执行
- 实现简单，安全性较高，能够顺利推动 edition 2023 发布
- 功能上让 delimited encoding 退化为"like groups but worse"（类似 group 但更差）
- 限制行为需要等到 edition 2024 才能得到修复，限制了 delimited encoding 的扩展空间
- 会阻碍 delimited encoding 生态系统的迁移进程，直到 edition 2024 开始推广

## 应用
- 作为 edition 2023 发布前的快速修复方案，在更优迁移路径成熟前临时使用
- 在 protoc 编译器中以静态校验的方式限制消息名与字段名的命名一致性
- 在需要阻断 group 行为残留、又不想引入破坏性变更的过渡窗口中使用
- 作为讨论 [[concepts/Edition 2023|Edition 2023]] 配套演进路线时的对照方案

## 相关概念
- [[concepts/Delimited encoding|Delimited encoding]]
- [[concepts/Edition 2023|Edition 2023]]
- [[concepts/Group-like fields|Group-like fields]]
- [[concepts/Smooth Extension|Smooth Extension]]
- [[concepts/Global Feature|Global Feature]]

## 相关实体
- 无相关实体

## 来源提及
- "Nerf Delimited Encoding in 2023 (not available externally) is the quickest path forward to unblock the release of edition 2023." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]
- "It has a lot of downsides though, and will block any migration towards delimited encoding until edition 2024 has started rolling out." — [[sources/editions-group-migration-issues|editions-group-migration-issues]]