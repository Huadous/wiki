---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "other"
aliases:
  - "config_brpc.sh"
  - "BRPC 配置脚本"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/gflags|gflags]]
- [[entities/protobuf|protobuf]]
- [[entities/leveldb|leveldb]]
- [[entities/cmake|cmake]]
- [[entities/glog|glog]]
- [[entities/thrift|thrift]]

## Related Concepts
- [[concepts/静态链接|静态链接]]
- [[concepts/构建系统|构建系统]]

## Mentions in Source
- "sh config_brpc.sh --headers=/usr/include --libs=/usr/lib --cc=clang --cxx=clang++" — [[sources/en_getting_started|en_getting_started]]
- "To not link debugging symbols, add --nodebugsymbols" — [[sources/en_getting_started|en_getting_started]]
- "To use brpc with glog, add --with-glog." — [[sources/en_getting_started|en_getting_started]]
- "To enable thrift support, install thrift first and add --with-thrift." — [[sources/en_getting_started|en_getting_started]]

> **Source: [[sources/getting_started|getting_started]]**
> - "使用config_brpc.sh编译brpc"
> - "$ sh config_brpc.sh --headers=/usr/include --libs=/usr/lib"
> - "这里我们给`--headers`和`--libs`传递多个路径使得脚本能够在多个地方进行检索。"