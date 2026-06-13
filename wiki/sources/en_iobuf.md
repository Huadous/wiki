---
type: source
created: 2026-06-13
updated: 2026-06-13
source_file: "[[brpc/en_iobuf.md]]"
tags: [IOBuf, Zero-copy buffer, Reference counting, IOBufBuilder, BufHandle, Protocol Buffers, IOBufAsZeroCopyInputStream, IOBufAsZeroCopyOutputStream, CodedInputStream]
aliases: ["brpc IOBuf 使用文档", "brpc IOBuf Documentation"]
---

# brpc IOBuf 使用文档 - 摘要

## 来源
- Original file: [[brpc/en_iobuf.md]]
- 摄入日期: 2026-06-13

## 核心内容
本文档详细介绍了 [[entities/brpc|brpc]] 框架中使用的 [[concepts/iobuf|butil::IOBuf]] 数据结构。[[concepts/iobuf|IOBuf]] 是一种经过先前项目验证的[[concepts/zero-copy-buffer|非连续零拷贝缓冲区]],在 [[entities/brpc|brpc]] 的部分协议和 HTTP body 中作为附件数据结构使用,接口与 std::string 类似但不完全相同。文档阐述了 IOBuf 的能力边界,包括默认构造不分配内存、零拷贝复制和追加、与字符串互转、支持文件描述符读写、与 protobuf 消息互转以及通过 [[concepts/iobufbuilder|IOBufBuilder]] 构造。同时指出其限制:生命周期应较短,避免引用计数的 8K 内存块占用过多内存。文档通过代码示例展示了典型操作,并提供了性能基准测试数据。

## 关键实体
- [[entities/brpc|brpc]] — Apache 开源的高性能 RPC 框架,IOBuf 的主要使用方
- [[entities/butil|butil]] — brpc 的实用工具库,IOBuf 类定义于其 iobuf.h 中
- [[entities/apache|Apache]] — 托管 brpc 项目的开源软件基金会
- [[entities/kylin|Kylin]] — 早期项目,其中的 BufHandle 被用作 IOBuf 的对比参照

## 关键概念
- [[concepts/iobuf|IOBuf]] — 核心数据结构,非连续零拷贝缓冲区
- [[concepts/zero-copy-buffer|零拷贝缓冲区]] — IOBuf 的核心技术特性
- [[concepts/reference-counting|引用计数]] — IOBuf 内部 8K 内存块的管理机制
- [[concepts/iobufbuilder|IOBufBuilder]] — 流式构建 IOBuf 的辅助类
- [[concepts/bufhandle|BufHandle]] — Kylin 中的数据结构,封装不佳的对比案例
- [[concepts/protocol-buffers|Protocol Buffers]] — IOBuf 支持互转的序列化协议
- [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]] — 将 IOBuf 适配为 protobuf 零拷贝输入流的包装类
- [[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]] — 将 IOBuf 适配为 protobuf 零拷贝输出流的包装类
- [[concepts/codedinputstream|CodedInputStream]] — protobuf 中配合 IOBuf 用于自定义格式解析的读取工具

## 要点
- [[concepts/iobuf|IOBuf]] 是 brpc 中用于协议附件和 HTTP body 的非连续零拷贝缓冲区,接口类似 std::string 但不完全相同
- 核心优势在于[[concepts/zero-copy-buffer|零拷贝]]和[[concepts/reference-counting|引用计数]]:复制仅复制管理结构、追加其他 IOBuf 无需拷贝载荷,但生命周期应保持短暂以避免 8K 内存块占用过多
- 支持 Cut/Append 切片操作、与 [[concepts/protocol-buffers|protobuf]] 消息互转(通过 [[concepts/iobufaszerocopyinputstream|IOBufAsZeroCopyInputStream]]/[[concepts/iobufaszerocopyoutputstream|IOBufAsZeroCopyOutputStream]])、文件描述符读写、通过 [[concepts/iobufbuilder|IOBufBuilder]] 流式构建
- 相比 [[entities/kylin|Kylin]] 的 [[concepts/bufhandle|BufHandle]],[[concepts/iobuf|IOBuf]] 封装更好,不暴露内部引用计数给用户,降低了使用复杂度
- 性能基准测试显示,[[concepts/iobuf|IOBuf]] 在不同数据大小下可达 240MB/s 至 1519MB/s 的吞吐量,QPS 从 858 万到 146 万不等