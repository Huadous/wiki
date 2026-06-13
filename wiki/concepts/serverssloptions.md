---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/server|brpc Server端使用文档]]"]
tags: [term]
aliases:
  - "ServerSSLOptions"
  - "brpc Server SSL Options"
  - "SSL options"
---


# ServerSSLOptions

## 定义
ServerSSLOptions 是 brpc 框架中 Server 端的 SSL/TLS 配置结构体，定义在 `ssl_options.h` 头文件中。通过 `brpc::ServerOptions.ssl_options` 字段开启 SSL 功能。它用于配置 Server 端的证书、SNI（Server Name Indication）行为以及 SSL 握手策略。

## 关键特征
- **默认证书**：Server 端开启 SSL 必须设置一张默认证书 `default_cert`，所有未匹配到特定 SNI 的 SSL 连接默认使用此证书。
- **多证书与 SNI**：可通过 `certs` 字段配置多张证书，以实现基于 SNI（Server Name Indication）的域名选择与证书分发。
- **strict_sni 控制**：当客户端请求的 SNI 找不到匹配证书时，`strict_sni` 决定是否拒绝请求。
- **动态证书管理**：运行时可通过 `AddCertificate` / `RemoveCertificate` / `ResetCertificates` 等接口动态添加、删除或重置证书。
- **SSL 层位置**：SSL 层位于协议层之下（作用在 Socket 层）。开启后，所有协议（如 HTTP）都支持用 SSL 加密后传输到 Server，Server 端会先进行 SSL 解密，再将原始数据递交给各个协议处理。
- **非 SSL 连接兼容**：SSL 开启后，端口仍然支持非 SSL 的连接访问，Server 会自动判断哪些连接是 SSL，哪些不是。

## 应用
- 为 brpc Server 端启用 HTTPS、TLS 等加密传输能力。
- 在同一端口下同时提供加密与非加密服务。
- 通过 SNI 在单个 Server 实例上为多个域名提供不同的证书。
- 运行时动态轮换或更新证书（例如证书即将过期时热替换），无需重启服务。
- 在对安全性要求较高的 RPC 通信场景中，配合 brpc 的各种协议（HTTP、HTTP/2、Protobuf over TCP 等）实现端到端加密。

## 相关概念
- [[concepts/SSL|SSL]]
- [[concepts/brpc-server|brpc::Server]]
- [[concepts/brpc-serveroptions|brpc::ServerOptions]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "设置ServerOptions.ssl_options，具体见ssl_options.h。" — [[sources/server|brpc Server端使用文档]]
- "Server端开启SSL必须要设置一张默认证书default_cert（默认SSL连接都用此证书）" — [[sources/server|brpc Server端使用文档]]
- "SSL层在协议层之下（作用在Socket层），即开启后，所有协议（如HTTP）都支持用SSL加密后传输到Server，Server端会先进行SSL解密后，再把原始数据送到各个协议中去。" — [[sources/server|brpc Server端使用文档]]
- "SSL开启后，端口仍然支持非SSL的连接访问，Server会自动判断哪些是SSL，哪些不是。" — [[sources/server|brpc Server端使用文档]]