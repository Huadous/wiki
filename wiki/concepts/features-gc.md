---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/editions-life-of-an-edition]]"]
tags: [method]
aliases:
  - "Feature GC"
  - "feature garbage collection"
  - "Features GC"
---


# Features GC

## 定义
Features GC（Features Garbage Collection，特性垃圾回收）是 [[entities/protoc|protoc]] 提供的一款命令行工具，运行 `protoc --gc-features foo.proto` 时，会针对处于 editions 模式下的 proto 文件，计算为维持文件原有行为而需要显式设置的特性（feature）最小集（或在计算代价过高时给出启发式最小集）。该工具读取文件中声明的 edition，并基于此推导出所有可继承的特性默认值，从而仅保留必须显式覆盖的特性，避免冗余显式设置。Features GC 的输出是 Protochangifier [[concepts/ProtoChangeSpec|ProtoChangeSpec]]，可用于自动清理大量 proto 文件。

## 关键特征
- 以 `protoc --gc-features` 子命令形式提供，属于 protoc 编译器工具链能力。
- 仅作用于 editions 模式下的 proto 文件，依据文件中声明的 edition 推导可继承的特性默认值。
- 输出为最小（或启发式最小）的必须显式设置的特性集合，而非全量特性集。
- 当精确最小集计算成本过高时，会退化为启发式最小集以保证可用性。
- 输出格式为 Protochangifier ProtoChangeSpec，可作为后续自动改写工具的输入。
- 适用于批量清理因历史演进而积累冗余或不一致特性设置的 proto 文件。

## 应用
- 对已有的 editions 模式 proto 文件进行批量清理，剔除为维持行为所不需要的冗余特性显式声明。
- 作为 Protochangifier 流水线的前置步骤，自动生成 ProtoChangeSpec 以驱动大规模 schema 改写。
- 在 [[concepts/Editions-adopter|Editions adopter]] 与 [[concepts/Editions-upgrader|Editions upgrader]] 工作流中辅助保持特性集最小化与一致性。
- 帮助 schema 作者验证当前特性显式设置是否与所选 edition 的默认值一致，从而定位不必要的显式覆盖。

## 相关概念
- [[concepts/Editions-adopter]]
- [[concepts/Editions-upgrader]]
- [[concepts/ProtoChangeSpec]]
- [[concepts/Feature]]

## 相关实体
- [[entities/protoc]]

## 来源提及
- "The features GC. Running protoc --gc-features foo.proto on a file in editions mode will compute the minimal (or a heuristically minimal, if this proves expensive) set of features to set on things, given the edition specified in the file." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]
- "This will produce a Protochangifier ProtoChangeSpec that describes how to clean up the file." — [[sources/editions-life-of-an-edition|editions-life-of-an-edition]]