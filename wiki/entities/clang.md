---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "LLVM Clang"
  - "clang"
---


# Clang

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]] (brpc 构建指南)

## 描述
Clang是LLVM编译器前端支持的C/C++编译器，广泛应用于开源项目中。brpc支持Clang 3.5至4.0版本，且没有已知的兼容性问题，开发者可以放心使用。在brpc的构建过程中，可以通过`--cxx=clang++ --cc=clang`选项显式指定使用Clang编译器。在MacOS环境下，由于系统默认依赖Clang/LLVM工具链，brpc推荐使用Clang进行编译。与[[entities/gcc|GCC]]类似，Clang也是brpc官方支持的两大编译器族之一，开发者可根据项目需求自由选择。

## 相关实体
- [[entities/brpc|brpc]] — Clang是brpc支持的编译器之一
- [[entities/gcc|GCC]] — 与Clang并列的brpc编译器选项
- [[entities/protobuf|protobuf]] — 在brpc构建中与Clang协同工作

## 相关概念
- [[concepts/静态链接|静态链接]] — 在brpc中使用Clang编译时涉及的链接方式

## 来源提及
- "Clang: 3.5-4.0 no known issues." — [[sources/en_getting_started|en_getting_started]]
- "To change compiler to clang, add --cxx=clang++ --cc=clang." — [[sources/en_getting_started|en_getting_started]]