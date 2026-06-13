---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options]]"]
tags: [project]
aliases:
  - "nanopb"
  - "NanoPB"
  - "nanopb C protobuf"
---


# nanopb

## 基本信息
- Type: project
- Source: [[sources/options]]

## 描述
nanopb 是一个轻量级的 Protocol Buffers C 实现，特别适用于嵌入式系统和资源受限环境。它在 Protocol Buffers 全局扩展注册表中分配到的扩展编号为 1010，官方网站为 http://kapsi.fi/~jpa/nanopb。nanopb 以其极小的代码体积和内存占用著称，被广泛用于物联网设备和微控制器中，为 protobuf 在嵌入式领域的应用提供了可行的方案。作为一个纯 C 语言实现，它不依赖于运行时代码生成，而是通过预编译方式生成高效的编解码代码，从而在资源极其有限的环境中仍能保持良好的性能。

## 相关实体
- [[entities/protobuf-c|protobuf-c]]
- [[entities/embedded-proto|Embedded Proto]]
- [[entities/protons|Protons]]

## 相关概念
- [[concepts/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[concepts/custom-options|Custom options]]
- [[concepts/extension-numbers|Extension numbers]]

## 来源提及
- "Nanopb — [[sources/options|options]]"
- "Website: http://kapsi.fi/~jpa/nanopb — [[sources/options|options]]"
- "Extensions: 1010 — [[sources/options|options]]"