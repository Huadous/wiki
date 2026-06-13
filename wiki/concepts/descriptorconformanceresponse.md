---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [standard]
aliases:
  - "Descriptor Conformance Response"
  - "DescriptorConformanceResponse 消息"
---


# DescriptorConformanceResponse

## 定义
DescriptorConformanceResponse 是与 [[concepts/DescriptorConformanceRequest|DescriptorConformanceRequest]] 配对的 proto 消息，用于返回描述符（descriptor）转换与特性解析（Feature Resolution）一致性测试（conformance test）的执行结果。它由被测实现（conformance binary）在完成描述符转换后返回，携带经过转换后的 `FileDescriptorProto`，以及一个 `FileDescriptorSet`，用于描述构建过程中由生成器运行时额外添加的任何特性（features），以便测试运行器能够正确核算这些运行时新增的特性。

## 关键特征
- 与 `DescriptorConformanceRequest` 严格成对出现，结构上镜像已有的解析/序列化一致性测试消息对 `ConformanceRequest`/`ConformanceResponse`。
- 核心字段为 `FileDescriptorProto file`，承载被测实现对原始描述符完成指定转换后的结果。
- 包含 `FileDescriptorSet added_features` 字段，用于上报测试过程中构建期新增的特性集合，从而让 runner 准确识别运行时由生成器加入的特性。
- 设计目标是支持多种描述符转换场景的测试，包括但不限于：
  - `proto3_optional`（proto3 可选字段）
  - `group` / `DELIMITED`（分组与定界编码）
  - `required` / `LEGACY_REQUIRED`（必填字段及其遗留形式）
- 兼具描述符转换结果回传与特性解析验证两重用途，是特性解析一致性测试体系的核心消息之一。

## 应用
- 在 Protobuf 一致性测试框架中，用于校验不同实现对描述符转换规则的处理是否一致。
- 用作特性解析（Feature Resolution）测试的输出容器，让 runner 能够区分原始特性与运行期新增特性。
- 用于对 `proto3_optional`、`group/DELIMITED`、`required/LEGACY_REQUIRED` 等多种描述符转换路径进行回归与互操作测试。
- 与 `DescriptorConformanceRequest` 联合部署，使描述符层面的测试能够沿用与解析/序列化一致性测试相同的请求-响应模式。

## 相关概念
- [[concepts/DescriptorConformanceRequest|DescriptorConformanceRequest]]
- [[concepts/Conformance Testing|Conformance Testing]]
- [[concepts/Feature Resolution|Feature Resolution]]
- [[concepts/FileDescriptorProto|FileDescriptorProto]]

## 相关实体
- 无相关实体。

## 来源提及
- ```
message DescriptorConformanceResponse {
  // The transformed file.
  FileDescriptorProto file = 1;
  // Any additional features added during build.
  FileDescriptorSet added_features = 2;
}
— [[sources/editions-editions-life-of-a-featureset]]