---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/rdma]]"]
tags: [term]
aliases:
  - "Local Identifier"
  - "本地标识符"
---


# LID

## 定义
LID（Local Identifier，本地标识符）是InfiniBand网络中每个端口分配的16位局部标识符，用于子网内的路由和寻址，类似于二层MAC地址。在brpc的RDMA文档中，LID作为RDMA硬件概念被提及，与其他参数如device、port、GID、MaxSge并列。这些参数在初始化时会从网卡读取并作出默认选择，必要时用户可通过flag参数指定。

## 关键特征
- 16位局部标识符，取值范围为0x0001至0xBFFF（有效LID范围）
- 由子网管理器（Subnet Manager）在子网初始化时动态分配
- 仅在单个子网内有效，不同子网的LID可能重复
- 每个InfiniBand端口至少分配一个LID（主LID），可选分配多个（多路径）
- 与GID（全局标识符）不同，LID仅用于子网内部路由，GID用于跨子网通信

## 应用
- **子网内数据包路由**：InfiniBand交换机根据数据包中的LID目标地址进行转发
- **RDMA初始化**：在brpc等框架的RDMA初始化过程中，LID从网卡自动读取，作为建立QP（队列对）连接的必需参数
- **用户可配置**：当默认选择的LID不符合需求时，用户可通过flag参数手动指定

## 相关概念
- [[concepts/GID|GID]]
- [[concepts/握手|握手]]
- [[concepts/QP|QP]]

## 相关实体
无相关实体。

## 来源提及
- "RDMA是硬件相关的通信技术，有很多独特的概念，比如device、port、GID、LID、MaxSge等。" — [[sources/rdma|rdma]]
- "这些参数在初始化时会从对应的网卡中读取出来，并且做出默认的选择（参见src/brpc/rdma/rdma_helper.cpp）。" — [[sources/rdma|rdma]]