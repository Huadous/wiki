---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources:
  - "[[sources/streaming_log|streaming_log]]"
  - "[[brpc/en_streaming_log.md]]"
tags:
  - "method"
aliases:
  - "流操作符重载"
  - "ostream operator overloading"
  - "std::ostream chaining"
  - "流操作符重载"
  - "ostream operator overloading"
---

## Description
operator<<重载是 C++ 标准库为流式输出提供的运算符重载机制，其本质是对左结合的二元运算符 `<<` 进行扩展，使自定义类型能够像内置类型一样被送入 `std::ostream`。当写下 `os << a << b << c` 时，编译器会将其展开为 `operator<<(operator<<(operator<<(os, a), b), c)` 的嵌套调用，因此每个重载函数必须返回 `std::ostream&` 引用以使下一次 `<<` 操作得以继续，这一机制在 en_streaming_log 中也被称为 chaining。streaming_log 正是利用这一特性，把日志内容像 DFS 遍历一棵树一样逐层调用儿子节点的 operator<<，从而实现复杂对象的流式打印，且全程无需分配临时内存——对于含有嵌套成员的对象 A，其 operator<< 通常以 `os << "A{b=" << a.b << ", c=" << a.c << "}"` 的形式递归打印各字段。这一机制是 streaming_log 相比 printf 形式日志在处理复杂对象时的核心优势，也是其日志流继承自 `std::ostream` 的设计基础。

## Related Concepts
- [[concepts/chaining|chaining]]
- [[concepts/流式日志|流式日志]]
- [[concepts/log宏|LOG 宏]]

## Related Entities
- [[entities/butil|butil]]
- [[entities/streaming_log|streaming_log]]

## Mentions in Source
> **Source: [[sources/streaming_log|streaming_log]]**
> - "比如为了打印对象A，那么我们得实现如下的函数：std::ostream& operator<<(std::ostream& os, const A& a);"
> - "这个函数的意思是把对象a打印入os，并返回os。之所以返回os，是因为operator<<对应了二元操作 << （左结合），当我们写下os << a << b << c时，它相当于operator<<(operator<<(operator<<(os, a), b), c);"

> **Source: [[sources/en_streaming_log|en_streaming_log]]**
> - "The solution in C++ is to send the log as a stream to the std::ostream object."
> - "The signature of the function means to print object a to os and then return os."
> - "Apparently operator<< needs a returning reference to complete this process, which is also called chaining."