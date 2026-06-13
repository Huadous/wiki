---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/java-lite|java-lite]]"]
tags: [product]
aliases:
  - "Apache Maven"
  - "Maven 构建工具"
---


# Maven

## 基本信息
- Type: product
- Source: [[sources/java-lite|java-lite]]

## 描述
Maven 是 Java 生态系统中广泛使用的依赖管理与项目构建工具，由 Apache 软件基金会维护。在 Protocol Buffers Java Lite 运行时的分发体系中，Maven 扮演着标准分发渠道的角色。Protobuf Java Lite 运行时通过 Maven 中央仓库发布，开发者可以在项目的 `pom.xml` 中声明 `com.google.protobuf:protobuf-javalite` 依赖来引入 Java Lite 运行时，从而在 Android 等对包体积敏感的环境中集成 Protobuf 能力。具体版本号需要从 Maven 仓库（如 mvnrepository.com）选取对应的 Protocol Buffers [Lite] Repository 中的版本。Maven 的标准化依赖管理机制显著降低了开发者在 [[entities/protobuf-java-lite-runtime|protobuf-java-lite-runtime]] 集成流程中的接入成本，是 [[entities/google-gnostic|google-gnostic]] 等 Protobuf 相关生态项目在 Java/Android 端落地时常用的构建基础设施之一。

## 相关实体
- [[entities/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/r8|R8]]

## 相关概念
- 暂无已建立的 concept 页面引用

## 来源提及
- "If you are using Maven, include the following:" — [[sources/java-lite|java-lite]]
- `<dependency> <groupId>com.google.protobuf</groupId> <artifactId>protobuf-javalite</artifactId> <version><!--version--></version> </dependency>` — [[sources/java-lite|java-lite]]
- "And replace <!--version--> with a version from the Maven Protocol Buffers [Lite] Repository." — [[sources/java-lite|java-lite]]