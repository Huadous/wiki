---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_getting_started]]"
  - "[[brpc/getting_started.md]]"
tags:
  - "product"
aliases:
  - "Google Test"
  - "Google C++ Testing Framework"
---

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/cmake|cmake]]
- [[entities/ubuntu|Ubuntu]]
- [[entities/centos|CentOS]]
- [[entities/homebrew|Homebrew]]

## Related Concepts
- [[concepts/单元测试|单元测试]]
- [[concepts/构建系统|构建系统]]

## Mentions in Source
> **Source: [[sources/en_getting_started|en_getting_started]]**
> - "If you need to run tests, install and compile libgtest-dev"
> - "sudo apt-get install -y cmake libgtest-dev && cd /usr/src/gtest && sudo cmake . && sudo make && sudo mv lib/libgtest* /usr/lib/ && cd -"
> - "To run tests: cd test && make && sh run_tests.sh"

> **Source: [[sources/getting_started|getting_started]]**
> - "如果你要运行测试，那么要安装并编译libgtest-dev（它没有被默认编译）："
> - "如果你要运行测试，需安装gtest。先运行`brew install googletest`看看homebrew是否支持（老版本没有），没有的话请下载和编译googletest"