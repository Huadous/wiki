---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/en_streaming_log|en_streaming_log]]"]
tags: [method]
aliases:
  - "带虚拟路径的 VLOG"
  - "VLOG2 (verbose log with virtual path)"
---


# VLOG2

## 定义
VLOG2 是 [[concepts/VLOG|VLOG]] 的扩展形式，允许调用者在调用处显式指定一个"虚拟路径"（virtual path），而不是使用编译器隐式提供的 `__FILE__`。其签名形如 `VLOG2("a/b/c", 2)`，日志过滤时按指定的虚拟路径而非实际文件路径匹配 `--verbose_module`。VLOG2 同样有对应的条件版本 [[concepts/VLOG2_IF|VLOG2_IF]]（以及与 [[concepts/VLOG_IF|VLOG_IF]] 的关系见来源原文）。

## 关键特征
- **显式虚拟路径**：调用者直接传入字符串作为模块标识，绕过 `__FILE__` 展开。
- **独立于文件位置**：过滤匹配基于传入的虚拟路径，而非编译时的真实文件路径。
- **与 `--verbose_module` 协同**：gflags 形式指定的 verbose 模块名应与虚拟路径保持一致才能生效。
- **存在条件版本**：与 [[concepts/VLOG|VLOG]] / [[concepts/VLOG_IF|VLOG_IF]] 类似，提供 `VLOG2_IF` 用于附加条件判断。

## 应用
- **公共头文件**：头文件被多个 `.cc` 包含时，`__FILE__` 会随包含点变化，使用 VLOG2 可统一为单一逻辑模块名。
- **模板代码**：模板实例化分散在多个翻译单元，`__FILE__` 反映的是实例化位置而非模板自身，VLOG2 可指定逻辑模块名。
- **代码生成 / 多源文件合并**：生成代码或 unity build 把多文件合并时，`__FILE__` 失去语义，VLOG2 让开发者按逻辑模块而非物理文件开启 verbose 日志。

## 相关概念
- [[concepts/VLOG|VLOG]]
- [[concepts/VLOG_IF|VLOG_IF]]
- [[concepts/--verbose_module|--verbose_module]]

## 相关实体
- [[entities/streaming_log|streaming_log]]
- [[entities/gflags|gflags]]

## 来源提及
- "VLOG has another form VLOG2, which allows user to specify virtual path:" — [[sources/en_streaming_log|en_streaming_log]]
- `VLOG2("a/b/c", 2) << "being filtered by a/b/c rather than public/foo/bar";` — [[sources/en_streaming_log|en_streaming_log]]
- "> VLOG and VLOG2 also have corresponding VLOG_IF and VLOG2_IF." — [[sources/en_streaming_log|en_streaming_log]]