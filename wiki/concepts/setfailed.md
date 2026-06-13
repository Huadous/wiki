---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "method"
aliases:
  - "Controller.SetFailed"
  - "设置RPC失败"
  - "SetFailed方法"
  - "Controller::SetFailed"
  - "Controller.SetFailed"
  - "设置RPC失败"
  - "SetFailed方法"
---

## Related Concepts
- [[concepts/done|done (protobuf Closure)]]
- [[concepts/closureguard|ClosureGuard]]
- [[concepts/synchronous-service|Synchronous Service]]
- [[concepts/asynchronous-service|Asynchronous Service]]
- [[concepts/elimiter|ELIMIT]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-controller|brpc::Controller]]

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Call Controller.SetFailed() to set the RPC to be failed."
> - "If error occurs during sending response, framework calls the method as well."
> - "If SetFailed() is called, error information is sent to client instead of normal content."
> - "When client receives the response, its controller will be SetFailed() as well and Controller::Failed() will be true."
> - "Controller.SetFailed() sets status-code as well with the value closest to the error-code in semantics."

> **Source: [[sources/server|server]]**
> - "调用Controller.SetFailed()可以把当前调用设置为失败，当发送过程出现错误时，框架也会调用这个函数。"
> - "用户一般是在服务的CallMethod里调用这个函数，比如某个处理环节出错，SetFailed()后确认done->Run()被调用了就可以跳出函数了(若使用了ClosureGuard，跳出函数时会自动调用done，不用手动)。"
> - "Controller.SetFailed也会设置status-code，值是与错误码含义最接近的status-code，没有相关的则填500错误(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR)。如果你要覆盖status_code，设置代码一定要放在SetFailed()后，而不是之前。"