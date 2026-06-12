---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/encoding]]"]
tags: [term]
aliases:
  - "I64/I32 wire types"
  - "Fixed-width numeric types"
---


# 非变长数值类型（固定大小）

## 定义
非变长数值类型（fixed-size numeric types）是协议缓冲区编码中一组使用固定字节数编码的数据类型，包括 `double`、`fixed64`、`float` 和 `fixed32`。这些类型分别映射到 I64（8 字节）或 I32（4 字节）线类型，与变长数值类型（如 `int64`、`uint64`）形成直接对比。其核心特征是编码长度固定，不随数值大小变化，适合数值范围大且对编码效率要求高的场景。

## 关键特征
- **固定长度编码**：`double` 和 `fixed64` 使用 I64 线类型，占用 8 字节；`float` 和 `fixed32` 使用 I32 线类型，占用 4 字节。
- **IEEE 754 标准**：`double` 和 `float` 遵循 IEEE 754 浮点数标准进行编码。
- **简单固定长度整数**：`fixed64` 和 `fixed32` 直接以固定长度的小端字节序存储整数。
- **Protoscope 表示**：在 Protoscope 工具中，通过后缀 `i64`（表示 fixed64）或 `i32`（表示 fixed32）来标记这些类型；例如 `25.4` 表示 `double`，`200i32` 表示 `fixed32`。
- **与 varint 对比**：区别于变长数值类型（如 `int32`、`uint32`），非变长类型不依赖数值大小，始终使用固定空间，在小数值场景下空间效率较低，但在大数值场景下更可预测。

## 应用
- **协议缓冲区数据序列化**：在需要存储高精度浮点数（如科学计算、金融数据）时使用 `double` 或 `float`。
- **固定宽度索引或标识符**：`fixed32` 和 `fixed64` 适用于需要按固定大小索引的字段，例如数据库记录 ID 或哈希值。
- **性能敏感场景**：当解码性能优先时，固定长度字段可直接按字节偏移读取，避免 varint 的逐字节解析开销。
- **与外部系统交互**：需要与使用固定长度二进制格式的系统（如网络协议头、硬件设备）交换数据时，`fixed64` 和 `fixed32` 提供直接映射。

## 相关概念
- [[concepts/wire-format|Wire format]]
- [[concepts/varint|Varint]]
- [[concepts/tag-length-value-tlv|Tag-Length-Value (TLV)]]
- [[concepts/protocol-buffers-encoding|Protocol Buffers Encoding]]

## 相关实体
- [[entities/protoscope|Protoscope]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "Non-varint numeric types are simple. `double` and `fixed64` have wire type I64, which tells the parser to expect a fixed eight-byte lump of data." — [[protobuf/encoding|encoding]]
- "`double` values are encoded in IEEE 754 double-precision format. We can specify a double record by writing `5: 25.4`, or a `fixed64` record with `6: 200i64`." — [[protobuf/encoding|encoding]]