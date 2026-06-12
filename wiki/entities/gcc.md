---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "GNU Compiler Collection"
  - "GNU编译器套件"
---


# GCC

## 基本信息
- **Type:** product
- **Source:** [[sources/en_getting_started|en_getting_started]]

## 描述

GCC（GNU Compiler Collection）是GNU项目开发的编译器套件，支持多种编程语言，是[[entities/brpc|brpc]]构建所依赖的核心编译器。brpc支持GCC 4.8到11.2版本，并推荐使用8.2以上版本以获取更好的兼容性和性能。在构建brpc时，GCC的版本选择直接影响编译过程，例如在GCC 4+中需要通过添加特定编译选项来解决errno问题。brpc默认启用C++11标准，从而减少了Boost依赖，并针对GCC 7中的过度对齐问题做了临时性规避。GCC与[[entities/Clang|Clang]]等其他编译器共存于brpc构建系统中，用户可通过编译选项在它们之间切换。

## 相关实体

- [[entities/brpc|brpc]]
- [[entities/Clang|Clang]]
- [[entities/protobuf|protobuf]]
- [[entities/cmake|cmake]]

## 相关概念

- [[concepts/静态链接|静态链接]]

## 来源提及

- "Prefer GCC 8.2+" — [[sources/en_getting_started|en_getting_started]]
- "GCC: 4.8-11.2" — [[sources/en_getting_started|en_getting_started]]
- "Adding -D__const__=__unused__ to cxxflags in your makefiles is a must to avoid errno issue in gcc4+." — [[sources/en_getting_started|en_getting_started]]
- "The over-aligned issues in GCC7 is suppressed temporarily now." — [[sources/en_getting_started|en_getting_started]]