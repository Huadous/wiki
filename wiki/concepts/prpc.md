---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std]]"]
tags: [term]
aliases:
  - "baidu_std 协议标识符"
  - "baidu_std Protocol Identifier"
---


# PRPC

## 定义
PRPC 是 baidu_std 协议的协议标识符，占据 baidu_std 数据包包头的前 4 字节。它用于在数据流中标识这是一个 baidu_std 协议的包，以便接收端能够正确解析后续的包体内容。

## 关键特征
- 固定长度为 4 字节，位于 baidu_std 包头的起始位置
- 是 baidu_std 协议的魔数（magic number），用于协议识别与数据流分帧
- 与包头中其余两个 32 位整数（包体长度和元数据长度）共同构成 12 字节的固定长度包头
- 包头中所有整数均采用网络字节序（大端序）表示，确保跨平台传输的一致性

## 应用
- 在基于 baidu_std 协议的 RPC 通信中，接收端首先读取前 4 字节的 PRPC 标识来验证协议类型
- 用于网络数据流中 baidu_std 包的边界识别与解析起始点
- 作为 baidu_std 协议与其他传输协议区分的关键标志

## 相关概念
- [[concepts/包头]]
- [[concepts/元数据]]

## 相关实体
- [[entities/baidu_std]]

## 来源提及
- 包头长度固定为12字节。前四字节为协议标识PRPC，中间四字节是一个32位整数，表示包体长度（不包括包头的12字节），最后四字节是一个32位整数，表示包体中的元数据包长度。整数均采用网络字节序表示。 — [[sources/baidu_std|baidu_std]]