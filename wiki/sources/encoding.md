---
---
type: source
created: 2026-06-12
updated: 2026-06-12
source_file: "[[protobuf/encoding.md]]"
tags: [Varint, Wire format, Tag-Length-Value (TLV), ZigZag encoding, Wire type, Length-delimited records, Submessages, Continuation bit, Field number, Packed repeated fields]
aliases: ["Protocol Buffers 编码文档", "Protobuf Wire Format 说明"]
---

# Encoding - Summary

## 来源
- Original file: [[protobuf/encoding.md]]
- Ingested: 2026-06-12

## 核心内容
本文档详细解释了Protocol Buffers的二进制编码格式（wire format），是理解Protobuf序列化底层原理的关键参考资料。文档从[[concepts/varint|varint]]变长编码入手，介绍了[[concepts/protocol-buffers-wire-types|协议缓冲区的六种线类型]]及其用途，并阐述了[[concepts/tag-length-value-tlv|Tag-Length-Value (TLV)]]记录结构——每个字段编码为包含字段编号和线类型的标签、可选长度前缀及实际数据。针对有符号整数，文档介绍了[[concepts/zigzag-encoding|ZigZag编码]]以优化负数空间占用。[[concepts/length-delimited-records|长度前缀记录(LEN)]]详解了字符串、字节、嵌套消息及packed字段的编码方式，[[concepts/submessage-encoding|子消息编码]]展示了消息嵌套的实现。[[concepts/non-varint-numeric-types-fixed-size|非变长数值类型]]（fixed64、double、fixed32、float）采用固定长度编码。同时介绍了[[concepts/packed-repeated-fields|packed重复字段]]默认启用后的紧凑编码优势。全文使用[[entities/protoscope|Protoscope]]工具提供直观的字节序列示例，所有示例基于Edition 2023或更新版本。

## 关键实体
- [[entities/protocol-buffers|Protocol Buffers]] — Google开发的序列化数据格式
- [[entities/protoscope|Protoscope]] — 用于可视化wire format的低级文本语言和工具

## 关键概念
- [[concepts/wire-format|Wire format]] — 二进制编码的核心框架
- [[concepts/varint|Varint]] — 变长整数编码方法
- [[concepts/tag-length-value-tlv|Tag-Length-Value (TLV)]] — 字段记录的基本结构
- [[concepts/zigzag-encoding|ZigZag encoding]] — 有符号整数优化编码
- [[concepts/protocol-buffers-wire-types|Protocol Buffers wire types]] — 六种线类型定义
- [[concepts/length-delimited-records|Length-delimited records]] — 动态长度编码方式
- [[concepts/submessage-encoding|Submessage encoding]] — 嵌套消息的编码规则
- [[concepts/packed-repeated-fields|Packed repeated fields]] — 连续存储的重复字段
- [[concepts/int32int64-signed-integers-twos-complement|int32/int64 signed integers (two's complement)]] — 二进制补码负数编码
- [[concepts/non-varint-numeric-types-fixed-size|Non-varint numeric types (fixed-size)]] — 固定长度数值类型

## 要点
- Varint编码使用延续位(continuation bit)机制，小数值占用更少字节，范围1-10字节
- 标签(tag)由字段编号左移3位后与线类型按位或得到，线类型低3位决定数据解析方式
- 消息采用TLV结构，解析器可跳过未知字段实现向前兼容
- sint32/sint64使用ZigZag编码减少负数占用，intN类型仍使用二进制补码
- LEN线类型用于字符串、字节、嵌套消息及packed repeated字段，带varint长度前缀
- 固定长度类型(I64/I32)如double、fixed64等编码后长度恒定
- 子消息编码与字符串编码结构相同，可嵌套任意层次
- Packed repeated字段将同类型所有值连续存储于一个LEN记录中，显著减小序列化大小