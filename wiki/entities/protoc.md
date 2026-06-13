---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/overview]]"
  - "[[sources/techniques]]"
  - "[[sources/editions]]"
  - "[[sources/proto3]]"
  - "[[sources/editions-what-are-protobuf-editions]]"
  - "[[protobuf/proto3.md]]"
  - "[[protobuf/java-lite.md]]"
  - "[[protobuf/implementing_proto3_presence.md]]"
  - "[[protobuf/field_presence.md]]"
  - "[[protobuf/editions.md]]"
tags:
  - "product"
aliases:
  - "Protocol Buffers compiler"
  - "protoc compiler"
---

## Related Entities
- [[entities/google-inc|Google Inc.]]
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protocol-buffers-v3-15-0|Protocol Buffers v3.15.0]]
- [[entities/protocol-buffers-v3-12-0|Protocol Buffers v3.12.0]]

## Related Concepts
- [[concepts/protocol-buffers|Protocol Buffers]]
- [[concepts/.proto-file|.proto file]]
- [[concepts/message-type|Message Type]]
- [[concepts/feature-proto3-optional|FEATURE_PROTO3_OPTIONAL]]
- [[concepts/code-generator|Code Generator]]
- [[concepts/proto3-optional-fields|proto3 optional fields]]
- [[concepts/proto3|proto3]]
- [[concepts/explicit-presence-discipline|Explicit presence discipline]]
- [[concepts/optional-label|Optional label]]

## Mentions in Source
> **Source: [[sources/proto3|proto3]]**
> - "If no syntax is specified, the protocol buffer compiler will assume you are using proto2."
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file, including getting and setting field values, serializing your messages to an output stream, and parsing your messages from an input stream."
> - "The protoc compiler will generate error messages if any future developers try to use these reserved field numbers."

> **Source: [[sources/java-lite|java-lite]]**
> - "You can generate Java Lite code for your .proto files:"
> - "$ protoc --java_out=lite:${OUTPUT_DIR} path/to/your/proto/file"
> - "The \"optimize_for = LITE_RUNTIME\" option in the .proto file no longer has any effect on Java code."

> **Source: [[sources/implementing_proto3_presence|implementing_proto3_presence]]**
> - "If you try to run `protoc` on a file with proto3 optional fields, you will get an error because the feature is still experimental."
> - "Pass `--experimental_allow_proto3_optional` to protoc."
> - "Make your filename (or a directory name) contain the string `test_proto3_optional`."

> **Source: [[sources/field_presence|field_presence]]**
> - "Run protoc (at least v3.15, or v3.12 using --experimental_allow_proto3_optional flag)."
> - "Presence tracking for proto3 messages is enabled by default since v3.15.0 release, formerly up until v3.12.0 the --experimental_allow_proto3_optional flag was required when using presence tracking with protoc."

> **Source: [[sources/editions|editions]]**
> - "When you run the protocol buffer compiler on a .proto, the compiler generates the code in your chosen language you'll need to work with the message types you've described in the file"
> - "The protoc compiler will generate error messages if any future developers try to use these reserved field numbers."
> - "The protoc parser validates that a given proto definition file is parseable."