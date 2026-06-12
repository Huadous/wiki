---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "term"
aliases:
  - "brpc::EOVERCROWDED"
  - "过载错误码"
---

## Related Concepts
- [[concepts/最大并发数|最大并发数]]
- [[concepts/自动并发限制器|自动并发限制器]]
- [[concepts/ELIMIT|ELIMIT]]
- [[concepts/服务器选项|服务器选项]]
- [[concepts/过载保护|过载保护]]
- [[concepts/限流|限流]]
- [[concepts/AutoConcurrencyLimiter|AutoConcurrencyLimiter]]
- [[concepts/ServerOptions|ServerOptions]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/echoservice|echoservice]]

## Mentions in Source
> **Source: [[sources/en_server]]**
> - "Set ServerOptions.ignore_eovercrowded. Default value is 0 which means not ignored."
> - "server.IgnoreEovercrowdedOf("example.EchoService.Echo") = true;"
> - "When method-level and server-level ignore_eovercrowded are both set, if any one of them is set to true, eovercrowded will be ignored."
> - "Set ServerOptions.ignore_eovercrowded. Default value is 0 which means not ignored." — [[sources/en_server|en_server]]
> - "When method-level and server-level ignore_eovercrowded are both set, if any one of them is set to true, eovercrowded will be ignored." — [[sources/en_server|en_server]]