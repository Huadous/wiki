---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_backup_request]]"]
tags: [project]
aliases:
  - "selective_echo_c++ 示例"
  - "SelectiveChannel 备份请求示例"
---


# example/selective_echo_c++

## 基本信息
- Type: project
- Source: [[sources/en_backup_request|en_backup_request]]

## 描述
example/selective_echo_c++ 是 [[entities/brpc|brpc]] 仓库中的一个 C++ 代码示例项目，用于演示当后端服务器无法挂载在同一个命名服务下时，如何使用 [[entities/SelectiveChannel|SelectiveChannel]] 实现两个子通道间的备份请求。该示例中 SelectiveChannel 包含两个子 Channel，先访问其中一个子 Channel，若在 [[entities/ChannelOptions|ChannelOptions]] 配置的 `backup_request_ms` 毫秒内未收到响应，则访问另一个子 Channel。若子 Channel 对应的是一个集群，该方法还可实现两个独立集群间的备份请求。该示例与 example/backup_request_c++ 形成对比，分别覆盖命名服务内和跨命名服务两种部署场景，为开发者提供在分布式环境下实现高可用请求模式的参考实现。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/SelectiveChannel|SelectiveChannel]]
- [[entities/ChannelOptions|ChannelOptions]]

## 相关概念
- [[concepts/backup-request|Backup Request]]
- [[concepts/backup_request_ms|backup_request_ms]]

## 来源提及
- "Define a SelectiveChannel that sets backup request, in which contains two sub channel." — [[sources/en_backup_request|en_backup_request]]
- "An example of SelectiveChannel can be found in example/selective_echo_c++. More details please refer to the above program." — [[sources/en_backup_request|en_backup_request]]