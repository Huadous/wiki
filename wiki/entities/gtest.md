---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Google Test"
  - "Google C++ Testing Framework"
---


# gtest

## 基本信息
- Type: 产品
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述
gtest 是 Google 开发的 C++ 测试框架，被广泛应用于 C++ 项目的单元测试。在 brpc 项目中，gtest 用于运行单元测试套件，确保各组件的正确性。不同操作系统上安装方式各不相同：在 Ubuntu 上需要安装 `libgtest-dev` 并在 `/usr/src/gtest` 目录下手动编译；在 Fedora 上安装 `gtest-devel`；在 MacOS 上可通过 `brew install googletest` 或手动编译安装。brpc 项目通过 cmake 的 `-DBUILD_UNIT_TESTS=ON` 选项启用测试，随后运行 `make test` 或 `sh run_tests.sh` 来执行测试。gtest 的安装和正确编译是运行 brpc 测试套件的前提条件。

## 相关实体
- [[entities/brpc|brpc]]
- [[entities/cmake|cmake]]

## 相关概念
- [[concepts/单元测试|单元测试]]
- [[concepts/构建系统|构建系统]]

## 来源提及
- "If you need to run tests, install and compile libgtest-dev" — [[sources/en_getting_started|en_getting_started]]
- "sudo apt-get install -y cmake libgtest-dev && cd /usr/src/gtest && sudo cmake . && sudo make && sudo mv lib/libgtest* /usr/lib/ && cd -" — [[sources/en_getting_started|en_getting_started]]
- "To run tests: cd test && make && sh run_tests.sh" — [[sources/en_getting_started|en_getting_started]]