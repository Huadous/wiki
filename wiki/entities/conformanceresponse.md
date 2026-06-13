---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[protobuf/editions-editions-life-of-a-featureset.md]]"]
tags: [other]
aliases:
  - "Conformance Response proto"
  - "conformance_testing.ConformanceResponse"
---


# ConformanceResponse

## 基本信息
- Type: other
- Source: [[protobuf/editions-editions-life-of-a-featureset.md]]

## 描述
ConformanceResponse 是 Protocol Buffers 一致性测试（conformance testing）框架中由被测语言二进制（language-under-tested binary）返回给驱动（runner）的现有 Protocol Buffers 消息，承载针对给定 [[entities/ConformanceRequest|ConformanceRequest]] 所产出的结果。该文档以此既有的请求/响应消息对作为架构先例，用以设计新增的特征解析（feature-resolution）一致性测试框架，并指出驱动会"receive a `ConformanceResponse` with the result"，随后在固定测试套件上循环以验证一致性。新的 [[entities/DescriptorConformanceResponse|DescriptorConformanceResponse]] 明确以此消息为建模蓝本，并通过新增一个用于收集描述符池构建过程中所填充的生成器特征的 `added_features` FileDescriptorSet 字段对其进行扩展。

## 相关实体
- [[entities/ConformanceRequest|ConformanceRequest]]
- [[entities/DescriptorConformanceResponse|DescriptorConformanceResponse]]

## 相关概念
- [[concepts/Conformance Testing|Conformance Testing]]
- [[concepts/Feature Resolution|Feature Resolution]]

## 来源提及
- "There's a runner binary that can be hooked up to another binary built in any language. It sends a `ConformanceRequest` proto with a serialized payload and set of instructions, and then receives a `ConformanceResponse` with the result." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]