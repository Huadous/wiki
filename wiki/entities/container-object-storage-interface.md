---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/options|options]]"]
tags: [project]
aliases:
  - "COSI"
  - "Container Object Storage Interface (COSI)"
  - "Kubernetes COSI"
---


# Container Object Storage Interface

## 基本信息
- Type: project
- Source: [[sources/options|options]]

## 描述
Container Object Storage Interface(COSI)是[[entities/protocolbuffersprotobuf|Protocol Buffers]]生态中由Kubernetes SIG(具体为kubernetes-sigs)提出的对象存储供应标准,规范托管在GitHub的kubernetes-sigs/container-object-storage-interface-spec仓库中。COSI是[[entities/container-storage-interface|Container Storage Interface (CSI)]]的姊妹规范,专门针对S3兼容的对象存储桶的动态供给、访问策略管理与生命周期配置而设计,弥补了CSI不直接支持对象存储桶的不足。该规范使用Protocol Buffers定义其桶声明(BucketClaim)、访问授权(BucketAccess)与桶类(BucketClass)等核心API,并通过[[concepts/descriptor-proto|descriptor.proto]]扩展为COSI特有的对象存储属性保留较大范围的扩展编号(1115-1124),从而在Protobuf全局扩展注册表中占据一组连续的标识位。COSI作为CSI的延伸,与Protobuf编码体系协同工作,使Kubernetes环境下的对象存储供给具备与块存储一致的声明式供给能力。

## 相关实体
- [[entities/protocolbuffersprotobuf|Protocol Buffers]]
- [[entities/protobuf-global-extension-registry|Protobuf Global Extension Registry]]
- [[entities/container-storage-interface|Container Storage Interface]]

## 相关概念
- [[concepts/extension-numbers|Extension numbers]]
- [[concepts/custom-options|Custom options]]
- [[concepts/descriptor-proto|descriptor.proto]]

## 来源提及
- "Container Object Storage Interface (COSI)" — [[sources/options|options]]
- "Website: https://github.com/kubernetes-sigs/container-object-storage-interface-spec" — [[sources/options|options]]
- "Extension: 1115-1124" — [[sources/options|options]]