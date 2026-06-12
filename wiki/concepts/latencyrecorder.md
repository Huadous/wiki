---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/backup_request]]"]
tags: [term]
aliases:
  - "bvar::LatencyRecorder"
  - "延迟记录器"
  - "brpc延迟记录器"
---


# LatencyRecorder

## 定义
LatencyRecorder是brpc的bvar库（bvar）中提供的延迟记录器类，用于收集用户自定义函数的延迟分布统计数据。开发者通过创建LatencyRecorder对象，使用butil::Timer记录函数执行时间，并将耗时（微秒/毫秒/秒等）赋值给记录器，即可在/vars监控页面自动获得qps、延迟、延迟CDF图等丰富的计数器。

## 关键特征
- **自动生成多维统计**：创建LatencyRecorder实例后，系统自动产生qps、延迟、延迟CDF等系列指标
- **与bvar库集成**：作为bvar（bvar）的一部分，与brpc内部监控体系无缝对接
- **多时间单位支持**：支持微秒（u_elapsed）、毫秒（m_elapsed）、秒（s_elapsed）、纳秒（n_elapsed）多种粒度的时间记录
- **低侵入性**：只需包含头文件、创建对象、记录耗时三步即可完成接入，对业务代码改动极小
- **实时可视化**：统计结果通过/vars监控页面实时展示，无需额外配置

## 应用
- **延迟优化辅助**：brpc文档中明确提到LatencyRecorder是优化backup_request_ms的重要辅助手段，帮助开发者定位延迟瓶颈
- **自定义函数监控**：对非RPC函数（如本地计算、外部服务调用）进行性能分析
- **业务指标采集**：在业务逻辑关键路径上插入延迟记录，用于监控告警和容量规划
- **性能回归测试**：在自动化测试中嵌入LatencyRecorder，评估代码变更对性能的影响
- **分布式追踪补充**：与分布式追踪工具配合，提供函数粒度的性能快照

## 相关概念
- [[concepts/latency_cdf|latency_cdf]] — 延迟累积分布函数，由LatencyRecorder自动生成
- [[concepts/bvar|bvar]] — 底层统计库，LatencyRecorder依赖其聚合能力
- [[concepts/backup_request|backup_request]] — LatencyRecorder常用于优化的关键机制

## 相关实体
- [[entities/bvar|bvar]] — 提供LatencyRecorder实现的统计库
- [[entities/brpc|brpc]] — 所属框架生态

## 来源提及
- "自行添加的方法：" — [[brpc/backup_request|backup_request]]
- "bvar::LatencyRecorder my_func_latency("my_func");" — [[brpc/backup_request|backup_request]]
- "my_func_latency << tm.u_elapsed();  // u代表微秒，还有s_elapsed(), m_elapsed(), n_elapsed()分别对应秒，毫秒，纳秒。" — [[brpc/backup_request|backup_request]]
- "好了，在/vars中会显示my_func_qps, my_func_latency, my_func_latency_cdf等很多计数器。" — [[brpc/backup_request|backup_request]]