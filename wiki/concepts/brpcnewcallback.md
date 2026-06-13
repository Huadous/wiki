---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_client]]"]
tags: [method]
aliases:
  - "NewCallback"
  - "brpc::NewCallback()"
---


# brpc::NewCallback

## 定义
`brpc::NewCallback` 是 brpc 框架提供的一个工具函数,定义于 `src/brpc/callback.h` 中。它用于创建一个 `google::protobuf::Closure` 对象,作为异步 RPC 调用完成时的 done 回调。`brpc::NewCallback` 是将自由函数(或成员方法)回调与其关联的响应对象与 Controller 对象绑定在一起的标准方式,这些对象在异步模式下通常采用堆分配。`brpc::NewCallback` 创建的回调对象会在 `Run()` 结束时自动 `delete` 自身。

## 关键特征
- **位置**:定义于 `src/brpc/callback.h`,由 brpc 直接提供。
- **返回类型**:返回一个 `google::protobuf::Closure*`,可直接作为异步 RPC 的 done 参数。
- **绑定参数**:可将任意可调用对象(自由函数或成员方法)与 response、Controller 等运行时对象绑定为一个 Closure。
- **自销毁语义**:回调对象在 `Run()` 结束时自动 `delete` 自身,无需调用方手动释放。
- **brpc 专属实现**:由于 Protobuf 3 将 `NewCallback` 设为 `private`,brpc 在 r32035 之后内置了自己的版本,并额外提供了更多重载;若用户的代码因 `NewCallback` 编译失败,可将 `google::protobuf::NewCallback` 替换为 `brpc::NewCallback`。

## 应用
- **异步 RPC 客户端回调**:在发起异步 RPC 时,通过 `brpc::NewCallback` 把处理函数、response 对象、Controller 对象组装成 done 闭包,在 RPC 完成时被框架回调。
- **回调与对象生命周期解耦**:适用于 response/Controller 各自单独 `new`,再由 `NewCallback` 装配为 done 的模式;也可将 response/Controller 设计为 done 的成员并与 done 一起 `new`,前者(brpc 文档推荐)更便于控制生命周期。
- **替换 `google::protobuf::NewCallback`**:当 Protobuf 3 之后 `google::protobuf::NewCallback` 不可见时,作为零迁移成本的替代方案,直接使用 `brpc::NewCallback` 即可使用相同的签名与重载。

## 相关概念
- [[concepts/asynchronous-call|Asynchronous call]]
- [[concepts/controller|Controller]]
- [[concepts/channel|Channel]]
- [[concepts/brpcjoin|brpc::Join]]

## 相关实体
- (暂无相关实体)

## 来源提及
- "You can new these objects individually and create done by NewCallback, or make response/controller be member of done and new them together. Former one is recommended." — [[sources/en_client]]
- "Since protobuf 3 changes NewCallback to private, brpc puts NewCallback in src/brpc/callback.h after r32035 (and adds more overloads). If your program has compilation issues with NewCallback, replace google::protobuf::NewCallback with brpc::NewCallback." — [[sources/en_client]]