---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "trackme-server"
  - "brpc trackme server"
---


# trackme_server

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述

trackme_server是[[entities/brpc|brpc]]框架提供的一个监控与跟踪工具程序，专为管理分布式brpc集群而设计。用户只需在集群中的某个位置启动trackme_server，并在需要被跟踪的brpc实例中指定`-trackme_server=SERVER`启动参数，该工具便会自动开始工作。trackme_server会定期接收来自各个brpc实例的心跳信号（ping），并在接收到心跳时记录日志。运维人员可以通过汇总日志中记录的实例网络地址，进一步调用各实例的内置服务来获取更详细的运行状态信息。该工具对于大规模分布式brpc集群的运维和问题排查非常有价值。

## 相关实体

- [[entities/brpc|brpc]] — trackme_server所跟踪和监控的RPC框架
- [[entities/config_brpc-sh|config_brpc.sh]] — brpc配置脚本，可能用于设置trackme_server参数

## 相关概念

（暂无）

## 来源提及

- "We provide a program to help you to track and monitor all brpc instances." — [[sources/en_getting_started|en_getting_started]]
- "Just run trackme_server somewhere and launch need-to-be-tracked instances with -trackme_server=SERVER." — [[sources/en_getting_started|en_getting_started]]
- "The trackme_server will receive pings from instances periodically and print logs when it does." — [[sources/en_getting_started|en_getting_started]]