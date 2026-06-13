---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/cpp_build_systems|cpp_build_systems]]"]
tags: [method]
aliases:
  - "Bazel Aspect 机制"
  - "Starlark Aspect"
  - "Bazel Aspects"
---


# Bazel Aspect

## 定义
Bazel Aspect 是 Bazel 构建系统提供的一种 Starlark 机制，允许用户在依赖图中进行"横切"遍历，收集关于构建规则的额外信息或定义额外的构建动作。Aspect 可以匹配 build graph 中满足条件的规则及其依赖，并向目标附加 provider，从而将额外信息沿依赖图向上传递。

## 关键特征
- 基于 Starlark API 实现，允许用户以编程方式扩展 Bazel 构建行为
- 支持在依赖图中横切遍历目标，而非仅沿依赖链向下传播
- 可访问匹配规则及其传递依赖（transitive dependencies）的全部信息
- 通过 provider 机制将收集到的信息或新定义的构建动作暴露给上游规则消费
- 与规则（rule）正交，可在不修改原规则定义的情况下增强构建流程

## 应用
- 在 Protobuf 的 C++ 构建系统支持中，aspect 被用来实现文件列表提取：通过 `cc_file_list_aspect` 和 `proto_file_list_aspect` 收集源文件信息，并经由 provider 暴露给上层规则消费
- `cc_proto_library` 规则使用 aspect 遍历 `proto_library` 规则的依赖图，动态挂载额外动作以调用 Protobuf 编译器生成 C++ 代码，再调用 C++ 编译器完成编译
- 实现"单一权威构建源"（single source of truth），由同一份构建描述派生出多种输出构建系统
- 在大型多语言代码库中，aspect 常被用于代码生成、覆盖率收集、依赖审计等横切关注点

## 相关概念
- [[concepts/cc-file-list-aspect|cc_file_list_aspect]]
- [[concepts/proto-file-list-aspect,proto_file_list_aspect]]
- [[concepts/starlark-api,Starlark API]]
- [[concepts/cc-proto-library,cc_proto_library]]

## 相关实体
- [[entities/bazel,Bazel]]
- [[entities/protobuf,Protobuf]]

## 来源提及
- "Bazel's Starlark API provides aspects to traverse the build graph, inspect build rules, define additional actions, and expose information through providers." — [[sources/cpp_build_systems|cpp_build_systems]]
- "the cc_proto_library rule uses an aspect to traverse the dependency graph of proto_library rules, and dynamically attaches actions to generate C++ code using the Protobuf compiler and compile using the C++ compiler." — [[sources/cpp_build_systems|cpp_build_systems]]