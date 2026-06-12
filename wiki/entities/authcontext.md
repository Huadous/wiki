---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
tags:
  - "other"
aliases:
  - "brpc AuthContext"
  - "身份认证上下文"
---

## Description
AuthContext 是 brpc 框架中用于存储客户端身份验证结果的上下文类。当服务器端实现 [[entities/authenticator|Authenticator]] 接口时，开发者可以在 `VerifyCredential` 方法中通过 AuthContext 填充用户的认证信息，包括用户名、用户组、角色等身份属性。认证完成后，控制器对象（[[entities/controller|Controller]]）可以通过 `controller->auth_context()` 方法获取该对象，其生命周期由 brpc 框架自动管理，无需手动释放。AuthContext 提供了多个方法用于获取不同维度的身份信息：`user()` 返回用户名，`group()` 返回用户组，`roles()` 返回角色集合，`starter()` 返回启动者信息，`is_service()` 判断是否为服务账户。该类是 brpc 服务端身份认证机制的核心组件，为微服务架构中的访问控制和权限管理提供了基础支持。认证过程仅在首次请求时触发，后续来自同一客户端的请求自动被视为已验证，无需重复执行认证逻辑，从而降低认证开销。

## Related Entities
- [[entities/authenticator|Authenticator]] — 服务器端认证接口，用于实现身份验证逻辑
- [[entities/controller|Controller]] — RPC 控制器对象，通过 `auth_context()` 方法获取认证上下文
- [[entities/brpc|brpc]] — 底层 RPC 框架，提供 AuthContext 的完整生命周期管理

## Related Concepts
- [[concepts/eovercrowded|eovercrowded]] — 过载错误码，与认证上下文的错误处理相关

## Mentions in Source
> **Source: [[sources/en_server|en_server]]**
- "class AuthContext { public: const std::string& user() const; const std::string& group() const; const std::string& roles() const; const std::string& starter() const; bool is_service() const; };" — [[sources/en_server|en_server]]
- "If the method returns 0, which indicates success, user can put verified information into `AuthContext` and access it via `controller->auth_context()` later, whose lifetime is managed by framework." — [[sources/en_server|en_server]]
- "Subsequent requests are treated as already verified without authenticating overhead." — [[sources/en_server|en_server]]