---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_http_service]]"
tags:
  - "term"
aliases:
  - "未解析路径"
  - "Controller.unresolved_path"
  - "未解析路径段"
---

## Related Entities
- [[entities/brpc|brpc]]  
- [[entities/baidu|baidu]]  
- [[entities/curl|curl]]

## Mentions in Source

> **Source: [[sources/en_http_service|en_http_service]]**
- "the path after /HttpService/Echo is filled into cntl->http_request().unresolved_path(), which is always normalized"
- "The path after asterisk can be obtained by cntl.http_request().unresolved_path(), which is always normalized, namely no slashes at the beginning or the end, and no repeated slashes in the middle."
- "the path after `/HttpService/Echo ` is filled into `cntl->http_request().unresolved_path()`, which is always normalized"
- "The path after asterisk can be obtained by `cntl.http_request().unresolved_path()`, which is always normalized, namely no slashes at the beginning or the end, and no repeated slashes in the middle."
- "cntl->response_attachment().append(cntl->http_request().unresolved_path());"
- "The path after `/HttpService/Echo` is filled into `cntl->http_request().unresolved_path()`, which is always normalized"
- "The path after `/FileService` is filled in `cntl->http_request().unresolved_path()`, which is always normalized"
- "Note that cntl.http_request().uri().path() is not ensured to be normalized, which is \"//v1//queue//stats//foo///bar//////\" ..."
- "in which unresolved_path are both foo/bar. The extra slashes at the left, the right, or the middle are removed."
- "the path after /FileService is filled in cntl->http_request().unresolved_path(), which is always normalized"

## Additional Information

unresolved_path是brpc HTTP请求中经过URL路由匹配后剩余的路径部分，常用于资源管理服务或Restful URL模式。它总是被归一化（normalized），即没有开头和结尾的斜杠，中间没有重复斜杠。在Service-Prefix模式中，路径/FileService之后的子路径会填入unresolved_path；在Restful模式中，通配符*匹配的部分也会填入unresolved_path。这提供了访问请求路径中动态片段的标准方式。需要注意的是，`cntl.http_request().uri().path()`并不保证被归一化，可能包含多余的斜杠，而unresolved_path则始终是干净且规范的路径。