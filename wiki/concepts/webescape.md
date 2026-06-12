---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [method]
aliases:
  - "brpc::WebEscape"
  - "URL转义函数"
  - "WebEscape安全函数"
---


# WebEscape

## 定义
WebEscape 是 Apache brpc 框架提供的一个安全函数，用于对 URL 进行转义（escaping），以防止注入攻击（injection attacks）。该函数通过将 URL 中的特殊字符转换为安全形式，确保用户可控的 URL 参数不会破坏请求结构或执行恶意操作。

## 关键特征
- **注入防护**：对 URL 中的特殊字符（如 `<`, `>`, `"`, `'`, `&` 等）进行转义，防止恶意构造的 URL 破坏语义或执行 XSS、SQL 注入等攻击。
- **函数式接口**：以 `brpc::WebEscape()` 形式提供简洁的调用方式，集成在 brpc 服务端框架中。
- **专注 URL 安全**：专门用于 URL 上下文的转义处理，不适用于其他数据格式（如 JSON、XML）的转义。
- **轻量高效**：作为核心内置函数，性能开销极低，适用于高并发 RPC 服务场景。

## 应用
- **公网服务防护**：当 brpc 服务直接暴露于公网或经过反向代理（如 Nginx、Envoy）时，对从公共网络传入的 URL 参数使用 `brpc::WebEscape()` 进行转义。
- **防御 XSS 攻击**：在输出 URL 到 HTML/JavaScript 上下文前进行转义，防止恶意脚本注入。
- **输入净化**：在处理用户提交的 URL 参数前，将转义后的安全字符串用于后续业务逻辑，减少注入风险。
- **与内置安全机制协同**：与 `[[concepts/内置服务安全|内置服务安全]]`（内部端口）、`[[entities/authcontext|AuthContext]]` 认证器以及 `[[concepts/SSL配置|SSL配置]]` 配合，构建多层纵深防御体系。
- **日志与监控**：对日志中记录的 URL 进行转义，防止因日志拼接导致的日志注入攻击。

## 相关概念
- [[concepts/内置服务安全|内置服务安全]]
- [[concepts/SSL配置|SSL配置]]
- [[concepts/认证机制|认证机制]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/nginx|nginx]]
- [[entities/envoy-proxy|envoy-proxy]]

## 来源提及
- "brpc::WebEscape() escapes url to prevent injection attacks with malice." — [[sources/en_server|en_server]]