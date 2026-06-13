---
type: concept
created: 2026-06-13
updated: 2026-06-13
sources: ["[[sources/baidu_std|baidu_std]]"]
tags: [standard]
aliases:
  - "HTTP Interface"
  - "HTTP接口规范"
---


# HTTP接口

## 定义
HTTP接口是 [[sources/baidu_std|baidu_std]] 协议规定的对外服务发布方式之一，要求服务以标准的 HTTP 协议对外发布接口。协议建议使用 RESTful 形式的 Web Service 接口，数据交换格式默认应使用 JSON，Content-Type 使用 `application/json`。

## 关键特征
- **传输协议**：使用标准的 HTTP 协议对外发布接口
- **数据格式**：数据交换格式默认应使用 JSON，Content-Type 使用 `application/json`
- **字符编码**：URL 和 JSON 中的字符编码一律使用 UTF-8
- **接口风格**：协议建议使用 RESTful 形式的 Web Service 接口
- **特殊场景例外**：有特殊需求的接口不受 JSON/application/json 限制，例如上传文件可使用 `multipart/form-data`，下载文件可根据实际内容选用合适的 Content-Type

## 应用
- 面向 Web 浏览器或移动端的标准化 API 发布
- 跨语言、跨平台的轻量级服务调用场景
- 文件上传/下载等需要特殊 Content-Type 的服务场景
- 对外开放的服务接口，要求遵循通用 HTTP 规范以便第三方接入

## 相关概念
- [[concepts/RESTful|RESTful]]
- [[concepts/RPC|RPC]]

## 相关实体
- [[sources/baidu_std|baidu_std]]

## 来源提及
- "服务应以标准的HTTP协议对外发布接口。" — [[sources/baidu_std|baidu_std]]
- "数据交换格式默认应使用JSON。Content-Type使用application/json。有特殊需求的接口不受此限制。例如上传文件可以使用multipart/form-data；下载文件可以根据实际内容选用合适的Content-Type。" — [[sources/baidu_std|baidu_std]]
- "URL和JSON中的字符编码一律使用UTF-8。" — [[sources/baidu_std|baidu_std]]