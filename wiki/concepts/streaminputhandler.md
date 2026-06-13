---
type: concept
created: 2026-06-12
updated: 2026-06-13
sources:
  - "[[]]"
  - "[[brpc/streaming_rpc.md]]"
tags:
  - "standard"
aliases:
  - "流输入处理接口"
  - "Stream 输入处理器"
---

## Related Concepts

- [[concepts/stream|Stream]]
- [[concepts/streamoptions|StreamOptions]]
- [[concepts/streaming-rpc|Streaming RPC]]

## Related Entities

- [[entities/brpc|brpc]]
- [[entities/iobuf|IOBuf]]

## Mentions in Source

> **Source: [[sources/en_streaming_rpc|en_streaming_rpc]]**
> - "class StreamInputHandler { public: // Callback when stream receives data virtual int on_received_messages(StreamId id, butil::IOBuf *const messages[], size_t size) = 0; // Callback when there is no data for a long time on the stream virtual void on_idle_timeout(StreamId id) = 0; // Callback when stream is closed by the other end virtual void on_closed(StreamId id) = 0; };"
> - "on_received_messages 首次调用的时机：在客户端同步 RPC 返回后或异步 RPC done->Run() 后，在服务端 done->Run() 后"

> **Source: [[sources/streaming_rpc|streaming_rpc]]**
> - "在建立或者接受一个Stream的时候， 用户可以继承StreamInputHandler并把这个handler填入StreamOptions中. 通过这个handler，用户可以处理对端的写入数据，连接关闭以及idle timeout"
> - "Handle input message, if handler is NULL, the remote side is not allowed to write any message, who will get EBADF on writing"