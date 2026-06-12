---
type: entity
created: 2026-06-12
updated: 2026-06-12
sources: ["[[sources/en_getting_started]]"]
tags: [product]
aliases:
  - "Docker引擎"
  - "Docker容器平台"
---


# Docker

## 基本信息
- Type: product
- Source: [[sources/en_getting_started|en_getting_started]]

## 描述

Docker是一个开源的容器化平台，用于简化应用的构建、部署和运行。它通过轻量级容器技术提供一致的环境，确保应用在不同系统间的可移植性。brpc官方推荐使用Docker作为快速体验和开发brpc的方式之一——用户只需克隆brpc仓库，执行`docker build -t brpc:master .`即可构建包含完整依赖的brpc镜像，随后通过`docker run -it brpc:master /bin/bash`进入容器进行开发或测试。Docker环境为brpc的编译和运行提供了隔离性，避免了本地环境配置的复杂性，特别适合快速尝鲜或在不同操作系统上进行brpc的试用。这使得开发者无需手动安装[[entities/openssl|OpenSSL]]、[[entities/gcc|GCC]]等依赖即可直接构建brpc项目。

## 相关实体

- [[entities/openssl|OpenSSL]]
- [[entities/gcc|GCC]]
- [[entities/cmake|CMake]]
- [[entities/glibc|GNU C Library]]
- [[entities/open-source-oss-community|开源社区]]

## 相关概念

无相关概念。

## 来源提及

- "Compile brpc with docker:" — [[sources/en_getting_started|en_getting_started]]
- "docker build -t brpc:master ." — [[sources/en_getting_started|en_getting_started]]
- "docker run -it brpc:master /bin/bash" — [[sources/en_getting_started|en_getting_started]]