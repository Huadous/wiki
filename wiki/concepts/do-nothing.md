---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [term]
aliases:
  - "Do Nothing Alternative"
  - "放弃 Editions 方案"
---


# Do Nothing

## 定义
Do Nothing 是 Protocol Buffers Editions 设计文档中明确列出并讨论的"考虑替代方案"（Alternative）之一，其核心内容是放弃整个 Editions 设计工作。该方案实质上是承认现有设计在第三方生成器场景下无法工作，因此选择直接放弃整个项目，而非寻求技术上的折中或修复。

## 关键特征
- **彻底放弃 Editions 项目**：Do Nothing 实质上意味着不再推进 Editions 设计工作，回归到 proto3 现状或放弃该方向。
- **第三方生成器被迫自行实现特性解析**：采用此方案后，第三方生成器（third party generators）将不得不自行复制特性解析逻辑（feature resolution logic），且没有任何来自 Protocol Buffers 团队的指导或支持。
- **几乎所有语言出现难以解决的膨胀问题**：除 C++ 外，几乎所有语言的代码体积（code size）和内存（memory）都会出现难以解决的膨胀问题。
- **唯一优点是"工作量更少"（Less work）**：在所有被列出的替代方案中，Do Nothing 是唯一以减少工作量为主要（也是唯一）卖点的方案。
- **缺点被直接评价为"其他所有方面都会更差"（Worse in every other way）**：文档以最简洁且最负面的措辞直接否定了该方案，使其在结构上充当推荐方案的反面。
- **作为反例存在**：Do Nothing 在文档结构上充当推荐方案的反例——推荐方案要求每个阶段（protoc、生成器、运行时）都独立执行特性解析并共享未解析特性，而 Do Nothing 则是对该设计目标的彻底放弃。

## 应用
Do Nothing 并非一个被推荐采用的方案，而是作为反例出现在设计决策讨论中，用于衬托其他替代方案（如 [[concepts/Bidirectional Plugins|Bidirectional Plugins]]、[[concepts/Central Feature Registry|Central Feature Registry]]、[[concepts/Default Placeholders|Default Placeholders]]、[[concepts/Use Generated Pool for C++ Generators|Use Generated Pool for C++ Generators]]）的相对优势。其"应用"场景仅限于设计文档中的对比论证。

## 相关概念
- [[concepts/Editions|Editions]]
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/C++ Generators|C++ Generators]]
- [[concepts/Non-C++ Generators|Non-C++ Generators]]
- [[concepts/Bidirectional Plugins|Bidirectional Plugins]]
- [[concepts/Central Feature Registry|Central Feature Registry]]
- [[concepts/Default Placeholders|Default Placeholders]]
- [[concepts/Use Generated Pool for C++ Generators|Use Generated Pool for C++ Generators]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Doing nothing would basically mean abandoning editions. The current design doesn't (and can't) work for third party generators." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]