---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]"]
tags: [phenomenon]
aliases:
  - "共享实现"
  - "Shared Implementations"
---


# Shared Implementations

## 定义
Shared Implementations（共享实现）指的是像 **upb** 和 **C++** 这类被多种语言（如 Python、Rust、Ruby、PHP 等）作为后端实现共同使用的运行时。当某项功能在这些共享运行时中被定义时，由于缺乏按语言的独立开关，迁移到这些共享实现会更困难——切换运行时实现可能导致微妙且危险的行为变化。

## 关键特征
- **跨语言复用**：单一运行时实现被多种编程语言作为底层后端共享使用。
- **缺乏按语言独立开关**：为这些共享实现定义的功能难以针对每种语言单独控制启用或关闭。
- **迁移成本高**：将功能迁移到共享实现中，会因耦合多个语言生态而带来额外风险。
- **行为一致性风险**：切换运行时实现时可能引入微妙且危险的行为变化，影响多个语言客户端。

## 应用
- 在 Protocol Buffers Editions 设计中评估新功能的放置位置时，需要权衡是否引入共享运行时依赖。
- 指导功能集（FeatureSet）的拆分策略，避免将语言独有特性与共享运行时绑定。
- 帮助开发者理解在切换底层后端（如从独立实现迁移到 upb 或 C++）时需要进行的兼容性测试与回归验证。

## 相关概念
- [[concepts/Polyglot|Polyglot]]
- [[concepts/Runtime Implementation Features|Runtime Implementation Features]]
- [[concepts/Generator Features|Generator Features]]

## 相关实体
*无相关实体。*

## 来源提及
- **Shared Implementations** - Runtimes like upb and C++ are used as backing implementations of multiple other languages (e.g. Python, Rust, Ruby, PHP). — [[sources/editions-editions-feature-extension-layout|editions-editions-feature-extension-layout]]