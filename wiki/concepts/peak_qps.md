---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[brpc/auto_concurrency_limiter|auto_concurrency_limiter]]"]
tags: [term]
aliases:
  - "峰值QPS"
  - "peak qps"
---


# peak_qps

## 定义
peak_qps 是服务的 QPS（Queries Per Second，每秒查询数）上限，表示服务在单位时间内能够处理或回复的最大请求数。它取决于 `best_max_concurrency`（最佳最大并发度）与 `noload_latency`（无负载延迟）的比值，是服务的固有属性，与拥塞状况无关，但可能随时间逐渐改变。需要注意，peak_qps 指的是**处理或回复**的 QPS，而不是**接收**的 QPS。

## 关键特征
- **固有属性**：peak_qps 由服务的 `best_max_concurrency` 和 `noload_latency` 决定，这两个量都是服务的固有属性，因此 peak_qps 也是服务的固有属性。
- **与拥塞无关**：peak_qps 的值不会因当前拥塞状况而改变，但可能随时间推移（如硬件升级、代码优化或环境变化）而逐渐变化。
- **处理量而非接收量**：peak_qps 衡量的是服务实际处理或回复的 QPS，而非接收请求的 QPS。
- **自适应限流的核心参数**：自适应限流的目标之一就是正确估算 peak_qps，以便将最大并发设置为靠近 `peak_qps × noload_latency` 的值（即满足 [[concepts/Little's Law|Little's Law]] 的理想并发度）。

## 应用
- **自适应限流（Auto Concurrency Limiter）**：自适应限流需要正确估算服务的 `noload_latency` 和 `peak_qps`，并将最大并发设置为靠近两者乘积的一个值，从而在保证服务稳定性的同时最大化吞吐量。brpc 的自适应限流实现参见 [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]。
- **服务启动时的快速打满**：在服务启动时需要快速打满 QPS 以减少流量损失。brpc 采用了两个措施来加速 peak_qps 的估算收敛：
  1. **立即提交采样窗口**：不等待采样窗口填满即可提交数据。
  2. **不平滑更新 max_qps**：对 max_qps 的更新不做平滑处理，使其能更快地反映真实容量。

## 相关概念
- [[concepts/自适应限流]]
- [[concepts/max_qps]]
- [[concepts/best_max_concurrency]]
- [[concepts/noload_latency]]
- [[concepts/Little's Law]]

## 相关实体
（无相关实体）

## 来源提及
- peak_qps: qps的上限。注意是处理或回复的qps而不是接收的qps。值取决于best_max_concurrency / noload_latency，这两个量都是服务的固有属性，故peak_qps也是服务的固有属性，和拥塞状况无关，但可能随时间逐渐改变。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]
- 自适应限流就是要找到服务的noload_latency和peak_qps， 并将最大并发设置为靠近两者乘积的一个值。 — [[sources/auto_concurrency_limiter|auto_concurrency_limiter]]