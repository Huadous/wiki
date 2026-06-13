---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-edition-zero-features|editions-edition-zero-features]]"]
tags: [term]
aliases:
  - "syntax-less Protobuf"
  - "no-syntax Protobuf"
---


# no-syntax Protobuf

## 定义
no-syntax Protobuf 是 Protobuf Editions 背后的哲学愿景，旨在消除 Protobuf 文件中显式 `syntax` 关键字的概念。它代表着从 proto2 与 proto3 之间的二元选择，转向更细粒度的、基于特性的配置模型——字段存在性、枚举开放性等行为不再由语法级别决定，而是由显式 features 控制。文档将 [[concepts/edition-zero|Edition Zero]] 介绍为这个「no-syntax Protobuf 大胆新世界」的「第一版」，并明确指出尽管移除了 `syntax` 关键字，这本质上是「定义了一种新的 Protobuf `syntax`，即使它不是以那种方式拼写的」。

## 关键特征
- 消除 `.proto` 文件中的显式 `syntax = "proto2"` / `syntax = "proto3"` 声明
- 由全局的 Edition 声明取代原有的语法版本选择
- 字段级行为（如存在性、枚举开放性等）通过显式 features 配置
- 取代 proto2 与 proto3 的二元分裂模型
- 形式上无 `syntax` 关键字，但语义上仍构成一种新的语法规范
- 作为 Editions 体系的长期演进愿景，[[concepts/edition-zero|Edition Zero]] 是其首个落地实例

## 应用
- Protobuf Editions 体系下的 schema 演进与兼容性管理
- 以特性（feature）为粒度进行细粒度行为配置，替代粗粒度的语法版本切换
- 为 [[concepts/protobuf-editions|Protobuf Editions]] 的未来演进提供统一的语言模型，避免每次引入新行为都需要新增语法版本
- 在 [[concepts/converged-semantics|Converged semantics]] 与 [[concepts/presence-discipline|presence discipline]] 等设计理念中体现 no-syntax 哲学

## 相关概念
- [[concepts/edition-zero|Edition Zero]]
- [[concepts/protobuf-editions|Protobuf Editions]]
- [[concepts/converged-semantics|Converged semantics]]
- [[concepts/presence-discipline|presence discipline]]

## 相关实体
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]

## 来源提及
- *Edition Zero Features* defines the "first edition" of the brave new world of no-syntax Protobuf. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]
- This document will require careful review from various stakeholders, because it is essentially defining a new Protobuf `syntax`, even if it isn't spelled that way. — [[sources/editions-edition-zero-features|editions-edition-zero-features]]