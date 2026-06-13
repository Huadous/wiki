---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "product"
aliases:
  - "sofa-pbrrc"
  - "sofa_pbrrc协议"
  - "sofa-pbrpc"
  - "sofa-pbrrc"
  - "sofa_pbrrc协议"
  - "sofa_pbrpc协议"
  - "sofa-pbrrc"
  - "sofa_pbrrc协议"
  - "sofa-pbrpc"
  - "sofa-pbrrc"
  - "sofa_pbrrc协议"
---

## Related Concepts
- [[concepts/baidu_std-protocol|baidu_std]]：brpc支持的另一种标准协议，在编码格式和连接管理上与sofa_pbrpc存在差异
- 协议自动检测：brpc服务器自动识别并处理sofa_pbrpc协议的能力
- 多协议支持：brpc在同一端口同时处理多种RPC协议的架构设计
- [[concepts/hulu_pbrpc|hulu_pbrpc]]：同类基于nshead和Protobuf的RPC协议
- [[concepts/nova_pbrpc|nova_pbrpc]]：另一种brpc支持的RPC协议
- [[concepts/public_pbrpc|public_pbrpc]]：另一种brpc支持的RPC协议
- [[concepts/nshead_mcpack|nshead_mcpack]]：另一类基于nshead的协议
- [[concepts/baidu_std-protocol|baidu_std]]：在编码格式和连接管理上与sofa_pbrpc存在差异的标准协议

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
> - "Protocol of sofa-pbrpc, shown as 'sofa_pbrpc', enabled by default."
> - "Server detects supported protocols automatically, without assignment from users."
> - "sofa-pbrpc is another RPC protocol based on nshead and Protobuf, similar to hulu-pbrpc, and is also enabled by default in brpc. It originated from Ant Financial (formerly the SOFA team) and is widely used within Baidu."
> - "Protocol of sofa-pbrpc, shown as 'sofa_pbrpc', enabled by default."
> - "Server is able to accept connections with different protocols from one port, users don't need to assign different ports for different protocols."

## Additional Information
sofa_pbrpc是蚂蚁金服开源的RPC协议，基于protobuf。brpc服务器默认支持该协议，无需额外配置。它在编码格式和连接管理上与baidu_std有所不同，但brpc通过协议自动检测机制可以无缝处理。源文件中将其列为默认支持的协议之一。该协议也称为Sofa protobuf RPC。