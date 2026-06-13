---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/combo_channel]]"
  - "[[sources/en_io]]"
  - "[[sources/backup_request]]"
  - "[[brpc/io.md]]"
  - "[[brpc/en_backup_request.md]]"
tags:
  - "method"
aliases:
  - "SelectiveChannel"
  - "schan"
  - "选择通道"
---

## Related Concepts
- [[concepts/load-balancing|负载均衡]]
- [[concepts/health-check|健康检查]]
- [[concepts/backup-request|backup request]]
- [[concepts/wait-free-mpsc|Wait-free MPSC 链表]]
- [[concepts/socket-unique-ptr|SocketUniquePtr]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/bns|bns]]
- [[entities/braft|braft]]
- [[entities/socket|socket]]
- [[entities/subchannel|subchannel]]
- [[entities/inputmessenger|InputMessenger]]
- [[entities/exampleselective_echo_c++|exampleselective_echo_c++]]

## Mentions in Source

> **Source: [[sources/combo_channel|combo_channel]]**
> - "SelectiveChannel（有时被称为"schan"）按负载均衡算法访问其包含的Channel，相比普通Channel它更加高层：把流量分给sub channel，而不是具体的Server。"
> - "SelectiveChannel的重试独立于其中的sub channel，当SelectiveChannel访问某个sub channel失败后（本身可能重试），它会重试另外一个sub channel。"
> - "目前SelectiveChannel要求request必须在RPC结束前有效，其他channel没有这个要求。"

> **Source: [[sources/en_io|en_io]]**
> - "SubChannel in SelectiveChannel is also managed by Socket, making SelectiveChannel choose a SubChannel just like a normal channel choosing a downstream server."
> - "The faked Socket even implements health checking."

> **Source: [[sources/backup_request|backup_request]]**
> - "【推荐】建立一个开启backup request的SelectiveChannel，其中包含两个sub channel。"
> - "SelectiveChannel的例子见example/selective_echo_c++，具体做法请参考上面的过程。"

> **Source: [[sources/io|io]]**
> - "比如SelectiveChannel中的每个Sub Channel都被置入了一个Socket中，这样SelectiveChannel可以像普通channel选择下游server那样选择一个Sub Channel进行发送。"
> - "这个假Socket甚至还实现了健康检查。"

> **Source: [[sources/en_backup_request|en_backup_request]]**
> - "[Recommended] Define a SelectiveChannel that sets backup request, in which contains two sub channel."
> - "The visiting process of this SelectiveChannel is similar to the above situation. It will visit one sub channel first. If the response is not returned after channelOptions.backup_request_ms ms, then another sub channel is visited."