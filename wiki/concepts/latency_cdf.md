---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/backup_request]]"]
tags: [method]
aliases:
  - "延迟CDF图"
  - "累积分布函数延迟图"
  - "Latency CDF Graph"
---


# latency_cdf

## 定义
latency_cdf是brpc框架默认提供的延迟累积分布函数图，用于直观展示服务请求延迟的分布情况。该图以可视化方式展示不同延迟阈值所覆盖的请求比例，帮助开发者合理配置`backup_request_ms`参数。图中y轴表示延迟（默认单位为微秒），x轴表示延迟小于y轴值的请求所占的累积比例。

## 关键特征
- **累积分布可视化**：展示延迟的累积分布函数，横轴为请求比例（0~100%），纵轴为延迟值
- **默认集成**：brpc内置提供，无需额外配置即可在监控页面查看
- **辅助参数调优**：专门用于辅助选择合理的`backup_request_ms`值，优化备用请求策略
- **可扩展**：支持通过`bvar::LatencyRecorder`自行添加自定义函数的latency_cdf监控
- **时间单位**：默认延迟单位为微秒（μs），数据采集使用`butil::Timer`进行高精度计时

## 应用
- **backup_request参数调优**：通过观察cdf图，开发者可以选择合适的`backup_request_ms`值。例如，若选择2ms可覆盖95.5%的请求，10ms可覆盖99.99%的请求，则可根据服务的延迟容忍度选择合适的超时阈值
- **性能监控与诊断**：快速识别服务延迟分布特征，判断是否存在长尾延迟问题
- **自定义函数性能分析**：业务代码中可通过`bvar::LatencyRecorder`和`butil::Timer`为特定函数添加延迟监控，生成独立的cdf图
- **SLA评估**：根据cdf图评估服务是否满足特定百分位的延迟SLA要求（如P99、P999延迟）

## 相关概念
- [[concepts/backup-request|backup request]]
- [[concepts/latency-recorder|LatencyRecorder]]

## 相关实体
- [[entities/bvar|bvar]]
- [[entities/baidu|baidu]]

## 来源提及
- "可以观察brpc默认提供的latency_cdf图，或自行添加。cdf图的y轴是延时（默认微秒），x轴是小于y轴延时的请求的比例。" — [[sources/backup_request|backup_request]]
- "在下图中，选择backup_request_ms=2ms可以大约覆盖95.5%的请求，选择backup_request_ms=10ms则可以覆盖99.99%的请求。" — [[sources/backup_request|backup_request]]
- "自行添加的方法：`my_func_latency << tm.u_elapsed();`" — [[sources/backup_request|backup_request]]