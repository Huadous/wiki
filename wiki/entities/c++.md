---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/editions-what-are-protobuf-editions]]"]
tags: [product]
aliases:
  - "C++编程语言"
  - "C++ language"
---


# C++

## 基本信息
- Type: product
- Source: [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]

## 描述
C++是一种广泛使用的系统编程语言，是[[entities/protocol-buffers|Protocol Buffers]]的主要代码生成目标之一。在Protocol Buffers Editions的演进中，C++的语言特性改进是重要议题，包括字符串访问器从`const std::string&`向`absl::string_view`的迁移、枚举命名风格的统一等。这些改进通过[[concepts/feature|Feature]]机制进行控制，允许用户逐步采用新特性而无需破坏现有代码。C++在Protocol Buffers生态中扮演代码生成与运行时支持的核心角色，其编译器`protoc`直接生成C++源代码。

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]] — C++是其主要代码生成目标之一
- [[entities/protoc|protoc]] — Protocol Buffers的编译器，生成C++代码

## 相关概念
- [[concepts/feature|Feature]] — 控制C++语言特性切换的机制

## 来源提及
- "string accessors in C++ still return const std::string&" — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Make every string and bytes accessor in C++ return absl::string_view, unlocking performance optimizations." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]
- "Make enum enumerators in C++ use kName instead of NAME." — [[sources/editions-what-are-protobuf-editions|editions-what-are-protobuf-editions]]