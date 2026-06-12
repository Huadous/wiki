---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
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

## Description
SetFailed是brpc框架中服务端异常处理的核心接口。调用`Controller::SetFailed()`后，框架会构造一个包含错误信息的响应返回给客户端，替代正常的protobuf响应体。如果错误发生在发送响应过程中，框架也会自动调用该方法。在异步服务中，SetFailed通常与`done->Run()`配合使用，且推荐结合`ClosureGuard`确保在异步回调正确调用前执行SetFailed操作。当客户端接收到失败的响应时，其`Controller`也会被同步设置为失败状态，使得`Controller::Failed()`返回`true`。如果使用了HTTP协议，SetFailed会根据错误码的语义自动选择最接近的HTTP状态码（如默认映射为500）。该方法具有幂等性，多次调用等效于一次调用，使用最后设定的错误信息。

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