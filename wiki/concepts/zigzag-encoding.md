---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/encoding]]"
tags:
  - "method"
aliases:
  - "ZigZag"
  - "ZigZag编码"
---

## Related Concepts
- [[concepts/Varint|Varint]]
- [[concepts/Two's-complement|Two's complement]]
- [[concepts/protobuf-wire-format|Protocol Buffers Wire Format]]

## Related Entities
- [[entities/Protocol-Buffers|Protocol Buffers]]

## Mentions in Source
> **Source: [[sources/encoding|encoding]]**
> - "sintN uses the 'ZigZag' encoding instead of two's complement to encode negative integers."
> - "For example: Signed Original 0 Encoded As 0, -1 -> 1, 1 -> 2, -2 -> 3, 0x7fffffff -> 0xfffffffe, -0x80000000 -> 0xffffffff."
> - "When the sint32 or sint64 is parsed, its value is decoded back to the original, signed version."
> - "Positive integers p are encoded as 2 * p (the even numbers), while negative integers n are encoded as 2 * |n| - 1 (the odd numbers)."
> - "In other words, each value n is encoded using (n << 1) ^ (n >> 31) for sint32s, or (n << 1) ^ (n >> 63) for the 64-bit version."