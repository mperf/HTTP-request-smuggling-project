# Task 1
Now that we have introduced the basics of the HTTP format, we will craft an attack that exploits a  Transfer-Encoding / Content-Length parsing mismatch. As you might have noticed, the trailing `0` in the tutorial did not matter for the request to be valid- could we perhaps use the fact that some parts of the message won't be read but still be accepted?

HTTP request smuggling (HRS) is an exploit that takes advantage of inconsistencies in HTTP request parsing between intermediary components (reverse proxies & load balancers) and back-end servers. The vulnerability typically arises because the HTTP/1 specification provides two different ways to specify where a request ends.

**What headers play an important role in HTTP request smuggling and what is their function?**

## Task 1.1
`request1.txt` has an empty header `Content-Length`. Set the header so that only `q=smuggling` is read. Do not modfiy the HTTP body.

## Task 1.2
`request2.txt` has the header `Transfer-Encoding: chunked`. Modify the body so that `q=smugglingab` is read. Do not change the headers, change only the necessary part in the body that `Transfer-Encoding` needs.

**What happens when you input a chunk that is too big or too small?**

## Executing your solutions
Test your solutions by running `./test.py`. This will also print out the servers response to your requests. Remember to have the server running.