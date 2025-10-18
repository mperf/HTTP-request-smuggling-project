#!/usr/bin/env python3

import socket
import time
import unittest

HAPROXY_HOST = 'localhost'
HAPROXY_PORT = 8080

def read_request_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

class test(unittest.TestCase):
    def test1(self):
        try:
            # Connect to socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HAPROXY_HOST, HAPROXY_PORT))

            # Read request from file
            attack = read_request_from_file('attack1.txt').replace(b'\n', b'\r\n')

            # Send request
            sock.sendall(attack)
            
            response1 = sock.recv(4096)

            # Send victim request
            time.sleep(0.2) # Sleep to simulate the actual attack
            victim = b"GET /public HTTP/1.1\r\nHost: localhost:8080\r\nAuthorization: Basic YWRtaW46YWRtaW4xMjM=\r\n\r\n"
            sock.sendall(victim)
            
            response2 = sock.recv(4096)

            # Close socket
            sock.close()

            self.assertTrue(b"Transfer-Encoding: chunked" in attack)
            self.assertTrue(b"Content-Length:" in attack)
            self.assertTrue(b"Admin access granted!" in response2)
            print("TASK 2.1 ATTACK RESPONSE:")
            print('=' * 60)
            print(response1.decode('utf-8', errors='ignore')[:300])
            print()
            print("TASK 2.1 VICTIM RESPONSE:")
            print('=' * 60)
            print(response2.decode('utf-8', errors='ignore')[:300])
            print()
        except Exception as e:
            print(f"Error: {e}")
            print("TASK 2.1 ATTACK RESPONSE:")
            print('=' * 60)
            print(response1.decode('utf-8', errors='ignore')[:300])
            print()
            print("TASK 2.1 VICTIM RESPONSE:")
            print('=' * 60)
            print(response2.decode('utf-8', errors='ignore')[:300])
            print()
            self.assertTrue(False)

    def test2(self):
        try:     
            # Connect to socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HAPROXY_HOST, HAPROXY_PORT))

            # Read request from file
            attack = read_request_from_file('attack2.txt').replace(b'\n', b'\r\n')

            # Send request
            sock.sendall(attack)
            
            response1 = sock.recv(4096)

            # Send victim request
            time.sleep(0.2) # Sleep to simulate the actual attack
            victim = b"GET /public HTTP/1.1\r\nHost: localhost:8080\r\nAuthorization: Basic YWRtaW46YWRtaW4xMjM=\r\n\r\n"
            sock.sendall(victim)
            
            response2 = sock.recv(4096)

            # Close socket
            sock.close()

            self.assertTrue(b"Transfer-Encoding: chunked" in attack)
            self.assertTrue(b"Content-Length:" in attack)
            self.assertTrue(b"admin user has been deleted!" in response2)
            print("TASK 2.2 ATTACK RESPONSE:")
            print('=' * 60)
            print(response1.decode('utf-8', errors='ignore')[:300])
            print()
            print("TASK 2.2 VICTIM RESPONSE:")
            print('=' * 60)
            print(response2.decode('utf-8', errors='ignore')[:300])
            print()
        except Exception as e:
            print(f"Error: {e}")
            print("TASK 2.2 ATTACK RESPONSE:")
            print('=' * 60)
            print(response1.decode('utf-8', errors='ignore')[:300])
            print()
            print("TASK 2.2 VICTIM RESPONSE:")
            print('=' * 60)
            print(response2.decode('utf-8', errors='ignore')[:300])
            print()
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()