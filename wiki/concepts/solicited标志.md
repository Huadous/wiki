---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
tags: [term, method]
aliases:
  - "solicited event flag"
  - "solicited completion flag"
  - "请求完成标志"
---


# solicited标志

## 定义

solicited标志是RDMA发送操作中的一个控制标志，用于指示接收端在处理完该消息后是否产生事件通知（即CQ中的完成通知）。在brpc的RDMA事件聚合机制中，该标志被选择性设置以优化事件触发频率，避免每个小消息都触发性能开销较高的完成通知。

## 关键特征

- **选择性设置**：`RdmaEndpoint`综合考虑数据大小、窗口状态与ACK情况，为每个发送消息独立决定是否设置solicited标志
- **事件控制**：设置标志后，消息完成时会触发CQ中的完成通知事件；不设置则不会触发
- **性能优化**：通过选择性设置，避免大量小消息各自触发事件导致性能退化
- **与滑动窗口联动**：标志设置策略与滑动窗口流控机制协同工作，在保证可靠性的同时减少事件处理次数

## 应用

- **brpc RDMA事件聚合**：作为事件聚合机制的核心控制参数，`RdmaEndpoint`利用solicited标志大幅减少CQ轮询和事件处理的频率
- **批量消息完成通知**：当一个消息被标记为solicited时，它之前的未标记消息的完成状态会一并被聚合通知，实现批量完成确认
- **减少上下文切换**：避免高频事件触发导致的用户态与内核态频繁切换，提升高吞吐场景下的传输效率

## 相关概念

- [[concepts/event-aggregation|事件聚合]]
- [[concepts/CQ|CQ]]
- [[concepts/sliding-window-flow-control|滑动窗口流控]]

## 相关实体

- [[entities/rdmaendpoint|RdmaEndpoint]]

## 来源提及

- "因此，RdmaEndpoint综合考虑数据大小、窗口与ACK的情况，对每个发送消息选择性设置solicited标志，来控制是否在发送端触发事件通知。" — [[sources/rdma|rdma]]
- "如果每个消息都触发事件进行处理，会导致性能退化严重，甚至不如TCP传输。" — [[sources/rdma|rdma]]