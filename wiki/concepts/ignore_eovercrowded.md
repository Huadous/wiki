---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
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

## Description
`ignore_eovercrowded` 通过两级作用域机制控制系统的过载处理行为。服务器级别设置通过 `ServerOptions.ignore_eovercrowded` 作用于所有方法，方法级别设置则通过 `server.IgnoreEovercrowdedOf("服务名.方法名")` 针对特定 RPC 方法独立配置。两级设置采用"逻辑或"规则，只要任一作用域为 `true`，该方法的过载检测即被忽略。默认值 `false`（值为 0）表示不忽略过载，即系统检测到过载时会正常拒绝请求并返回 `ELIMIT` 错误码。开启后，请求在过载状态下仍被处理，这可能加重系统负载，因此建议仅用于对过载不敏感的请求或测试环境。需注意，brpc 框架不存在服务级别（service-level）的 `ignore_eovercrowded` 设置，只有方法和服务器两级。

## Related Concepts
- [[concepts/max_concurrency|max_concurrency]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/brpc-controller|brpc::Controller]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]
- [[entities/echoservice|echoservice]]
- [[entities/myechoservice|myechoservice]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Set ServerOptions.ignore_eovercrowded. Default value is 0 which means not ignored."
> - "server.IgnoreEovercrowdedOf('example.EchoService.Echo') = true;"
> - "When method-level and server-level ignore_eovercrowded are both set, if any one of them is set to true, eovercrowded will be ignored."
> - "NOTE: No service-level ignore_eovercrowded."