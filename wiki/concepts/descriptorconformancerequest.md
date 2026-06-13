---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [standard]
aliases:
  - "Descriptor Conformance Request"
  - "DescriptorConformanceRequest proto"
---


# DescriptorConformanceRequest

## 定义
DescriptorConformanceRequest 是 Protocol Buffers Editions 提案 "Editions: Life of a FeatureSet" 中提出的一个 proto 消息（message），用于驱动一种新型的描述符（descriptor）变换与特性（feature）解析的一致性测试框架（conformance test framework）。它携带一个**变换前**的 `FileDescriptorProto`（即待测试的文件），以及构建所需的依赖与特性文件的 `FileDescriptorSet`。该框架借助该消息向各语言二进制发送与语言无关的测试载荷，使任何符合规范的二进制都能使用其自身的特性解析实现重新构建描述符，并通过配对的 [[concepts/DescriptorConformanceResponse|DescriptorConformanceResponse]] 验证其结果是否与 C++ 参考实现（source-of-truth）一致。

## 关键特征
- **proto 消息定义**：标准 protobuf message，可被序列化为语言无关的测试载荷。
- **双字段结构**：
  - `file`：类型为 `FileDescriptorProto`，表示**变换前**的待测文件。
  - `dependencies`：类型为 `FileDescriptorSet`，提供构建所需的依赖与特性文件池。
- **语言无关的测试载体**：通过统一的序列化格式，使任何语言的 conformant 二进制都能消费相同输入。
- **配对使用**：与 `DescriptorConformanceResponse` 共同构成请求/响应测试 API。
- **面向特性解析**：核心目标是验证各语言对 [[concepts/Feature-Resolution|Feature Resolution]] 行为的一致性，而非简单的编码/解码正确性。
- **以 C++ 为参考实现**：响应比对基线由 C++ 实现提供。

## 应用
- **跨语言一致性验证**：在 Editions 特性引入后，确保所有官方/第三方实现（Java、Python、Go、C++、Ruby 等）在特性解析与描述符变换上行为一致。
- **Editions 迁移回归测试**：在 [[sources/editions-life-of-an-edition|Editions 迁移生命周期]]中，自动化验证每次特性变更不会破坏跨语言互操作。
- **特性组合验证**：通过构造包含特定 [[sources/features|Feature Settings]] 组合的 `dependencies`，测试复杂特性集下的描述符构建结果。
- **CI/CD 集成**：作为 conformant 二进制的标准接口，便于在持续集成流水线中统一运行语言无关的测试用例。
- **新语言实现准入测试**：第三方实现可通过该接口证明其对 Editions 规范的遵循程度。

## 相关概念
- [[concepts/DescriptorConformanceResponse|DescriptorConformanceResponse]]
- [[concepts/Conformance-Testing|Conformance Testing]]
- [[concepts/Feature-Resolution|Feature Resolution]]
- [[concepts/FileDescriptorProto|FileDescriptorProto]]
- [[concepts/FileDescriptorSet|FileDescriptorSet]]

## 相关实体
无相关实体。

## 来源提及
- The following request/response protos describe the API:

message DescriptorConformanceRequest {
  // The file under test, pre-transformation.
  FileDescriptorProto file = 1;
  // The pool of dependencies and feature files required for build.
  FileDescriptorSet dependencies = 2;
}``` — [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]