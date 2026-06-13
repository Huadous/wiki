---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [other]
aliases:
  - "Conformance Request proto"
  - "conformance_testing.ConformanceRequest"
---


# ConformanceRequest

## 基本信息
- Type: other
- Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]

## 描述
ConformanceRequest 是 Protocol Buffers 语言无关（language-agnostic）一致性测试框架（conformance testing framework）中已存在的一条 Protocol Buffers 消息，用于在 runner 二进制与待测语言二进制之间传递序列化负载和测试指令。runner 二进制启动后会与任意语言实现构建的待测二进制挂钩，向其发送一个 `ConformanceRequest` proto（包含序列化负载与指令集合），并接收返回的 `ConformanceResponse` 结果。该消息是描述提案中提出的新 `DescriptorConformanceRequest` 的参考模型（reference model），其既有的 runner-based 架构正是新描述符一致性框架（descriptor conformance framework）所刻意对齐的设计基础。尽管作者最终认为现有消息形态并不完全契合 feature resolution 场景，但已确立的 runner 通信模型被新框架完整继承与镜像。

## 相关实体
- [[entities/ConformanceResponse|ConformanceResponse]]
- [[entities/DescriptorConformanceRequest|DescriptorConformanceRequest]]

## 相关概念
- [[concepts/Conformance-Testing|Conformance Testing]]
- [[concepts/Feature-Resolution|Feature Resolution]]

## 来源提及
- "There's a runner binary that can be hooked up to another binary built in any language. It sends a `ConformanceRequest` proto with a serialized payload and set of instructions, and then receives a `ConformanceResponse` with the result." — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]