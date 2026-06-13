---
type: source
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[protobuf/editions-edition-naming.md]]"
tags:
  - "FeatureSet"
  - "Feature Resolution"
  - "Editions"
  - "Option Retention"
  - "Hyrum's Law"
  - "Descriptor Pool"
  - "Conformance Testing"
  - "CodeGenerator"
  - "Edition Defaults"
  - "Global Features"
  - "Generator Features"
  - "Source Features"
  - "Runtime Features"
  - "Resolved Features"
  - "Unresolved Features"
  - "Dynamic Messages"
  - "DescriptorConformanceRequest"
  - "DescriptorConformanceResponse"
  - "Bidirectional Plugins"
  - "Central Feature Registry"
  - "Default Placeholders"
  - "Staged Rollout for Dynamic Messages"
  - "Bootstrapping"
  - "GeneratorRequest"
  - "Runtimes Without Reflection"
  - "Use Generated Pool for C++ Generators"
  - "C++ Generators"
  - "Non-C++ Generators"
  - "raw_features"
  - "MergeFeatures"
  - "GetFeatures"
  - "FileDescriptor::CopyTo"
  - "Do Nothing"
aliases:
  - "Editions: Life of a FeatureSet"
  - "FeatureSet 生命周期设计"
---

## 来源
- Original file: [[protobuf/editions-editions-life-of-a-featureset.md]]
- Ingested: 2026-06-13

## 核心内容

本文档由 [[entities/mkruskal-google|mkruskal-google]] 撰写并于 2023-08-17 批准，深入讨论了 Protocol Buffers [[concepts/editions|Editions]] 系统中 [[concepts/featureset|FeatureSet]] 在 [[entities/protoc|protoc]]、生成器与运行时之间的生命周期管理问题。本文承接 [[entities/protobuf-editions-design-features|Protobuf Editions Design: Features]]、[[entities/exposing-editions-feature-sets|Exposing Editions Feature Sets]] 与 [[entities/editions-runtime-feature-set-defaults|Editions: Runtime Feature Set Defaults]] 等先期设计，指出其根本缺陷：protoc 无法作为特性解析的通用真相来源，因为它只能通过 import 发现那些被显式导入的生成器特性。

文档推荐采用"每阶段独立解析"方案——在 protoc、各 [[concepts/codegenerator|CodeGenerator]] 及各运行时中分别实现 [[concepts/feature-resolution|Feature Resolution]]，仅在彼此之间传递 [[concepts/unresolved-features|Unresolved Features]]。该方案虽需跨语言复制解析逻辑，但能最小化代码大小与内存开销，并统一处理 [[concepts/descriptor-pool|Descriptor Pool]] 与 [[concepts/dynamic-messages|Dynamic Messages]] 场景。文档针对 [[concepts/c++-generators|C++ Generators]]、[[concepts/non-c++-generators|Non-C++ Generators]]、[[concepts/runtimes-without-reflection|Runtimes Without Reflection]]、[[entities/descriptor-proto|descriptor.proto]] 引导及动态消息等不同情况分别给出策略，并通过扩展 [[concepts/conformance-testing|Conformance Testing]] 框架（引入 [[concepts/descriptorconformancerequest|DescriptorConformanceRequest]]/[[concepts/descriptorconformanceresponse|DescriptorConformanceResponse]]）保证跨语言一致性。

## 补充来源
- Additional source: [[protobuf/editions-edition-naming.md]]
- 注：该来源未提供与本页主题直接相关的信息

## 关键实体
- [[entities/mkruskal-google|mkruskal-google]] - 文档作者
- [[entities/protoc|protoc]] - Protocol Buffers 编译器入口
- [[entities/descriptor-proto|descriptor.proto]] - 因无法导入任何特性文件而需特殊处理
- [[entities/protobuf-editions-design-features|Protobuf Editions Design: Features]] - 定义特性解析算法的基础文档
- [[entities/exposing-editions-feature-sets|Exposing Editions Feature Sets]] - 早期 FeatureSet 可见性设计
- [[entities/editions-runtime-feature-set-defaults|Editions: Runtime Feature Set Defaults]] - 运行时默认特性设计
- [[entities/filedescriptorproto|FileDescriptorProto]] - 描述符核心消息
- [[entities/filedescriptorset|FileDescriptorSet]] - 流水线间传递的容器
- [[entities/conformancerequest|ConformanceRequest]] - 现有 conformance 框架请求消息
- [[entities/conformanceresponse|ConformanceResponse]] - 现有 conformance 框架响应消息

## 关键概念
- [[concepts/featureset|FeatureSet]] - 承载特性的核心数据结构
- [[concepts/feature-resolution|Feature Resolution]] - 将 defaults、继承与 override 合并到 FeatureSet 的算法
- [[concepts/editions|Editions]] - 替代 proto2/proto3 的新机制
- [[concepts/option-retention|Option Retention]] - 规定 option 可见阶段的保留策略
- [[concepts/hyrums-law|Hyrum's Law]] - 解释为何不公开已解析特性
- [[concepts/descriptor-pool|Descriptor Pool]] - 运行时构建描述符的关键数据结构
- [[concepts/conformance-testing|Conformance Testing]] - 跨语言一致性测试方法
- [[concepts/codegenerator|CodeGenerator]] - protoc 用于生成目标语言代码的基类
- [[concepts/edition-defaults|Edition Defaults]] - 每 edition 自带的默认 FeatureSet 值
- [[concepts/global-features|Global Features]] - 应用于 protobuf 语言本身的特性
- [[concepts/generator-features|Generator Features]] - 由特定运行时/生成器拥有的特性
- [[concepts/source-features|Source Features]] - 选项保留前 protoc 与生成器可见的特性
- [[concepts/runtime-features|Runtime Features]] - 选项保留后运行时可见的特性
- [[concepts/resolved-features|Resolved Features]] - 已应用 defaults 和继承的特性
- [[concepts/unresolved-features|Unresolved Features]] - 用户显式设置、未经解析的最小表示
- [[concepts/dynamic-messages|Dynamic Messages]] - 在运行时构建并操作消息的功能
- [[concepts/descriptorconformancerequest|DescriptorConformanceRequest]] - 新增的描述符一致性请求
- [[concepts/descriptorconformanceresponse|DescriptorConformanceResponse]] - 新增的描述符一致性响应
- [[concepts/bidirectional-plugins|Bidirectional Plugins]] - protoc 与插件双向通信方案
- [[concepts/central-feature-registry|Central Feature Registry]] - 中央特性注册表方案
- [[concepts/default-placeholders|Default Placeholders]] - 默认占位符方案
- [[concepts/staged-rollout-for-dynamic-messages|Staged Rollout for Dynamic Messages]] - 渐进式动态消息发布策略
- [[concepts/bootstrapping|Bootstrapping]] - descriptor.proto 在各运行时中的引导编译
- [[concepts/generatorrequest|GeneratorRequest]] - protoc 向生成器传递信息的消息
- [[concepts/runtimes-without-reflection|Runtimes Without Reflection]] - 不支持反射的运行时
- [[concepts/use-generated-pool-for-c++-generators|Use Generated Pool for C++ Generators]] - C++ 生成器使用生成池方案
- [[concepts/c++-generators|C++ Generators]] - C++ 生成器的特性解析策略
- [[concepts/non-c++-generators|Non-C++ Generators]] - 非 C++ 生成器的特性解析策略
- [[concepts/raw_features|raw_features]] - 渐进式发布中的过渡字段
- [[concepts/mergefeatures|MergeFeatures]] - DescriptorPool 获取已解析 FeatureSet 的 API
- [[concepts/getfeatures|GetFeatures]] - FileDescriptor 返回 FeatureSet 的 API
- [[concepts/filedescriptorcopyto|FileDescriptor::CopyTo]] - 序列化为 unresolved runtime features 的方法
- [[concepts/do-nothing|Do Nothing]] - 放弃 Editions 的替代方案

## 要点
- protoc 不能作为特性解析的通用真相来源：它只能通过 import 发现生成器特性，对未被导入的生成器特性无能为力
- 推荐方案让 protoc、各生成器、各运行时各自独立进行 [[concepts/feature-resolution|Feature Resolution]]，仅在彼此之间传递 [[concepts/unresolved-features|Unresolved Features]]，以最小化代码大小与内存开销
- [[concepts/c++-generators|C++ Generators]] 可直接复用现有解析工具并通过 [[concepts/codegenerator|CodeGenerator]] 虚方法注册自己的特性；[[concepts/non-c++-generators|Non-C++ Generators]] 与运行时需复制解析逻辑，但可通过嵌入序列化的 [[concepts/edition-defaults|Edition Defaults]] 避免重复计算
- [[concepts/runtimes-without-reflection|Runtimes Without Reflection]]（如 Java lite、ObjC）由生成器直接把所需已解析特性嵌入自定义对象，无需运行时再做解析
- [[entities/descriptor-proto|descriptor.proto]] 因无法导入任何特性文件而需被特殊对待，可能需要为引导生成额外的辅助信息
- [[concepts/dynamic-messages|Dynamic Messages]] 支持是设计关键约束：方案必须允许在 bypass protoc 的运行时构造 descriptor 时仍能正确处理 editions
- 为保证跨语言一致性，需扩展 [[concepts/conformance-testing|Conformance Testing]] 框架，新增 [[concepts/descriptorconformancerequest|DescriptorConformanceRequest]]/[[concepts/descriptorconformanceresponse|DescriptorConformanceResponse]] 来测试任意对 descriptor 的转换
- 已解析的 FeatureSet 永不对外暴露，仅以包装 API 形式提供，从而借助 [[concepts/hyrums-law|Hyrum's Law]] 保护内部决策的可演进性
- 文档还评估了 [[concepts/default-placeholders|Default Placeholders]]、[[concepts/bidirectional-plugins|Bidirectional Plugins]]、[[concepts/central-feature-registry|Central Feature Registry]] 等替代方案，但均因代码体积、descriptor pool 支持或版本不一致等问题未被采纳