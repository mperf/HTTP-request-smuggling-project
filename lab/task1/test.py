#!/usr/bin/env python3

import socket
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
            request = read_request_from_file('request1.txt').replace(b'\n', b'\r\n')

            # Send request
            sock.sendall(request)

            # Respons
            response = sock.recv(4096)
            
            # Close socket
            sock.close()

            self.assertTrue(b"q=smugglingab" in request)
            self.assertTrue(b"q=smuggling\"" in response)
        except Exception as e:
            # print(f"Error: {e}")
            print("TASK 1.1 SERVER RESPONSE")
            print('=' * 60)
            print(response.decode('utf-8', errors='ignore')[:300])
            print()
            self.assertTrue(False)

    def test2(self):
        try:
            # Connect to socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HAPROXY_HOST, HAPROXY_PORT))

            # Read request from file
            request = read_request_from_file('request2.txt').replace(b'\n', b'\r\n')

            # Send request
            sock.sendall(request)

            # Respons
            response = sock.recv(4096)

            # Close socket
            sock.close()

            self.assertTrue(b"Transfer-Encoding: chunked" in request)
            self.assertTrue(b"q=smugglingab" in request)
            self.assertTrue(b"q=smugglingab\"" in response)
        except Exception as e:
            print(f"Error: {e}")
            print("TASK 1.2 SERVER RESPONSE")
            print('=' * 60)
            print(response.decode('utf-8', errors='ignore')[:300])
            print()
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()