---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [term]
aliases:
  - "Protobuf结构查看"
  - "Protobuf结构体查看服务"
---


# /protobufs

## 定义
**/protobufs** 是 brpc 框架提供的一个内置 HTTP 服务端点（Endpoint），用于动态查看当前进程中所有已注册到 Protocol Buffers 描述池中的 Protobuf 消息类型、服务定义、枚举、文件描述符等元信息。它以一种人类可读的格式化页面（默认与浏览器兼容）展示完整的 Protobuf 结构体定义，使开发者能够在运行时实时检查和验证协议接口的结构与字段。

## 关键特征
- **动态元数据浏览**：无需查阅源代码或重新编译，即可通过浏览器直接获取当前服务所使用的全部 Protobuf 定义。
- **与 Protobuf 描述池集成**：服务直接基于 `DescriptorPool` 生成内容，确保信息与进程内存中的定义完全一致。
- **支持快速搜索**：页面内置搜索功能，方便开发者定位特定消息或字段。
- **接口兼容性辅助**：可用于对比不同服务版本间的消息结构差异，诊断序列化失败或不兼容问题。
- **安全敏感性**：由于该服务会暴露服务内部协议的全部定义细节，在生产环境或安全敏感场景下应通过防火墙、认证或配置关闭访问。

## 应用
- **接口兼容性诊断**：当服务升级后出现序列化异常或 RPC 调用失败时，通过 /protobufs 查看两端实际的 Protobuf 定义，快速定位字段变更或移除导致的兼容性问题。
- **开发调试**：在开发测试阶段，免去频繁查阅文档或 `.proto` 源文件的麻烦，直接在浏览器中验证消息结构与预期是否一致。
- **协议学习**：对刚接触的服务，使用 /protobufs 快速了解其通信协议的所有消息类型和 RPC 服务定义。

## 相关概念
- [[concepts/内置服务|内置服务]]
- [[concepts/protobuf-descriptor|protobuf-descriptor]]
- [[concepts/brpc内置服务|brpc内置服务]]
- [[concepts/序列化|序列化]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/protobuf-team|protobuf-team]]

## 来源提及
- "/protobufs: 查看程序中所有的protobuf结构体。" — [[sources/builtin_service|builtin_service]]