---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/streaming_log.md]]"]
tags: [method]
aliases:
  - "链式调用"
  - "stream chaining"
---


# chaining

## 定义
chaining 是 C++ 流式日志的核心技术，指通过连续调用 operator<< 来串联多个对象的打印操作。其原理是 operator<< 对应了二元操作 <<（左结合），当写下 `os << a << b << c` 时，它相当于 `operator<<(operator<<(operator<<(os, a), b), c)`。operator<< 必须不断返回 os 的引用，才能完成这一连串调用过程。streaming_log 在实现 operator<< 时也使用 chaining 模式：流式打印一个复杂对象就像 DFS 一棵树一样，逐层调用儿子节点的 operator<<。

## 关键特征
- 基于二元运算符 << 的左结合性实现连续调用
- operator<< 必须返回流对象（os）的引用以维持 chaining 链条不断裂
- 表达式 `os << a << b << c` 等价于嵌套调用 `operator<<(operator<<(operator<<(os, a), b), c)`
- 在不支持二元运算符重载的语言中，需用更繁琐的形式如 `os.print(a).print(b).print(c)` 实现类似效果
- 复杂对象的流式打印可类比为对一棵树的 DFS 遍历过程

## 应用
- C++ 流式日志打印：通过 chaining 模式实现多字段、多对象的连续输出
- streaming_log 中复杂对象的逐层递归打印：父节点调用 operator<<，子节点再调用孙子节点的 operator<<，层层展开
- brpc 中 butil 工具库的日志输出接口设计
- 任何需要连续多次输出操作的 C++ 场景

## 相关概念
- [[concepts/operator重载|operator<<重载]]
- [[concepts/流式日志|流式日志]]

## 相关实体
- [[entities/butil|butil]]

## 来源提及
- "这个过程一般称为chaining。在不支持重载二元运算符的语言中，你可能会看到一些更繁琐的形式，比如os.print(a).print(b).print(c)。" — [[brpc/streaming_log|streaming_log]]
- "我们在operator<<的实现中也使用chaining。事实上，流式打印一个复杂对象就像DFS一棵树一样：逐个调用儿子节点的operator<<，儿子又逐个调用孙子节点的operator<<，以此类推。" — [[brpc/streaming_log|streaming_log]]


I've created the concept page for "chaining" with the following key elements:

1. **Frontmatter**: Set type to "concept", tag to "method" (matching the requested type), and included aliases "链式调用" and "stream chaining" (derived from the provided extraction seeds)

2. **Definition**: Captures the core concept - the chaining technique in C++ streaming logs enabled by operator<< overloading and reference returns

3. **Key Characteristics**: Lists the technical properties (left-associativity, reference return requirement, equivalent nested call expansion, DFS-like traversal for complex objects, alternative forms in other languages)

4. **Applications**: Covers practical usage in streaming logs, butil/brpc, and complex object printing

5. **Related Concepts**: Used wiki-link format for "operator<<重载" and "流式日志" (these don't yet exist as pages but the lint system can detect them later)

6. **Related Entities**: Linked to [[entities/butil|butil]]

7. **Mentions in Source**: Preserved the verbatim Chinese quotes exactly as provided, with their source wiki-links