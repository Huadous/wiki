---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "other"
aliases:
  - "brpc AuthContext"
  - "身份认证上下文"
---

## Related Entities
- [[entities/authenticator|Authenticator]] — 服务器端认证接口，用于实现身份验证逻辑
- [[entities/controller|Controller]] — RPC 控制器对象，通过 `auth_context()` 方法获取认证上下文
- [[entities/brpc|brpc]] — 底层 RPC 框架，提供 AuthContext 的完整生命周期管理

## Related Concepts
- [[concepts/eovercrowded|eovercrowded]] — 过载错误码，与认证上下文的错误处理相关
- [[concepts/身份验证|身份验证]] — AuthContext 所服务的核心安全机制
- [[concepts/brpc-server-options|brpc::ServerOptions]] — 用于配置 `auth` 字段以启用 Authenticator 验证功能

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
- "class AuthContext { public: const std::string& user() const; const std::string& group() const; const std::string& roles() const; const std::string& starter() const; bool is_service() const; };" — [[sources/en_server|en_server]]
- "If the method returns 0, which indicates success, user can put verified information into `AuthContext` and access it via `controller->auth_context()` later, whose lifetime is managed by framework." — [[sources/en_server|en_server]]
- "Subsequent requests are treated as already verified without authenticating overhead." — [[sources/en_server|en_server]]

> **Source: [[sources/server|server]]**
- "用户可以把验证后的信息填入AuthContext" — [[sources/server|server]]
- "后续可通过controller->auth_context()获取，用户不需要关心其分配和释放。" — [[sources/server|server]]
- "class AuthContext { public: const std::string& user() const; const std::string& group() const; const std::string& roles() const; const std::string& starter() const; bool is_service() const; };" — [[sources/server|server]]
- "把实现的Authenticator实例赋值到ServerOptions.auth，即开启验证功能" — [[sources/server|server]]