---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/load_balancing.md]]"]
tags: [term]
aliases:
  - "NamingServiceActions"
  - "brpc NamingServiceActions"
---


# NamingServiceActions

## 定义
NamingServiceActions 是 brpc 命名服务（NamingService）框架中的反向调用接口（callback interface）。它允许用户主动将获取到的节点列表通知给框架，而非由框架内部通过 PeriodicNamingService 周期性轮询来获取变更。该接口的核心方法是 `ResetServers`，接收新的服务器列表后，触发框架内部的去重、差异比较，并向已注册的 [[entities/namingservicewatcher|NamingServiceWatcher]] 观察者广播变更。

## 关键特征
- **反转控制（Inversion of Control）**：将节点列表获取的主动权交给用户侧，框架不再主动轮询，而是被动接收用户推送的更新。
- **核心方法 `ResetServers`**：接收新的服务器地址列表，触发后续的去重、差异比对与观察者通知流程。
- **事件驱动**：充分利用 ZooKeeper 这类支持 Watcher 事件通知的命名服务，避免传统轮询方式带来的数秒级延迟。
- **去重与差异比较**：框架在收到新列表后会自动进行去重处理，仅将发生变化的节点广播给 [[entities/namingservicewatcher|NamingServiceWatcher]]，减少不必要的回调开销。
- **线程模型**：ResetServers 的调用通常发生在 [[entities/namingservicethread|NamingServiceThread]] 中，框架负责将更新投递到正确的线程上下文。

## 应用
- **基于 ZooKeeper 的服务发现**：用户实现一个监听 ZooKeeper 节点变化的 Watcher，在节点变化时调用 `NamingServiceActions::ResetServers`，实现近实时的服务列表更新。
- **基于文件 / 配置中心的服务发现**：用户从本地文件、etcd、Consul 等来源读取节点列表后，调用 `ResetServers` 通知框架。读取一次并调用一次 `ResetServers` 后即可退出（列表不再变化时）。
- **低延迟服务发现场景**：在轮询周期（通常为几秒）无法满足实时性要求时，反向调用模式可将延迟降至事件通知的毫秒级。
- **自定义命名服务**：任何用户实现的 NamingService 都可持有 NamingServiceActions 句柄，在合适的时机将最新列表回推给框架。

## 相关概念
- [[concepts/命名服务|命名服务]]
- [[concepts/NamingService|NamingService]]
- [[concepts/PeriodicNamingService|PeriodicNamingService]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/namingservicewatcher|NamingServiceWatcher]]
- [[entities/namingservicethread|NamingServiceThread]]

## 来源提及
- "所以我们反转了控制权：不是我们调用用户函数，而是用户在获得列表后调用我们的接口，对应NamingServiceActions。" — [[sources/load_balancing|load_balancing]]
- "获取后调用NamingServiceActions::ResetServers告诉框架。" — [[sources/load_balancing|load_balancing]]
- "在读取完一次并调用NamingServiceActions::ResetServers后就退出了，因为列表再不会改变了。" — [[sources/load_balancing|load_balancing]]