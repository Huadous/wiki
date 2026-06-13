---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "Certificate Transparency"
  - "CT"
  - "证书透明度"
---


# Certificate Transparency

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Certificate Transparency(CT)是由Google主导的一个安全审计框架,旨在通过公开的、仅可追加的日志来记录所有TLS证书,从而检测错误签发或恶意颁发的证书。该项目已在Protocol Buffers官方扩展注册表中注册,扩展编号为1023,其代码托管在GitHub的google/certificate-transparency仓库中。

Certificate Transparency使用Protocol Buffers作为其日志结构、客户端与服务器之间通信的序列化格式。项目通过descriptor.proto扩展机制,为CT特有的自定义选项保留编号,以确保全局唯一性。Certificate Transparency已被主流浏览器(如Chrome)强制启用,成为公共TLS证书生态系统中不可或缺的关键安全基础设施。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protocolbuffersprotobuf|protobuf]]
- Protobuf Global Extension Registry

## 相关概念
- Extension numbers
- Custom options
- descriptor.proto

## 来源提及
- Certificate Transparency — [[sources/options|options]]
- Website: https://github.com/google/certificate-transparency — [[sources/options|options]]
- Extensions: 1023 — [[sources/options|options]]