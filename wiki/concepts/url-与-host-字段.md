---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/http_client|http_client]]"]
tags: [term]
aliases:
  - "Host 字段"
  - "URI 处理"
  - "URL Host Field Handling"
---


# URL 与 Host 字段

## 定义
URL 与 Host 字段是指 brpc 框架在构造 HTTP/H2 请求时，对请求 URL 中的 `Host` 头（HTTP/1.1）或 `:authority` 伪头（HTTP/2）所遵循的一套自动填充与解析规则。该机制确保请求的目标主机信息能够被正确传递到服务端。

## 关键特征
- **用户优先**：若用户自行填写了 `host` 字段（大小写不敏感），框架不会对其做任何修改。
- **URL 内嵌 host 提取**：若 URL 中包含 host（如 `http://www.foo.com/path`），框架自动将该值填入 `Host` 字段。
- **域名兜底**：若 URL 不含 host，但 `Channel` 初始化的地址为域名形式，则使用该域名作为 `Host`。
- **IP+Port 兜底**：若以上条件都不满足，框架会使用目标 server 的 IP 与 port 作为 `Host`（例如地址为 `10.46.188.39:8989` 的 http server 将会看到 `Host: 10.46.188.39:8989`）。
- **H2 协议对应字段**：在 HTTP/2 协议中，对应的字段名为 `:authority`。
- **地址分离**：`Channel.Init()` 与 `cntl.http_request().uri()` 可以不同，二者解耦。

## 应用
- **命名服务场景**：在使用 BNS（百度命名服务）等返回多节点信息的服务时，URL 可保持不变，Host 字段由框架根据实际选中的节点自动填充，从而正确路由到目标 server。
- **HTTP 代理场景**：在 HTTP 代理转发场景中，可将目标地址信息写入 Host 字段，而 URI 部分保留通用路径，实现灵活的代理转发逻辑。

## 相关概念
- [[concepts/channel|Channel]]
- [[concepts/http-h2-client|HTTP/h2 客户端]]

## 相关实体
- [[entities/examplehttp_c++|http_client.cpp 示例]]

## 来源提及
- 若用户自己填写了"host"字段(大小写不敏感)，框架不会修改。 — [[sources/http_client|http_client]]
- 若用户没有填且URL不包含host，比如"/index.html?name=value"，如果Channel初始化的地址也不包含域名，则框架会以目标server的ip和port为Host，地址为10.46.188.39:8989的http server将会看到"Host: 10.46.188.39:8989"。 — [[sources/http_client|http_client]]
- 对应的字段在h2中叫":authority"。 — [[sources/http_client|http_client]]