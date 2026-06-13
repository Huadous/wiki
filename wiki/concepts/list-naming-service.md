---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/load_balancing]]"]
tags: [method]
aliases:
  - "list 命名服务"
  - "list://协议"
---


# list naming service

## 定义
list naming service 是 brpc 中以 `list://addr1,addr2,...` 协议形式提供的最简命名服务实现，地址列表直接内联在服务名字符串中（以逗号分隔）。由于列表内容在读取后不会再改变，该服务在调用一次 [[entities/namingservicethread|NamingServiceThread]] 内部的 `NamingServiceActions::ResetServers` 后即退出，不依赖任何周期性拉取或文件监听机制，是 brpc 中资源开销最低的命名服务实现方式。

## 关键特征
- 地址列表直接内联于服务名 URL 中，形如 `list://addr1,addr2,...`，无需额外的注册中心或配置文件
- 仅在首次读取时解析一次地址列表，调用 `NamingServiceActions::ResetServers` 后立即退出
- 不需要后台线程进行周期性拉取或基于 [[entities/filewatcher|FileWatcher]] 的文件变更监听
- 资源开销极低，是 brpc 命名服务体系中最轻量的实现
- 适用于地址完全固定、不会动态变化的场景（例如调试、本地测试或固定后端列表）

## 应用
- 本地开发与调试：直接通过 `list://` 协议指定若干已知后端，省去部署注册中心的成本
- 单元测试与集成测试：在测试用例中以字符串形式硬编码目标地址，便于复现
- 静态后端集群：当后端地址在运行时完全不变且数量有限时，作为最简配置方案使用
- 与 [[concepts/命名服务]] 体系中的其他实现（如基于 DNS、文件、远程注册中心的命名服务）形成对比，作为最小可用参考实现

## 相关概念
- [[concepts/命名服务]] — brpc 中服务发现与流量调度的统称，list naming service 是其中最简的实现

## 相关实体
- [[entities/namingservicethread]] — 承载命名服务读取与回调的主线程容器，list naming service 在其内部触发一次 `ResetServers` 后即结束
- [[entities/namingservicewatcher]] — 命名服务观察者接口，list naming service 通过其接收地址更新（仅有一次）
- [[entities/filewatcher]] — 文件监听机制，list naming service 不需要此机制即可工作

## 来源提及
- "list：列表就在服务名里（逗号分隔）。在读取完一次并调用NamingServiceActions::ResetServers后就退出了，因为列表再不会改变了。" — [[sources/load_balancing|load_balancing]]
- "list://addr1,addr2,...       # use the addresses separated by comma" — [[sources/load_balancing|load_balancing]]