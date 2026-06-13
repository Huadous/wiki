---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/json2pb]]"]
tags: [method]
aliases:
  - "repeated字段JSON编码规则"
  - "single_repeated_to_array"
  - "repeated to JSON Array mapping"
---


# repeated字段JSON编码

## 定义
repeated字段JSON编码定义了protobuf中`repeated`类型与JSON Array之间的映射规则，是json2pb实现JSON与protobuf双向转换时的核心编码方法之一。该方法在默认情况下将`repeated`字段序列化为花括号包围的JSON对象中的数组，同时对仅含一个`repeated`类型成员的message提供简化的数组直序列化选项。

## 关键特征
- **默认映射方式**：`repeated`字段序列化为花括号包围的JSON对象中的数组，例如`repeated int32 numbers = 1`对应`{"numbers" : [12, 17, 1, 24]}`。
- **对应rapidjson Array**：以方括号包围，元素会被递归地解析，与message不同的是，数组中每个元素的类型相同。
- **简化包体支持**：对于仅有一个`repeated`类型成员的message，json2pb支持直接序列化为数组（如`[12, 17, 1, 24]`），从而简化包体结构。
- **默认关闭**：单repeated成员直接序列化为数组的特性默认为关闭状态。
- **手动开启方式**：客户端在发送请求时或服务端在发送回复时，可通过`cntl.set_pb_single_repeated_to_array(true)`手动开启该特性。
- **使用示例**：
  ```cpp
  brpc::Controller cntl;
  cntl.set_pb_single_repeated_to_array(true);
  ```

## 应用
- **API请求/响应序列化**：在brpc服务中使用protobuf定义接口时，将`repeated`字段与JSON Array进行转换，方便HTTP等JSON协议客户端调用。
- **简化包体结构**：对于仅包含一个`repeated`字段的message（如简单列表类型），通过开启`single_repeated_to_array`特性可将外层的花括号省略，直接传输数组，减少包体大小和解析开销。
- **跨语言互操作**：确保使用JSON作为中间数据格式时，protobuf消息结构能被正确还原为`repeated`类型字段。

## 相关概念
- [[concepts/JSON-protobuf转换规则|JSON-protobuf转换规则]]
- [[concepts/JSON-map编码|JSON map编码]]

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/json2pb|json2pb]]
- [[entities/rapidjson|rapidjson]]
- [[entities/protocol-buffers|Protocol Buffers]]

## 来源提及
- "对应rapidjson Array, 以方括号包围，其中的元素会被递归地解析，和message不同，每个元素的类型相同。" — [[sources/json2pb|json2pb]]
- "特别的，针对仅有一个 `repeated` 类型成员的 `message`，序列化为 `json` 时支持直接序列化为数组，以简化包体。" — [[sources/json2pb|json2pb]]
- "brpc::Controller cntl;
cntl.set_pb_single_repeated_to_array(true);" — [[sources/json2pb|json2pb]]