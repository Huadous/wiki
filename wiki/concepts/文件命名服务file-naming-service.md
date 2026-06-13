---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/combo_channel]]"
  - "[[brpc/load_balancing.md]]"
tags:
  - "method"
aliases:
  - "file://命名服务"
  - "File Naming Service"
  - "文件命名服务"
  - "file naming service"
  - "file://命名服务"
  - "File Naming Service"
  - "文件命名服务"
---

## Related Concepts
- [[concepts/命名服务|命名服务]]
- [[concepts/容量计算规则|容量计算规则]]
- [[concepts/DynamicPartitionChannel|DynamicPartitionChannel]]
- [[concepts/PartitionChannel|PartitionChannel]]

## Related Entities
- [[entities/etcd|etcd]]
- [[entities/zookeeper|zookeeper]]
- [[entities/bns|bns]]
- [[entities/filewatcher|FileWatcher]]
- [[entities/namingservicethread|NamingServiceThread]]
- [[entities/namingservicewatcher|NamingServiceWatcher]]

## Mentions in Source
> **Source: [[sources/combo_channel|combo_channel]]**
> - "命名服务"file://server_list"的内容是："
> - "09-06 10:51:10:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 3 unique addresses from `server_list`"
> - "开始修改分库，在server_list中加入4分库的8005："
> - "客户端发现了server_list的变化并重新载入，但qps并没有什么变化。"

> **Source: [[sources/load_balancing|load_balancing]]**
> - "file：列表即文件。合理的方式是在文件更新后重新读取。"
> - "file://<file-path>           # load addresses from the file"