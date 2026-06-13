---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_server]]"]
tags: [term]
aliases:
  - "服务所有权"
  - "服务生命周期管理"
  - "ServiceOwnership"
---


# ServiceOwnership

## 定义
ServiceOwnership 是 `brpc::Server` 中用于控制服务对象生命周期的枚举值。当调用 `AddService` 方法向服务器注册服务时，通过 `ownership` 参数指定服务器是否拥有该服务对象的所有权，从而决定服务对象的销毁时机和内存管理责任。

## 关键特征
- **严格二值枚举**：仅包含两个值 —— `SERVER_OWNS_SERVICE` 和 `SERVER_DOESNT_OWN_SERVICE`
- **生命周期控制**：`SERVER_OWNS_SERVICE` 表示服务器在销毁时会自动 `delete` 服务对象；`SERVER_DOESNT_OWN_SERVICE` 表示服务器不管理服务生命周期
- **默认行为差异**：默认所有权取决于 `AddService` 的重载版本，但通常推荐显式指定
- **与 ServiceOptions 协同**：可通过 `ServiceOptions` 结构体中的 `ownership` 字段显式设置
- **内存安全管理**：直接影响服务对象的析构时机，避免悬空指针或内存泄漏

## 应用
- **短生命周期服务**：当服务对象仅在服务器运行期间使用时，使用 `SERVER_OWNS_SERVICE` 简化内存管理
- **持久化服务对象**：当服务对象需要被多个服务器共享或跨越服务器生命周期存在时，使用 `SERVER_DOESNT_OWN_SERVICE`
- **栈上对象注册**：如果服务对象分配在栈上（如局部变量），必须使用 `SERVER_DOESNT_OWN_SERVICE`，防止服务器在析构时对栈内存执行 `delete`
- **依赖注入场景**：当服务需要接收外部配置或依赖时，通常在外部创建对象后以 `SERVER_DOESNT_OWN_SERVICE` 注册

## 相关概念
- [[concepts/协议自动检测|协议自动检测]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/serviceoptions|serviceoptions]]
- [[entities/echoservice|echoservice]]
- [[entities/myechoservice|myechoservice]]

## 来源提及
- "If ownership is SERVER_OWNS_SERVICE, server deletes the service at destruction." — [[sources/en_server|brpc 服务端教程]]
- "To prevent the deletion, set ownership to SERVER_DOESNT_OWN_SERVICE." — [[sources/en_server|brpc 服务端教程]]
- "Following code adds MyEchoService: server.AddService(&my_echo_service, brpc::SERVER_DOESNT_OWN_SERVICE);" — [[sources/en_server|brpc 服务端教程]]