---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std|baidu_std]]"]
tags: [product]
aliases:
  - "GNU zip"
  - "gzip压缩算法"
---


# gzip

## 基本信息
- Type: product
- Source: [[sources/baidu_std|baidu_std]]

## 描述
gzip 是一种广泛使用的数据压缩程序和算法，在 [[sources/baidu_std|baidu_std]] 协议中被列为可选的压缩算法之一。在 [[sources/baidu_std|baidu_std]] 协议的 RpcMeta 元数据中，通过 `compress_type` 字段指定具体的压缩算法，当该字段值为 2 时表示对包体中的数据部分使用 gzip 进行压缩。gzip 与 [[concepts/Snappy|Snappy]]（`compress_type` 值为 1）并列被 [[sources/baidu_std|baidu_std]] 协议支持，实现方可根据实际需求在[[concepts/压缩算法|压缩算法]]中选择合适的压缩方式以减少网络传输量。

## 相关实体
No related entities

## 相关概念
- [[concepts/压缩算法|压缩算法]]
- [[concepts/Snappy|Snappy]]

## 来源提及
- `2    | 使用gzip   |` — [[sources/baidu_std|baidu_std]]
- `compress_type       | 详见附录[压缩算法](#compress_algorithm)          |` — [[sources/baidu_std|baidu_std]]