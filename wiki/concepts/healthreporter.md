---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "other"
aliases:
  - "健康报告器"
  - "自定义健康检查"
  - "Health Reporter"
---

## Related Concepts
- [[concepts/builtin-service|内置服务]]
- [[concepts/json2pb|json2pb]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc::Server|brpc::Server]]
- [[entities/brpc::ServerOptions|brpc::ServerOptions]]

## Mentions in Source
> **Source: [[sources/server|server]]**
> - "/health页面默认返回'OK'，若需定制/health页面的内容：先继承[HealthReporter](https://github.com/apache/brpc/blob/master/src/brpc/health_reporter.h)，在其中实现生成页面的逻辑（就像实现其他http service那样），然后把实例赋给ServerOptions.health_reporter，这个实例不被server拥有，必须保证在server运行期间有效。"