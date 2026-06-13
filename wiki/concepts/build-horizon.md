---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-evolution|editions-edition-evolution]]"]
tags: [term]
aliases:
  - "build horizon"
  - "构建视野"
---


# Build Horizon

## 定义
Build Horizon 是 Protobuf Editions 演进文档中为解决"来自未来的 edition"问题而提出的设计机制。当编译时使用较旧 edition 的服务收到以更新 edition 编码的消息时，会发生解析失败，从而导致不可接受的服务降级（unacceptable service degradation）。为应对该问题，文档提出两种可选路径：其一是完全禁止引入需要读取方（reader）支持新编码格式的特性（被认为不切实际）；其二是定义某种 build horizon，对可在当前版本中引入的特性范围加以约束。

## 关键特征
- 目的：防止旧版服务（使用较旧 edition 编译）因收到新版编码消息而出现解析失败，避免服务降级
- 应对的核心问题是"来自未来的 edition"（editions from the future）
- 属于 Editions 演进中处理向后兼容性的关键设计概念
- 提供两种解决方向：禁止引入需要新编码支持的特性，或通过 build horizon 限制特性引入范围
- 引入新特性时必须能够纳入某种形式的 build horizon 之内

## 应用
- Protobuf Editions 演进过程中新特性的引入与边界划定
- 服务端/客户端之间因 edition 差异造成的兼容性问题处理
- 在跨版本部署场景中，约束单个构建版本所允许使用的特性集合
- 作为[[concepts/Editions 演进设计|editions-edition-evolution]]中关于兼容性策略的核心术语之一

## 相关概念
- [[concepts/Protobuf Editions|Protobuf Editions]]
- [[concepts/Protobuf Features|Protobuf Features]]
- [[concepts/Backend Features|Backend Features]]
- [[concepts/Editions 演进设计|Editions 演进设计]]

## 相关实体
- [[entities/protoc|protoc]]

## 来源提及
- "Editions may introduce such features, but they must somehow fit into some kind of build horizon." — [[sources/editions-edition-evolution|editions-edition-evolution]]
- "The alternative is to define some kind of build horizon." — [[sources/editions-edition-evolution|editions-edition-evolution]]
- "Because a parse failure would be an unacceptable service degradation, we have a couple of options:" — [[sources/editions-edition-evolution|editions-edition-evolution]]