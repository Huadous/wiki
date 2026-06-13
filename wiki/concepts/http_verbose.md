---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "other"
aliases:
  - "调试标志"
  - "HTTP verbose"
  - "-http_verbose"
---

## Related Entities
- [[entities/brpc|brpc]]

## Overview
http_verbose是brpc中的一个调试标志，用于打印所有HTTP请求和响应的内容。开启后，服务端会输出详细的HTTP报文信息，方便开发人员定位问题。

## Usage
通过设置brpc的flag（如`-http_verbose`）即可启用。该标志应仅用于调试环境，不可用于线上服务。

## Important Notes
- 仅用于调试环境，不可用于线上服务
- 通过`-http_verbose`标志启用
- 会打印所有HTTP请求和响应的内容