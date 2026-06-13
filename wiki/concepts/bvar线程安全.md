---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [term]
aliases:
  - "bvar thread safety"
  - "bvar线程兼容"
---


# bvar线程安全

## 定义
bvar 线程安全是对 bvar 库并发行为模式的明确定义：bvar 是**线程兼容**（thread-compatible）的，而非完全线程安全（thread-safe）。该定义描述了 bvar 在多线程环境下的使用边界——它并非对所有操作都保证并发安全，而是仅在特定场景下安全。

## 关键特征
- **线程兼容而非线程安全**：bvar 整体上属于线程兼容库，并不保证所有接口的并发调用都安全。
- **不同实例可并发操作**：用户可以在不同线程中操作**不同的** bvar，例如在多个线程中同时 expose 或 hide 不同的 bvar，它们对共享全局数据的操作经过合理设计，是安全的。
- **读写接口是线程安全的**：bvar 的读写操作（如 `<<` 运算符和 `get_value`）本身是线程安全的，可以在多个线程中并发调用。
- **非读写接口不是线程安全的**：除读写接口外，bvar 的其他函数（如 expose / hide）都是线程不安全的，不能在多个线程中同时操作同一个 bvar，否则很可能导致程序 crash。
- **gflag 直接覆盖线程不安全**：直接覆盖 `FLAGS_bvar_dump_file` / `FLAGS_bvar_dump_include` / `FLAGS_bvar_dump_exclude` 等 `std::string` 类型的 gflag 是线程不安全的。

## 应用
- **多线程监控指标采集**：在不同线程中各自操作不同的 bvar 实例（例如每个线程独立 expose 一个计数器），既满足监控需求，又避免竞争。
- **并发读写同一 bvar**：在多线程中并发地对同一 bvar 调用 `<<` 或 `get_value` 等读写接口，可以安全地进行数据写入与读取。
- **避免跨线程的非读写操作**：编写代码时必须确保对同一 bvar 的 expose、hide 等管理性操作只在单一线程中执行，否则会面临程序 crash 的风险。
- **dump 功能的并发控制**：对 `FLAGS_bvar_dump_*` 系列 gflag 的修改必须避免并发覆盖，通常采用专门的 setter 接口而非直接赋值。

## 相关概念
- [[concepts/expose|expose]]
- [[concepts/衍生变量|衍生变量]]
- [[concepts/合并运算符要求|合并运算符要求]]

## 相关实体
- [[entities/bvar|bvar]]
- [[entities/bvar::Variable|bvar::Variable]]

## 来源提及
- About thread-safety:
- bvar是线程兼容的。你可以在不同的线程里操作不同的bvar。比如你可以在多个线程中同时expose或hide**不同的**bvar，它们会合理地操作需要共享的全局数据，是安全的。 — [[sources/bvar_c++|bvar_c++]]
- **除了读写接口**，bvar的其他函数都是线程不安全的：比如说你不能在多个线程中同时expose或hide**同一个**bvar，这很可能会导致程序crash。一般来说，读写之外的其他接口也没有必要在多个线程中同时操作。 — [[sources/bvar_c++|bvar_c++]]
- 请勿直接设置FLAGS_bvar_dump_file / FLAGS_bvar_dump_include / FLAGS_bvar_dump_exclude。一方面这些gflag类型都是std::string，直接覆盖是线程不安全的； — [[sources/bvar_c++|bvar_c++]]