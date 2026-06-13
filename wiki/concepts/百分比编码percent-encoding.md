---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_http_service]]"
  - "[[brpc/http_service.md]]"
tags:
  - "standard"
aliases:
  - "URL编码"
  - "百分号编码"
  - "Percent-encoding"
  - "Percent-encoding (in brpc)"
  - "URL编码"
  - "百分号编码"
  - "Percent-encoding"
  - "percent encoding"
  - "URL编码"
  - "百分号编码"
  - "Percent-encoding"
  - "Percent-encoding (in brpc)"
  - "URL编码"
  - "百分号编码"
  - "Percent-encoding"
---

## Description
Percent encoding 是 URI 规范中用于表示保留字符的标准编码机制，依据 RFC 3986 第 2.2 节定义。该标准将需要编码的 reserved 字符分为两类：gen-delims（包括 `:`、`/`、`?`、`#`、`[`、`]`、`@`）和 sub-delims（包括 `!`、`$`、`&`、`'`、`(`、`)`、`*`、`+`、`,`、`;`、`=`）。在 brpc 处理 Base64 编码查询字符串的实际场景中，由于 Base64 输出可能包含 `=` 等 sub-delims 字符，若直接拼接到 URI 中会导致解析错误，因此文档建议对 URI 先做 percent encoding 再进行 Base64 编码，对应的解码流程则先做 percent decoding 再用 Base64 解码。这一做法与 BASE64编码查询字符串问题 的解决方案直接相关，也是 [[entities/brpc|brpc]] HTTP 服务中处理二进制安全查询参数的推荐模式。

## Related Concepts
- [[concepts/base64编码查询字符串问题|BASE64编码查询字符串问题]]
- [[concepts/查询字符串|查询字符串]]
- [[concepts/uri规范|URI规范]]
- [[concepts/base64编码|BASE64编码]]
- [[concepts/http参数|HTTP参数]]
- [[concepts/百分号编码|Percent Encoding（百分号编码）]]

## Related Entities
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/http_service|http_service]]**
> - "根据[HTTP协议](http://tools.ietf.org/html/rfc3986#section-2.2)中的要求，以下字符应该使用%编码"
> - "第二个方法是在对这个URI做[percent encoding](https://en.wikipedia.org/wiki/Percent-encoding)，解码时先做percent decoding再用Base64."