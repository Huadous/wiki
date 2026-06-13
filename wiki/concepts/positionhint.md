---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/flatmap]]"]
tags: [method]
aliases:
  - "PositionHint 迭代器保存机制"
  - "FlatMap PositionHint"
  - "迭代器位置保存"
---


# PositionHint

## 定义
PositionHint 是 [[entities/flatmap|butil::FlatMap]] 提供的一种迭代器位置保存与恢复机制。它专门用于解决「在迭代过程中安全删除元素」这一棘手场景：用户可以先通过 `save_iterator` 将当前迭代器位置保存到 PositionHint 结构中，在调用 `erase()` 之后再通过 `restore_iterator` 从 hint 恢复出一个仍然有效的迭代器，从而避免 `erase()` 后 `++iterator` 可能失效的常见陷阱。

## 关键特征
- **两步式操作**：使用流程固定为 `save_iterator` → `erase` → `restore_iterator` 三步，必须严格按顺序执行。
- **状态保存载体**：PositionHint 是一个轻量级结构（示例中通过 `typename Map::PositionHint hint{};` 声明），用于在 erase 前后承载迭代器的位置信息。
- **解决失效问题**：直接针对 `erase()` 之后 `++iterator` 可能失败的工程陷阱，使按条件删除元素成为可能。
- **FlatMap 专属 API**：该机制是 [[entities/flatmap|FlatMap]] 相对普通开链哈希表在工程易用性上的亮点设计，并非通用 STL 接口。

## 应用
- **遍历中按条件删除**：例如遍历 FlatMap 并删除所有 key 为偶数的元素，是 PositionHint 最典型的使用场景。
- **安全的边遍历边清理**：任何需要在迭代容器的同时根据条件移除部分元素的场景，都能借助该机制避免迭代器失效。
- **替代易错的「先 ++ 再判断」模式**：在开链哈希表中常见的「`++it; if (pred) erase(prev);`」样板代码可由 PositionHint 简化。

## 相关概念
- [[concepts/开链哈希]]
- [[concepts/哈希表]]

## 相关实体
- [[entities/flatmap]]

## 来源提及
- "After `erase()', ++iterator may fail." — [[sources/flatmap|flatmap]]
- "We need to save iterator before `erase()' and restore iterator after `erase()'." — [[sources/flatmap|flatmap]]
- "typename Map::PositionHint hint{};" — [[sources/flatmap|flatmap]]
- "map.save_iterator(it, &hint);" — [[sources/flatmap|flatmap]]
- "it = map.restore_iterator(hint);" — [[sources/flatmap|flatmap]]