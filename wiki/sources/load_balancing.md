---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/load_balancing.md]]"
tags: [命名服务, NamingService, NamingServiceActions, PeriodicNamingService, 负载均衡, LoadBalancer, 健康检查, DoublyBufferedData, bthread, BNS, DNS, file naming service, list naming service]
aliases: ["brpc Naming Service, Load Balancing and Health Check", "brpc 服务发现与流量调度"]
---

# brpc 命名服务、负载均衡与健康检查 - Summary

## 来源
- Original file: [[brpc/load_balancing.md]]
- Ingested: 2026-06-13

## 核心内容
本文档系统描述了 [[entities/brpc|brpc]] 框架中上游与下游节点之间的服务发现与流量调度机制，涵盖三大核心主题：[[concepts/命名服务|命名服务]]、[[concepts/负载均衡|负载均衡]] 和 [[concepts/健康检查|健康检查]]。命名服务采用反转控制模式，由用户通过 [[concepts/namingserviceactions|NamingServiceActions::ResetServers]] 主动将节点列表通知给框架，而非框架轮询用户函数，支持 bns、file、list 等多种实现方式。负载均衡通过 [[concepts/doublybuffereddata|DoublyBufferedData]] 技术实现多线程间无锁访问，[[concepts/loadbalancer|LoadBalancer]] 通过字符串工厂模式注册以便于扩展。健康检查针对被 SetFailed 的 [[entities/socket|Socket]] 动态创建独立的 [[concepts/bthread|bthread]] 周期性地尝试重连，成功后通过 Socket::Revive 复活节点。整个架构强调可扩展性、低延迟以及对故障节点的自动恢复能力。

## 关键实体
- [[entities/brpc|brpc]]：Apache 开源的高性能 RPC 框架，本文聚焦其命名服务、负载均衡和健康检查机制
- [[entities/namingservicewatcher|NamingServiceWatcher]]：感知命名服务列表变化的观察者接口
- [[entities/namingservicethread|NamingServiceThread]]：运行命名服务逻辑的独立 bthread 容器类，可被多个 Channel 共享
- [[entities/filewatcher|FileWatcher]]：基于 src/butil/files/file_watcher.h 的文件变更监听工具，被 file 协议命名服务利用
- [[entities/socket|Socket]]：brpc 中表示网络连接的核心类，在健康检查中提供 StartHealthCheck、SetFailed、Revive 等方法

## 关键概念
- [[concepts/命名服务|命名服务]]：将服务名映射到具体节点地址列表的机制，brpc 采用反转控制设计
- [[concepts/namingservice|NamingService]]：brpc 中获得服务名对应所有节点的接口
- [[concepts/namingserviceactions|NamingServiceActions]]：允许用户主动通知框架节点列表变更的反向调用接口
- [[concepts/periodicnamingservice|PeriodicNamingService]]：为没有事件通知能力的命名服务提供的辅助基类，默认 5 秒拉取一次
- [[concepts/负载均衡|负载均衡]]：将流量合理分配到多个下游节点的核心机制
- [[concepts/loadbalancer|LoadBalancer]]：从多个服务节点中选择一个节点的接口
- [[concepts/健康检查|健康检查]]：自动恢复失效节点的机制，通过独立 bthread 执行
- [[concepts/doublybuffereddata|DoublyBufferedData]]：通过双缓冲实现多线程无锁访问的数据结构技术
- [[concepts/bthread|bthread]]：brpc 框架中的协程/用户态线程抽象
- [[concepts/bns|BNS]]：Baidu Naming Service，brpc 支持的一种命名服务实现
- [[concepts/dns|DNS]]：Domain Naming Service，通过 http:// 协议形式暴露的命名服务
- [[concepts/file-naming-service|file naming service]]：以 file:// 协议形式提供的命名服务实现，通过 [[entities/filewatcher|FileWatcher]] 监听文件变更
- [[concepts/list-naming-service|list naming service]]：以 list:// 协议形式提供的最简命名服务实现

## 要点
- brpc 的命名服务采用反转控制设计：用户调用 [[concepts/namingserviceactions|NamingServiceActions::ResetServers]] 主动通知框架，而非框架轮询用户函数
- brpc 支持 bns://、file://、list://、http:// 等多种命名服务协议，通过 global.cpp 中的字符串工厂模式注册，扩展新协议简单
- 没有事件通知能力的命名服务（如 [[concepts/bns|BNS]]）可继承 [[concepts/periodicnamingservice|PeriodicNamingService]]，默认每 5 秒拉取一次节点列表
- [[concepts/loadbalancer|LoadBalancer]] 通过 [[concepts/doublybuffereddata|DoublyBufferedData]] 技术实现多线程间无锁的负载均衡选择，所有策略通过字符串注册
- 健康检查通过为每个 SetFailed 的 [[entities/socket|Socket]] 动态创建独立 [[concepts/bthread|bthread]] 执行，成功后调用 Socket::Revive 复活节点
- 命名服务是健康检查和负载均衡的前置条件：只有仍在 NamingService 中的节点才会被执行健康检查或被 LoadBalancer 选择
- file:// 命名服务通过 [[entities/filewatcher|FileWatcher]] 监听文件修改时间来触发 NamingServiceActions::ResetServers，避免不必要的轮询