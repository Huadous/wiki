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
  - "网络端点"
  - "EndPoint"
  - "Butil.EndPoint"
  - "网络端点"
  - "EndPoint"
---

## Related Concepts
- [[concepts/远程地址|远程地址]]
- [[concepts/本地地址|本地地址]]
- [[concepts/solicited标志|solicited标志]]
- [[concepts/ssl|SSL]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/brpc-controller|brpc::Controller]]
- [[entities/rdmaendpoint|rdmaendpoint]]
- [[entities/nginx|nginx]]

## Mentions in Source
**Source: [[sources/en_server|en_server]]**
- "controller->remote_side() gets address of the client which sent the request. The return type is butil::EndPoint."
- "controller->local_side() gets server-side address of the RPC connection, return type is butil::EndPoint."
- "LOG(INFO) << "remote_side=" << cntl->remote_side(); printf("remote_side=%s\n", butil::endpoint2str(cntl->remote_side()).c_str());"

**Source: [[sources/server|server]]**
- "`controller->remote_side()`可获得发送该请求的client地址和端口，类型是butil::EndPoint。"
- "controller->local_side()获得server端的地址，类型是butil::EndPoint。"
- "关于IPV6和Unix domain socket的使用，详见 [EndPoint](endpoint.md)。"