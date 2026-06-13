---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/techniques]]"
  - "[[protobuf/editions-editions-life-of-a-featureset.md]]"
tags:
  - "term"
aliases:
  - "FileDescriptorProto集合"
  - "描述符集"
---

## Related Concepts
- [[concepts/self-describing-messages|Self-describing Messages]]
- [[concepts/message-type|Message type]]
- [[concepts/conformance-testing|Conformance Testing]]
- [[concepts/bootstrapping|Bootstrapping]]
- [[concepts/feature-resolution|Feature Resolution]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/protoc|protoc]]
- [[entities/filedescriptorproto|FileDescriptorProto]]
- [[entities/descriptorconformancerequest|DescriptorConformanceRequest]]
- [[entities/descriptorconformanceresponse|DescriptorConformanceResponse]]

## Mentions in Source
> **Source: [[sources/techniques|techniques]]**
> - "protoc can output a FileDescriptorSet — which represents a set of .proto files — using the --descriptor_set_out option."
> - "google.protobuf.FileDescriptorSet descriptor_set;"

> **Source: [[sources/editions-editions-life-of-a-featureset|editions-editions-life-of-a-featureset]]**
> - "message DescriptorConformanceRequest {
  // The file under test, pre-transformation.
  FileDescriptorProto file = 1;
  // The pool of dependencies and feature files required for build.
  FileDescriptorSet dependencies = 2;
}"
> - "message DescriptorConformanceResponse {
  // The transformed file.
  FileDescriptorProto file = 1;
  // Any additional features added during build.
  FileDescriptorSet added_features = 2;
}"