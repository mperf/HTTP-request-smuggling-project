# Tutorial
HTTP request smuggling is an attack that exploits flaws in how websites handle HTTP requests. This exploit is primarily targeting vulnerabilities in how HTTP/1 requests are interpreted but, depending on how a website is set up, HTTP/2 may also be vulnerable.

## How HTTP works
HTTP (Hypertext Transfer Protocol) is a simple, text-based, request/response protocol. A client (browser, script, scanner) opens a TCP connection to a server, sends a request, and the server replies with a response.

An HTTP request has:
- A request line
- Headers
- A blank line
- An optional message body

An example HTTP request (note that the order is always the same as written above):
```http
GET /index.html HTTP/1.1
Host: www.example.re
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.1)
Accept: text/html
Accept-Language: en-US, en; q=0.5
Accept-Encoding: gzip, deflate

q=smuggling
```
## What are HTTP headers?
HTTP headers pass additional information with a request/ response message. 
- General headers: apply to both requests and responses (e.g., Connection, Date)
- Request headers: sent by the client (e.g.: Host, User-Agents, Cookie, Content-Length)
- Response headers: sent by the server (e.g., Server, Location)
- Entity/ Representation headers: describe the message body (e.g., Content-Type, Content-Length, Content-Encoding)

## Execution the tutorial

Test your request by running `./test.py`. This will also print out the servers response to your request in `solution.txt`. When it comes to HTTP request smuggling, the following could be helpful to think about for a second before starting the tasks;
- Would the request still work if we removed the trailing `0` at the end?
- What happens with the parts of the HTTP requests that aren't read?