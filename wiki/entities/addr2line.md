---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_rpc]]"]
tags: [product]
aliases:
  - "GNU addr2line"
  - "地址行号转换工具"
---


# addr2line

## 基本信息
- Type: product
- Source: [[sources/streaming_rpc]]

## 描述
addr2line 是 GNU Binutils 工具集中的一个实用程序，用于将程序运行地址映射回源代码文件名和行号。在 brpc 的 [[concepts/streaming_log|streaming_log]] 调试流程中，当 [[concepts/CHECK宏|CHECK宏]] 断言失败时，会自动打印调用处的 call stack，其中第二列为代码地址。用户可以使用 addr2line 配合可执行文件查看每个地址对应的源码位置，例如运行 `$ addr2line -e ./test_base 0x000000a716b2` 即可输出对应的 .cc 源文件与行号。它是 streaming_log 调试流程中不可或缺的辅助工具，常与 [[entities/butil|butil]] 工具库配合使用以快速定位问题。

## 相关实体
- [[entities/butil]]

## 相关概念
- [[concepts/CHECK宏]]
- [[concepts/streaming_log]]

## 来源提及
- "callstack中的第二列是代码地址，你可以使用addr2line查看对应的文件行数：" — [[sources/streaming_rpc]]
- "$ addr2line -e ./test_base 0x000000a716b2 
/home/gejun/latest_baidu_rpc/public/common/test/test_streaming_log.cpp:223" — [[sources/streaming_rpc]]