---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/client|client]]"
  - "[[brpc/avalanche.md]]"
tags:
  - "standard"
aliases:
  - "RetryPolicy"
  - "重试策略接口"
---

## Related Concepts
- [[concepts/重试退避|重试退避]]
- [[concepts/backup request|backup request]]
- [[concepts/连接方式|连接方式]]
- [[concepts/流量放大|流量放大]]
- [[concepts/雪崩|雪崩]]

## Related Entities
- [[entities/brpc::ChannelOptions|brpc::ChannelOptions]]
- [[entities/brpc::Controller|brpc::Controller]]
- [[entities/brpc|brpc]]

## Mentions in Source

> **Source: [[sources/client|client]]**
> - "用户可以通过继承brpc::RetryPolicy自定义重试条件。比如brpc默认不重试http/h2相关的错误，而你的程序中希望在碰到HTTP_STATUS_FORBIDDEN (403)时重试，可以这么做："
> - "// 给ChannelOptions.retry_policy赋值就行了。// 注意：retry_policy必须在Channel使用期间保持有效，Channel也不会删除retry_policy，所以大部分情况下RetryPolicy都应以单例模式创建。"

> **Source: [[sources/avalanche|avalanche]]**
> - "注意考察重试发生时的行为，特别是在定制RetryPolicy时。如果你只是用默认的brpc重试，一般是安全的。"
> - "但用户程序也常会自己做重试，比如通过一个Channel访问失败后，去访问另外一个Channel，这种情况下要想清楚重试发生时最差情况下请求量会放大几倍，服务是否可承受。"