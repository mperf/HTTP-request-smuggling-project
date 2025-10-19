# Task 1
Now that we have introduced the basics of the HTTP format, we will craft an attack that exploits a  Transfer-Encoding / Content-Length parsing mismatch. As you might have noticed, the trailing `0` in the tutorial did not matter for the request to be valid- could we perhaps use the fact that some parts of the message won't be read but still be accepted?

HTTP request smuggling (HRS) is an exploit that takes advantage of inconsistencies in HTTP request parsing between intermediary components (reverse proxies & load balancers) and back-end servers. The vulnerability typically arises because the HTTP/1 specification provides two different ways to specify where a request ends.

**What headers play an important role in HTTP request smuggling and what is their function?**
Content-Length Header: Declares the exact number of bytes in the message body.
Transfer-Encoding Header: Specifies whether the body contains one or more chunked data. Each chunk consists of the chunk size in bytes (expressed in hexadecimal), followed by a newline, followed by the chunk contents.

## Task 1.1
`request1.txt` has an empty header `Content-Length`. Set the header so that only `q=smuggling` is read. Do not modfiy the HTTP body.

POST /postComment HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smugglingab

## Task 1.2
`request2.txt` has the header `Transfer-Encoding: chunked`. Modify the body so that `q=smugglingab` is read. Do not change the headers, change only the necessary part in the body that `Transfer-Encoding` needs.

POST /postComment HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked

d
q=smugglingab
0

**What happens when you input a chunk that is too big or too small?**
If the chunk size too big, the receiver waits for the extra bytes it was told to expect, which can hang or block the connection and let the other side treat subsequent bytes differently.
If the chunk size is too small, the receiver stops after the declared size so the leftover bytes become the start of the next chunk or request, which lets an attacker shift data and smuggle extra requests.