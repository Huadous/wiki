---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/java-lite]]"]
tags: [method]
aliases:
  - "ProGuard 混淆规则"
  - "ProGuard Rules"
  - "proguard-rules.pro 配置"
---


# ProGuard obfuscation rules

## 定义
ProGuard 混淆规则是指通过 `-keep` 等指令控制代码混淆器（如 R8）保留特定类、方法和字段的命名与结构，从而避免运行时反射失败。在使用 [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]] 的项目中，开发者需要在 `proguard-rules.pro` 文件中添加 `-keep class * extends com.google.protobuf.GeneratedMessageLite { *; }`，以确保所有继承自 `GeneratedMessageLite` 的 protobuf 生成类及其成员不被 [[entities/r8|R8]] 重命名。这是 Java Lite Runtime 在生产构建中正常工作的必要配置。

## 关键特征
- 通过 `-keep` 指令精确控制类、方法、字段的保留范围，防止被混淆器重命名
- 采用通配符 `*` 匹配所有继承自指定基类（本场景中为 `com.google.protobuf.GeneratedMessageLite`）的子类
- 末尾的 `{ *; }` 表示保留匹配类的所有成员（方法与字段）
- 是 Android 启用代码压缩与混淆（minifyEnabled true）时的强制配置项
- 规则在构建时生效，影响最终 APK / AAB 中代码的符号表与名称

## 应用
- Android 应用集成 [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]] 时，必须在 `proguard-rules.pro` 中加入对应 `-keep` 规则，否则 R8 会重命名 protobuf 生成的 `MessageLite` 子类，导致运行时反射（如 `mergeFrom`、`writeTo` 内部调用）出现 `ClassNotFoundException` 或 `NoSuchMethodError`
- 适用于 release 构建以及任何启用了 R8 / ProGuard 的构建变体
- 在使用 [[entities/android|Android]] Gradle Plugin 的项目中，可将规则写入模块级 `proguard-rules.pro` 或通过 `consumerProguardFiles` 由依赖库自动注入

## 相关概念
- [[concepts/reflection-based-serialization|Reflection-based serialization]]

## 相关实体
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]
- [[entities/r8|R8]]
- [[entities/android|Android platform]]
- [[entities/maven|Apache Maven]]

## 来源提及
- "Until the issues is resolved you need to add the following line to your proguard-rules.pro file inside your project:" — [[sources/java-lite]]
- "-keep class * extends com.google.protobuf.GeneratedMessageLite { *; }" — [[sources/java-lite]]