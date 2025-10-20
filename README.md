# HTTP-request-smuggling-project

# HTTP-requests
Explain how does HTTP work
* What does a http request look like?
* what are the headers?
* “ok this is a simple HTTP request, execute it and tell me the response”
* basically use curl to access a website
* maybe create a simple web server that requires some headers to get 200 OK response


# HTTP-request-smuggling
intro to the vulnerability
* theory
* how can we manipulate the headers?
* How can we prevent such attacks?
* examples


### Getting started
* Along the lines of the first lab; the focus should be to learn the arguments and what happens, be careful with using tools since it can generalize the process too much.
* how to connect and set up the lab

### Learning Goals
* Could outline the core concepts that the person doing the lab should learn from it (essentially what we've learned from it)

### Troubleshooting Guide
* Could be useful

### Assignment

#### Task 1 - contact an unauthenticated page (goes through both server)
Instructions for task 1

#### Task 2 - contact an authorized page (the first server blocks the request)
Instructions for task 2

#### Task 3 - develop an attack to bypass the authentication of the first server
Instructions for task 3


#### Report
In case we want them to give written answers to something
#### Problem Statement
Modern web applications often rely on multiple servers, such as a front-end proxy and a back-end application server, to handle HTTP traffic efficiently. However, these servers do not always interpret HTTP requests in exactly the same way. Small differences in how they handle headers like Content-Length and Transfer-Encoding can cause them to disagree on where one request ends and the next begins.
This inconsistency can be exploited by an attacker to smuggle hidden HTTP requests through the connection, a vulnerability known as HTTP Request Smuggling. Because the front-end and back-end see different versions of the same request, the attacker’s hidden payload can bypass security checks, manipulate server behavior, or access data belonging to other users.

#### References 
We used the PortSwigger Lab as a starting point for our own lab. We studied their exercises to gain a practical understanding of HTTP request smuggling and to analyse example request/response patterns. However, we implemented all infrastructure, scenarios and tasks for this project independently. For learning purposes only, we reproduced key behaviours observed in the PortSwigger material, then designed and developed original lab tasks and solutions.

#### Contributions
##### Mattia Perfumo
Developed the Docker virtual infrastructure for the lab, including two web servers, a sample script to simulate the attack, and the task objectives. The development started by analyzing the HTTP Request Smuggling vulnerability and how it can be exploited. The lab was designed to provide a hands-on experience to understand the vulnerability and explore different attack vectors. My approach was to create a first server that handles authentication via HTTP Basic Authentication and a second server exposing different endpoints, some of which are protected by the first server. I encountered challenges in finding the right configuration for the servers to simulate the vulnerability effectively. I tried different services and configurations, including using Nginx, Apache, and documented CVEs, but eventually settled on a different approach that allowed for a more straightforward setup. The final architecture relies on a script that sends the student's requests to the first server and, after some milliseconds, it sends inside the same connection (crucial for the attack) a victim request. This enabled different attack vectors, which were then documented as objectives for the lab. The first objective is to redirect the victim to another page, potentially allowing the attacker to perform actions on behalf of the victim. The second objective is to delete the victim's account, demonstrating the impact of the vulnerability. Moreover, the last objective is to leak the victim's headers, which contain the authentication information. These objectives were then translated into tasks for the students to complete by my colleagues, who provided detailed instructions and explanations for each task.

##### Sarah Winter
My main contribution to the group project was researching and writing the theory section on HTTP and HTTP Request Smuggling. I spent a considerable amount of time reading and experimenting with examples in order to gain a thorough understanding of how HTTP works, how requests and responses are constructed, the function of headers, and how different servers handle them. I also investigated how reverse proxies and back-end servers interact, as this information is crucial for identifying potential smuggling vulnerabilities. Next, I delved deeper into the topic of request smuggling itself: how this kind of attack works in practice; why it happens; the vulnerabilities it exploits; and how it can be prevented. Armed with this knowledge, I wrote the theory section of our report and created the theory questions and lab tasks. The aim was to create exercises that would help students to understand the topic step by step rather than just memorise it. This took a considerable amount of time as it was surprisingly difficult to write questions that were both clear and challenging. I had to rewrite and adjust several of the questions so that they matched the rest of the lab setup and guided students towards understanding the concept independently. In addition, I wrote the solutions for all the theory tasks. While the others focused mainly on building and testing the lab environment, I worked on the research, writing and task design, which required a great deal of independent work and problem solving. Overall, I spent a considerable amount of time learning, experimenting and writing to ensure that the theoretical aspect of the project was comprehensive and comprehensible.

##### Lukas Malmberg



##### Fabian Andréasson

### Acknowledgment
This task was designed by:         <br>
Mattia Perfumo                     <br>
Fabian Andréasson                  <br>
Lukas Malmberg                     <br>
Sarah Winter                       <br>


### useful links

https://nathandavison.com/blog/haproxy-http-request-smuggling
