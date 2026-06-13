---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [product]
aliases:
  - "GNU C Library"
  - "GNU glibc"
---


# glibc

## 基本信息
- **类型**: product
- **相关来源**: [[sources/en_getting_started|en_getting_started]]

## 描述
glibc（GNU C Library）是GNU项目发布的C标准库实现，是Linux系统上最核心的运行时组件之一。brpc项目明确支持glibc 2.12至2.25版本范围，并声明在此区间内无已知兼容性问题。glibc为brpc提供了底层系统调用封装与完整的标准C函数接口，是brpc编译与运行的基础依赖之一。它与[[entities/gcc|GCC]]编译器紧密配合，共同构成了brpc跨平台运行的关键底层支撑。

## 相关实体
- [[entities/gcc|GCC]] — 与glibc共同构成brpc编译运行的基础工具链
- [[entities/brpc|brpc]] — 依赖glibc提供底层系统调用与C运行时支持
- [[entities/cmake|CMake]] — brpc构建系统中涉及glibc版本检测的构建工具

## 相关概念
无

## 来源提及
- "glibc: 2.12-2.25 no known issues." — [[sources/en_getting_started|en_getting_started]]