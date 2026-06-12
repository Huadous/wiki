---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/builtin_service]]"]
tags: [term]
aliases:
  - "vars服务"
  - "自定义计数器"
  - "brpc变量展示接口"
---


# /vars

## 定义
/vars是brpc内置服务中的一个HTTP端点，用于暴露和展示用户可定制的计数器。它允许开发者根据应用需求自定义需要监控的变量，以键值对形式呈现各种内部度量指标（如请求数、延迟分布、错误率等），为性能调优和异常检测提供实时数据支持。

## 关键特征
- **可定制性**：用户可以根据业务需要自由注册和暴露自定义计数器，不限于系统内置指标。
- **实时性**：通过HTTP GET访问/vars，可获取服务当前时刻的瞬时度量值。
- **自动格式化**：返回数据的格式会根据请求的User-Agent头自动调整（如纯文本、JSON等），便于不同客户端解析。
- **体系化集成**：与/status、/connections等内置服务共同构成brpc完整的状态查看体系。
- **低开销**：计数器更新操作轻量，不会对服务性能产生明显影响。

## 应用
- **实时监控**：运维人员通过/vars接口采集服务的瞬时状态，如当前QPS、活跃连接数、错误计数等。
- **性能分析**：观察延迟分布百分位（P99、P999）、RPC耗时等指标，定位性能瓶颈。
- **异常检测**：监控错误率、超时次数等指标，配合告警系统及时发现服务异常。
- **容量规划**：收集长期指标数据，分析服务负载趋势，为资源扩容提供依据。

## 相关概念
- [[concepts/status|/status]]
- [[concepts/connections|/connections]]
- [[concepts/flags|/flags]]
- [[concepts/rpcz|/rpcz]]
- [[concepts/builtin-service|内置服务]]

## 相关实体
- [[entities/brpc|brpc]]

## 来源提及
- "/vars: 用户可定制的，描绘各种指标的计数器。" — [[sources/builtin_service|builtin_service]]