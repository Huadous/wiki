---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]"
  - "[[protobuf/editions-group-migration-issues.md]]"
tags:
  - "method"
aliases:
  - "DELIMITED encoding"
  - "DELIMITED 消息编码"
  - "Delimited encoding"
  - "DELIMITED encoding"
  - "DELIMITED 消息编码"
---

## Related Concepts
- [[concepts/features-message-encoding|features.message_encoding]]
- [[concepts/group-encoding|Group encoding]]
- [[concepts/messageschema|MessageSchema]]
- [[concepts/rawmessageinfo|RawMessageInfo]]
- [[concepts/group-fields|Group fields]]
- [[concepts/group-like-fields|Group-like fields]]
- [[concepts/editions|Editions]]
- [[concepts/text-format|Text format]]
- [[concepts/wire-format|Wire format]]

## Related Entities
- [[entities/protocol-buffers|Protocol Buffers]]
- [[entities/edition-2023|Edition 2023]]

## Mentions in Source
> **Source: [[sources/editions-java-lite-for-editions|editions-java-lite-for-editions]]**
> - "In the compiler, message fields with `features.message_encoding = DELIMITED` should be treated as a group *before* encoding message info."
> - "will be encoded and treated by `MessageSchema` like its pre-editions equivalent below."

> **Source: [[sources/editions-group-migration-issues|editions-group-migration-issues]]**
> - "Address some unexpected issues in delimited encoding in edition 2023 before its OSS release."
> - "He discovered that our new message encoding feature piggybacked a bit too much on the old group logic, and actually ended up being virtually useless in general."