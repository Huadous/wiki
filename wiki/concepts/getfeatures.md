---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-editions-life-of-a-featureset]]"]
tags: [method]
aliases:
  - "FileDescriptor::GetFeatures"
  - "GetFeatures API"
---


# GetFeatures

## 定义
GetFeatures 是 protobuf 中 `FileDescriptor` 上的 C++ API 方法,用于返回该描述符所关联的 `FeatureSet` 对象。在推荐方案下,生成器将自己的特性 proto 文件(如 `lang_features.proto`)通过 `DescriptorPool` 注册后,通过 GetFeatures 获得的 `FeatureSet` 对象将始终包含完全解析的该语言特性。该方法与 `MergeFeatures` 共同构成了 C++ 生成器访问已解析特性的核心 API 入口。

## 关键特征
- 属于 `FileDescriptor` 的 C++ 运行时 API,返回与该文件描述符关联的 `FeatureSet` 实例
- 依赖 `DescriptorPool` 完成特性解析:默认情况下,`DescriptorPool` 仅解析全局特性与 C++ 特性
- 支持通过 `DescriptorPool` 的新方法以新的特性集替换 C++ 特性,从而扩展特性解析范围
- 与 `MergeFeatures` 配对使用,使生成器无需重新实现特性解析逻辑即可获取已完全解析的特性集
- 解析结果对调用方透明:返回的 `FeatureSet` 始终是合并/解析完毕的最终视图

## 应用
- **C++ 代码生成器**:在 protobuf 编译插件(`CodeGenerator`)中,通过 `GetFeatures` 读取目标 `.proto` 文件对应的语言特性集,以决定生成代码的具体行为
- **跨语言生成器接入**:当生成器注册了自己的 `lang_features.proto` 后,可以通过该 API 直接获取该语言特性的已解析值,避免重复实现解析流程
- **Editions 特性决策**:在 Editions 体系下,基于 GetFeatures 返回的 `FeatureSet` 对字段存在性、编码方式、默认值等特性做出代码生成决策
- **特性验证与诊断**:工具可借助 GetFeatures 检查某一 `FileDescriptor` 的有效特性配置

## 相关概念
- [[concepts/feature-resolution|Feature Resolution]]
- [[concepts/resolved-features|Resolved Features]]
- [[concepts/generator-features|Generator Features]]
- [[concepts/c++-generators|C++ Generators]]
- [[concepts/descriptor-pool|Descriptor Pool]]

## 相关实体
- [[entities/feature-set|FeatureSet]]
- [[entities/descriptor-pool|DescriptorPool]]
- [[entities/code-generator|CodeGenerator]]

## 来源提及
- "By default, `DescriptorPool` will only resolve the global features and the C++ features (since this is the C++ runtime). A new method will be added to `DescriptorPool` that allows new feature sets to replace the C++ features for feature resolution." — [[sources/editions-editions-life-of-a-featureset]]