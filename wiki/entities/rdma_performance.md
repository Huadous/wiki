---
type: entity
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/rdma|rdma]]"]
tags: [other]
aliases:
  - "RDMA性能测试示例"
  - "rdma_performance example"
  - "brpc RDMA performance example"
---


# rdma_performance

## 基本信息
- Type: other
- Source: [[sources/rdma|rdma]]

## 描述
rdma_performance是[[entities/brpc|brpc]]官方提供的RDMA性能测试示例程序，位于 `example/rdma_performance` 目录下，用于演示和测试[[concepts/rdma|RDMA]]读写性能。该示例支持Server和Client两种角色，可通过 `config_brpc.sh`、`make` 或 `bazel` 三种方式编译，其编译方式与其他RDMA集成方式类似。该程序是用户验证brpc RDMA功能正确性和性能表现的重要参考实现之一。

## 相关实体
- [[entities/brpc|brpc]]

## 相关概念
- [[concepts/rdma|RDMA]]

## 来源提及
- `cd example/rdma_performance  # 示例程序 — [[sources/rdma|rdma]]`
- `make — [[sources/rdma|rdma]]`
- `bazel build --define=BRPC_WITH_RDMA=true example:rdma_performance_server — [[sources/rdma|rdma]]`
- `bazel build --define=BRPC_WITH_RDMA=true example:rdma_performance_client — [[sources/rdma|rdma]]`