---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/java-lite|java-lite]]"
  - "[[protobuf/java-lite.md]]"
tags:
  - "standard"
aliases:
  - "LITE_RUNTIME"
  - "optimize_for = LITE_RUNTIME"
  - "Protobuf LITE_RUNTIME 编译选项"
  - "Code size optimization"
  - "LITE_RUNTIME"
  - "optimize_for = LITE_RUNTIME"
  - "Protobuf LITE_RUNTIME 编译选项"
---

## Description
LITE_RUNTIME 最初是 `.proto` 文件中 `optimize_for` 枚举的取值之一，与 `SPEED`、`CODE_SIZE` 并列，用于指示编译器生成与精简版（Lite）Java 运行时兼容的代码。该选项的设计初衷是为了满足 Android 等资源受限平台对 APK 体积与运行时依赖的严格要求——Java Lite 运行时通过剥离完整 Java 运行时的部分功能（如基于反射生成的 `hashCode`、`equals` 与序列化方法）来获得更小的二进制体积。然而，根据 [[sources/java-lite|java-lite]] 的官方说明，"optimize_for = LITE_RUNTIME" 在 `.proto` 文件中"no longer has any effect"，即在文件内声明该选项不再影响 Java 代码生成结果。官方推荐的替代方式是通过 `protoc --java_out=lite:${OUTPUT_DIR}` 命令行参数显式指定 Lite 输出模式，且只有在这种方式下才适用 [[concepts/abi-stability|ABI 稳定性]] 保证。这一废弃决定与 Java Lite 运行时的设计权衡直接相关：源码文档明确指出"In order to achieve maximum performance and code size, we do NOT guarantee API/ABI stability for Java Lite"，即体积与性能优化的代价是放弃稳定性承诺。因此，Java Lite 适用于对体积敏感、对稳定性要求不高的移动端场景，而完整 Java 运行时则更适合服务端等需要稳定 API 的环境。

## Related Concepts
- [[concepts/abi-stability|ABI 稳定性]]
- [[concepts/protobuf-java-lite-runtime|Protobuf Java Lite Runtime]]
- [[concepts/reflection-based-serialization|Reflection-based serialization]]

## Related Entities
- [[entities/protobuf-java-lite-runtime|protobuf-java-lite-runtime]]
- [[entities/android|android]]
- [[entities/google-inc|google-inc]]
- [[entities/r8|r8]]
- [[entities/maven|maven]]

## Mentions in Source

**Source: [[sources/java-lite|java-lite]]**
- The "optimize_for = LITE_RUNTIME" option in the .proto file no longer has any effect on Java code.
- `$ protoc --java_out=lite:${OUTPUT_DIR} path/to/your/proto/file`
- The Protobuf Java Lite runtime is separated from the main Java runtime because it's designed and implemented with different constraints. In particular, the Java Lite runtime is much smaller which makes it more suitable to be used on Android.
- In order to achieve maximum performance and code size, we do NOT guarantee API/ABI stability for Java Lite.