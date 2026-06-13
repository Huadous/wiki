---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client]]"]
tags: [term]
aliases:
  - "brpc::Channel"
  - "Channel 类"
---


# Channel

## 定义
Channel 是 brpc 框架中用于访问服务的核心客户端抽象。当通过 Channel 访问 HTTP/H2 服务时，创建 Channel 时须通过 `ChannelOptions.protocol` 指定协议类型（`PROTOCOL_HTTP` 或 `PROTOCOL_H2`），且 `Channel::Init` 的第一个参数可为任意合法 URL，但框架仅使用其中的 host 与 port 部分。

## 关键特征
- 必须通过 `ChannelOptions.protocol` 显式指定协议（如 `PROTOCOL_HTTP` 或 `PROTOCOL_H2`），用于 HTTP/H2 服务的访问。
- `Channel::Init` 的第一个参数接受任意合法 URL，但仅解析其中的 host 与 port，其余部分（如 path、scheme、query 等）会被丢弃。
- 支持 BNS（Baidu Naming Service）等命名服务地址形式，便于通过服务名访问后端。
- 可区分代理（proxy）场景与直连场景，配置方式有所不同。
- Channel 复用底层连接，而具体的请求 URI 由 `cntl.http_request().uri()` 单独指定，从而实现同一连接基础上访问不同 URI 的服务。

## 应用
- 作为 brpc 客户端访问 HTTP/H2 服务的入口对象，统一封装连接管理与协议协商。
- 通过 BNS 等命名服务实现服务发现与负载均衡场景下的客户端接入。
- 在代理或直连模式下使用同一套 Channel 抽象访问上游服务。
- 与 `cntl.http_request().uri()` 配合，复用一条连接访问同一 host 上的多个不同 URI。

## 相关概念
- [[concepts/http-h2-client|HTTP/h2 客户端]]
- [[concepts/url-host-field|URL 与 Host 字段]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "brpc::Channel可访问http/h2服务，ChannelOptions.protocol须指定为PROTOCOL_HTTP或PROTOCOL_H2。" — [[sources/http_client]]
- "设定好协议后，`Channel::Init`的第一个参数可为任意合法的URL。注意：允许任意URL是为了省去用户取出host和port的麻烦，`Channel::Init`只用其中的host及port，其他部分都会丢弃。" — [[sources/http_client]]