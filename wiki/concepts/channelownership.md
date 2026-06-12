---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term]
aliases:
  - "所有权枚举"
  - "Channel Ownership"
---


# ChannelOwnership

## 定义

ChannelOwnership 是 brpc 框架中用于组合 Channel（特别是 `ParallelChannel`）的一个枚举类型，用于指定在添加 sub channel 时，组合 Channel 是否取得该 sub channel 的所有权。该枚举有两个取值：`brpc::OWNS_CHANNEL` 和 `brpc::DOESNT_OWN_CHANNEL`。它提供了一种灵活、精细的内存管理机制，允许用户控制 sub channel 的生命周期。

## 关键特征

- **两种所有权模式**：提供 `OWNS_CHANNEL`（拥有所有权）和 `DOESNT_OWN_CHANNEL`（不拥有所有权）两种模式。
- **自动内存管理**：当设置为 `OWNS_CHANNEL` 时，组合 Channel（如 `ParallelChannel`）在析构时会自动删除其拥有的 sub channel。
- **安全性保障**：即使同一个 sub channel 多次加入同一个 `ParallelChannel`，且多次指定了 `OWNS_CHANNEL`，该 sub channel 在析构时也至多被删除一次，避免了重复释放导致的内存错误。
- **生命周期解耦**：允许用户根据具体场景灵活决定 sub channel 的生命周期是由组合 Channel 管理还是由用户自己管理。

## 应用

- **简化内存管理**：当 `ParallelChannel` 的 sub channel 无需在组合 Channel 之外独立存在时，使用 `OWNS_CHANNEL` 可自动管理其生命周期，避免内存泄漏或手动管理的繁琐。
- **共享 Sub Channel 的场景**：当同一个 `sub channel` 被多个组合 Channel 共享，或需要用户手动管理其生命周期时，使用 `DOESNT_OWN_CHANNEL` 可使所有权与生命周期分离，保证共享 channel 的安全性。
- **与特定 Channel 类型配合**：例如，`SelectiveChannel` 始终拥有其 sub channel 的所有权，这与 `ParallelChannel` 可选择所有权不同。在理解 `SelectiveChannel` 的语义时，需注意这一差异。

## 相关概念

- [[concepts/CallMapper|CallMapper]]
- [[concepts/ResponseMerger|ResponseMerger]]

## 相关实体

- [[entities/ParallelChannel|ParallelChannel]]
- [[entities/SelectiveChannel|SelectiveChannel]]

## 来源提及

- "当ownership为brpc::OWNS_CHANNEL时，sub_channel会在ParallelChannel析构时被删除。" — [[sources/combo_channel|combo_channel]]
- "一个sub channel可能会多次加入一个ParallelChannel，如果其中一个指明了ownership为brpc::OWNS_CHANNEL，那个sub channel会在ParallelChannel析构时被最多删除一次。" — [[sources/combo_channel|combo_channel]]
- "SelectiveChannel总是own sub channel，这和ParallelChannel可选择ownership是不同的。" — [[sources/combo_channel|combo_channel]]