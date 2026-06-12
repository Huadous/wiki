---
type: concept
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[sources/en_server]]"
  - "[[sources/en_http_service]]"
tags:
  - "method"
aliases:
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip compression (in brpc)"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "Gzip压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip响应体压缩"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
  - "gzip compression"
  - "响应压缩"
  - "Response Compression"
  - "压缩算法"
---

## Related Concepts
- [[concepts/http-header|HTTP header]]
- [[concepts/content-type|Content-Type]]
- [[concepts/渐进发送|渐进发送]]
- [[concepts/http-参数|HTTP参数]]
- [[concepts/controller|Controller]]
- [[concepts/http-body-compress-threshold|http_body_compress_threshold]]
- [[concepts/content-encoding|Content-Encoding]]
- [[concepts/accept-encoding|Accept-Encoding]]

## Related Entities
- [[entities/brpc|brpc]]
- [[entities/iobuf|iobuf]]
- [[entities/hulu_pbrpc|hulu_pbrpc]]
- [[entities/nova_pbrpc|nova_pbrpc]]
- [[entities/sofa_pbrpc|sofa_pbrpc]]
- [[entities/public_pbrpc|public_pbrpc]]
- [[entities/nshead_mcpack|nshead_mcpack]]
- [[entities/curl|curl]]
- [[entities/bvar|bvar]]
- [[entities/nginx|nginx]]
- [[entities/redis|redis]]
- [[entities/grpc|grpc]]

## Mentions in Source

> **Source: [[sources/en_server]]**
> - "set_response_compress_type() sets compression method for the response, no compression by default."
> - "Supported compressions: brpc::CompressTypeSnappy, brpc::CompressTypeGzip, brpc::CompressTypeZlib"
> - "Attachment is not compressed."
> - "brpc::CompressTypeSnappy : snanpy, compression and decompression are very fast, but compression ratio is low."
> - "brpc::CompressTypeGzip : gzip, significantly slower than snappy, with a higher compression ratio."
> - "brpc::CompressTypeZlib : zlib, 10%~20% faster than gzip, slightly higher compression ratio."
> - "set_response_compress_type() sets compression method for the response, no compression by default. — [[brpc/en_server|en_server]]"
> - "Supported compressions: brpc::CompressTypeSnappy : [snanpy](http://google.github.io/snappy/), compression and decompression are very fast, but compression ratio is low. — [[brpc/en_server|en_server]]"
> - "brpc::CompressTypeGzip : [gzip](http://en.wikipedia.org/wiki/Gzip), significantly slower than snappy, with a higher compression ratio. — [[brpc/en_server|en_server]]"

> **Source: [[sources/en_http_service]]**
> - "Call `Controller::set_response_compress_type(brpc::COMPRESS_TYPE_GZIP)` to **try to** compress the http body with gzip."
> - "Body size is less than the bytes specified by -http_body_compress_threshold (512 by default)."
> - "gzip is not a very fast compression algorithm."
> - "Not compress http body when it's less than so many bytes."
> - "Call Controller::set_response_compress_type(brpc::COMPRESS_TYPE_GZIP) to try to compress the http body with gzip. — [[brpc/en_http_service|en_http_service]]"
> - "The request does not set Accept-encoding or the value does not contain "gzip". — [[brpc/en_http_service|en_http_service]]"
> - "Body size is less than the bytes specified by -http_body_compress_threshold (512 by default). — [[brpc/en_http_service|en_http_service]]"