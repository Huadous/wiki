---
type: entity
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[sources/en_server]]"
  - "[[brpc/server.md]]"
tags:
  - "other"
aliases:
  - "证书结构"
  - "SSL证书信息"
  - "CertInfo结构体"
---

## Related Entities
- [[entities/brpc|brpc]]

## Related Concepts
- [[concepts/streaming-rpc|streaming-rpc]]
- [[concepts/baidu_std-protocol|baidu_std-protocol]]
- [[concepts/sni|SNI]]
- [[concepts/ssl|SSL]]
- [[concepts/server-ssl-options|ServerSSLOptions]]

## Mentions in Source
> **Source: [[sources/server|server]]**
> - "Certificate structure\nstruct CertInfo {\n    // Certificate in PEM format.\n    // Note that CN and alt subjects will be extracted from the certificate,\n    // and will be used as hostnames. Requests to this hostname (provided SNI\n    // extension supported) will be encrypted using this certifcate.\n    // Supported both file path and raw string\n    std::string certificate;"
> - "Additional hostnames besides those inside the certificate. Wildcards are supported but it can only appear once at the beginning (i.e. *.xxx.com).\n    std::vector<std::string> sni_filters;"
> - "No directly relevant information"