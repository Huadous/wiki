---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/streaming_log|streaming_log]]"]
tags: [method]
aliases:
  - "流操作符重载"
  - "ostream operator overloading"
---


# operator<<重载

## 定义
operator<<重载是 C++ 中实现流式输出的关键技术，通过为自定义类型重载 `std::ostream& operator<<(std::ostream& os, const T& t)` 函数，使得对象可以被送入 `std::ostream` 进行打印。该函数返回 `os` 的引用以支持 chaining（链式调用），从而允许连续多次 `<<` 操作串联。streaming_log 正是利用这一机制，把日志内容像 DFS（深度优先遍历）一棵树一样逐层调用儿子节点的 operator<<，从而实现复杂对象的流式打印，且全程无需分配临时内存。这正是 streaming_log 相比 printf 形式日志在处理复杂对象时的核心优势。

## 关键特征
- **二元运算符重载**：通过重载左结合的二元运算符 `<<`，使自定义类型能够像内置类型一样被送入输出流。
- **返回流引用**：重载函数返回 `std::ostream&` 引用，使结果可以作为下一次 `<<` 操作的左侧操作数，从而支持链式串联。
- **组合等价性**：`os << a << b << c` 等价于 `operator<<(operator<<(operator<<(os, a), b), c)`，即嵌套调用。
- **无临时内存分配**：流式输出在打印过程中不依赖临时缓冲区，而是直接将内容写入目标流。
- **树形递归打印**：复杂对象可通过逐层调用子节点的 operator<<，以 DFS 的方式实现嵌套结构的流式输出。

## 应用
- **自定义类型的打印**：为用户自定义类重载 `operator<<`，使其实例能直接通过 `std::cout` 或日志流输出。
- **链式日志输出**：在日志库（如 streaming_log）中，通过重载 `operator<<` 把日志内容逐层嵌套打印，全程无临时内存分配。
- **复杂对象的格式化**：对于含有嵌套成员的对象，可借助 operator<< 重载实现类似 DFS 的递归打印，简化复杂数据结构的日志记录。
- **调试与诊断**：在调试程序时，利用 operator<< 将内部状态以流式方式输出到标准输出或日志文件，便于追踪对象状态。

## 相关概念
- [[concepts/chaining|chaining]]
- [[concepts/流式日志|流式日志]]

## 相关实体
- [[entities/butil|butil]]

## 来源提及
- "比如为了打印对象A，那么我们得实现如下的函数：std::ostream& operator<<(std::ostream& os, const A& a);" — [[sources/streaming_log|streaming_log]]
- "这个函数的意思是把对象a打印入os，并返回os。之所以返回os，是因为operator<<对应了二元操作 << （左结合），当我们写下os << a << b << c时，它相当于operator<<(operator<<(operator<<(os, a), b), c);" — [[sources/streaming_log|streaming_log]]