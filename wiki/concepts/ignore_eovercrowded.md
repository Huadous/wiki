---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "term"
aliases:
  - "忽略EOVERCROWDED"
  - "ignore_eovercrowded配置"
  - "brpc过载忽略"
  - "Ignore Eovercrowded"
  - "忽略EOVERCROWDED"
  - "ignore_eovercrowded配置"
  - "brpc过载忽略"
---

## Related Concepts
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/brpc-controller|brpc::Controller]]
- [[concepts/serveroptions|brpc::ServerOptions]]
- [[concepts/bthread|bthread 执行队列]]
- [[concepts/max-concurrency|最大并发控制]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]
- [[entities/echoservice|echoservice]]
- [[entities/myechoservice|myechoservice]]
- [[entities/brpc-server|brpc::Server]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Set ServerOptions.ignore_eovercrowded. Default value is 0 which means not ignored."
> - "server.IgnoreEovercrowdedOf('example.EchoService.Echo') = true;"
> - "When method-level and server-level ignore_eovercrowded are both set, if any one of them is set to true, eovercrowded will be ignored."
> - "NOTE: No service-level ignore_eovercrowded."

> **Source: [[sources/server|server]]**
> - "设置ServerOptions.ignore_eovercrowded，默认值0代表不忽略"
> - "server.IgnoreEovercrowdedOf("...") = ...可设置method级别的ignore_eovercrowded。也可以通过设置ServerOptions.ignore_eovercrowded一次性为所有的method设置忽略eovercrowded。"
> - "当ServerOptions.ignore_eovercrowded和server.IgnoreEovercrowdedOf("...")=...同时被设置时，任何一个设置为true，就表示会忽略eovercrowded。"