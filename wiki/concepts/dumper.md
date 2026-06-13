---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/bvar_c++|bvar_c++]]"]
tags: [other]
aliases:
  - "bvar::Dumper"
  - "Dumper 基类"
  - "bvar Dumper"
---


# Dumper

## 定义
Dumper 是 brpc 中 bvar 导出机制里用于**用户自定义导出行为**的抽象基类。用户通过继承 Dumper 并实现其纯虚函数 `dump(const std::string& name, const butil::StringPiece& description)`，即可将进程内已曝光的 bvar 数据导出到任意目的地（如文件、HTTP 端点、第三方监控系统等），而不仅限于 `bvar_dump_file` 所指定的本地文件。当 `dump()` 返回 `false` 时，`Variable::dump_exposed()` 将**停止遍历并返回 -1**。

## 关键特征
- **抽象基类**：定义了一个纯虚函数 `dump(const std::string& name, const butil::StringPiece& description) = 0;`，强制派生类提供具体导出实现。
- **作为回调点**：在 `Variable::dump_exposed()` 遍历已曝光 bvar 的过程中，Dumper 实例被逐个变量调用，从而决定每个变量的导出方式。
- **短路机制**：`dump()` 返回 `false` 即触发遍历终止，使外层 `dump_exposed()` 立即返回 `-1`，提供一种"中止导出"的控制手段。
- **与 DumpOptions 协作**：常配合 `DumpOptions` 中的 `white_wildcards`（白名单通配符）与 `black_wildcards`（黑名单通配符）使用，过滤需要导出的变量集合。
- **导出目的地无关**：不绑定任何具体输出介质，因此可灵活对接文件、HTTP、第三方 metrics 系统等。

## 应用
- **自定义导出到文件**：在无需使用默认 `bvar_dump_file` 的场景下，继承 Dumper 实现自有文件输出格式。
- **HTTP 端点暴露**：通过实现 Dumper 将 bvar 数据实时推送到远程 HTTP 服务，以便集中监控或聚合。
- **对接第三方监控系统**：将 bvar 数据导出到 Prometheus、Grafana、自研 metrics 平台等。
- **按需过滤导出**：结合 `DumpOptions.white_wildcards` 与 `black_wildcards`，仅导出符合白名单或未被黑名单过滤的变量。
- **中止导出流程**：在特定条件下（例如检测到异常或收到停止信号）让 `dump()` 返回 `false`，立即终止整次导出动作。

## 相关概念
- [[concepts/bvar导出|bvar导出]]
- [[concepts/DumpOptions|DumpOptions]]
- [[concepts/expose|expose]]

## 相关实体
- [[entities/bvar::Variable|bvar::Variable]]

## 来源提及
- // Implement this class to write variables into different places.
  // If dump() returns false, Variable::dump_exposed() stops and returns -1.
  class Dumper {
  public:
      virtual bool dump(const std::string& name, const butil::StringPiece& description) = 0;
  }; — [[sources/bvar_c++|bvar_c++]]
- 用户也可以使用dump_exposed函数自定义如何导出进程中的所有已曝光的bvar： — [[sources/bvar_c++|bvar_c++]]