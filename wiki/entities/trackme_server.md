---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "trackme-server"
  - "brpc trackme server"
---

## Related Entities

- [[entities/brpc|brpc]] — trackme_server 所跟踪和监控的 RPC 框架，trackme_server 程序随 brpc 项目发布

## Related Concepts

- [[concepts/实例追踪|实例追踪]] — trackme_server 所实现的核心功能目标
- [[concepts/rpcz|rpcz]] — 与实例追踪密切相关的 brpc 跟踪/分析能力

## Mentions in Source

> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "We provide a program to help you to track and monitor all brpc instances."
> - "Just run trackme_server somewhere and launch need-to-be-tracked instances with -trackme_server=SERVER."
> - "The trackme_server will receive pings from instances periodically and print logs when it does."

> **Source: [[sources/getting_started|getting_started]]**
> - "我们提供了一个程序去帮助你追踪和监控所有brpc实例。 只需要在某处运行 [trackme_server](https://github.com/apache/brpc/tree/master/tools/trackme_server/) 然后再带着 -trackme_server=SERVER参数启动需要被追踪的实例。"
> - "trackme_server将从实例周期性地收到ping消息然后打印日志。"