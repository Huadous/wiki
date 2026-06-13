---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/features]]"]
tags: [term]
aliases:
  - "export 语句"
  - "ES模块导出"
---

# export 关键字

## 定义
`export` 关键字是 JavaScript 模块系统（ES Modules）中的核心语法，用于将模块内部的函数、变量、类或接口对外暴露，使其可以被其他模块通过 `import` 关键字导入并使用。它定义了模块的公共接口，是实现代码封装与模块化开发的基础。

## 关键特征
- **导出方式灵活**：支持命名导出（named export）和默认导出（default export）两种形式
- **模块作用域隔离**：只有被 `export` 标记的内容才对模块外部可见，其余内容保持私有
- **静态解析**：`export` 语句在编译阶段即可被解析，支持 tree-shaking 优化
- **重命名支持**：可通过 `as` 关键字为导出的标识符指定别名
- **聚合导出**：支持 `export * from` 或 `export { ... } from` 语法，重新导出其他模块的内容

## 应用
- **库与框架开发**：如 [[entities/brpc|brpc]] 的 Node.js 客户端模块使用 `export` 定义对外 API
- **工具函数封装**：在 [[entities/node-js|Node.js]] 项目中通过 `export` 暴露常用工具函数集
- **组件化开发**：现代前端框架（如 React、Vue）通过 `export` 定义可复用的 UI 组件
- **模块分割与懒加载**：结合动态 `import()` 实现按需加载，优化 [[entities/github|GitHub]] 等大型应用的性能

## 相关概念
- [[concepts/模块化开发|模块化开发]]：`export` 是实现模块化的核心语法之一，与 `import` 共同构成模块系统
- [[concepts/ES Modules|ES Modules]]：`export` 是 ES Modules 标准的关键组成部分
- [[concepts/tree-shaking|tree-shaking]]：`export` 的静态特性使构建工具能移除未使用的导出代码

## 相关实体
- [[entities/node-js|Node.js]]：作为 JavaScript 运行时环境，Node.js 从 v12 开始稳定支持 ES Modules 的 `export` 语法
- [[entities/protocol-buffers|Protocol Buffers]]：`export` 常用于将 protobuf 生成的 JavaScript 类暴露给模块消费者

## 来源提及
*(No source content available for this page)*