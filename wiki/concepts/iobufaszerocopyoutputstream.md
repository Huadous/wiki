---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/iobuf|iobuf]]"]
tags: [term]
aliases:
  - "IOBuf 输出流适配器"
  - "IOBufAsZeroCopyOutputStream"
  - "ZeroCopyOutputStream wrapper"
---


# IOBufAsZeroCopyOutputStream

## 定义
IOBufAsZeroCopyOutputStream 是 butil 库中与 [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]] 对应的输出端适配器类，用于将 [[concepts/butil-iobuf|butil::IOBuf]] 适配为 Google Protobuf 的 ZeroCopyOutputStream 接口。它允许用户通过 protobuf 的 `SerializeToZeroCopyStream` 接口直接将序列化结果写入到 IOBuf 中，避免了先将 protobuf 消息序列化到临时缓冲区再拷贝进 IOBuf 的中间过程。

## 关键特征
- 作为 IOBuf 与 Protobuf ZeroCopyOutputStream 接口之间的桥接适配器
- 通过 `SerializeToZeroCopyStream` 直接将 protobuf 消息零拷贝地写入 IOBuf
- 与 [[concepts/iobufbuilder|IOBufBuilder]] 共同构成 IOBuf 的输出侧 API
- 适合结构化 protobuf 数据的输出场景，而 IOBufBuilder 更适合可打印数据的输出场景
- 避免了序列化中间缓冲区的额外内存拷贝开销

## 应用
- 通过 Protobuf 接口将序列化后的结构化数据高效地写入 IOBuf：

cpp
IOBufAsZeroCopyOutputStream wrapper(&iobuf);
pb_message.SerializeToZeroCopyStream(&wrapper);


- 在 brpc 框架中将 protobuf 序列化结果直接填充到网络 IOBuf 中，配合 [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]] 完成结构化数据的端到端传输
- 与 IOBufBuilder 互补，分别覆盖文本式与结构化两种主要的 IOBuf 输出场景

## 相关概念
- [[concepts/butil-iobuf|butil::IOBuf]]
- [[concepts/iobufbuilder|IOBufBuilder]]
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]
- [[concepts/iobuf-protobuf-interop|IOBuf 与 Protobuf 互操作]]
- [[concepts/zerocopyoutputstream|ZeroCopyOutputStream]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "protobuf序列化为IOBuf" — [[sources/iobuf|iobuf]]
- "IOBufAsZeroCopyOutputStream wrapper(&iobuf); pb_message.SerializeToZeroCopyStream(&wrapper);" — [[sources/iobuf|iobuf]]
- "用可打印数据创建IOBuf" — [[sources/iobuf|iobuf]]