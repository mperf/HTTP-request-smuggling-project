#!/usr/bin/env python3

import socket
import unittest

HAPROXY_HOST = 'localhost'
HAPROXY_PORT = 8080

def read_request_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

class test(unittest.TestCase):
    def test(self):
        # Connect to socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HAPROXY_HOST, HAPROXY_PORT))

        # Read request from file
        request = read_request_from_file('solution.txt').replace(b'\n', b'\r\n')

        # Send request
        sock.sendall(request)

        # Respons
        response = sock.recv(4096)

        print(response.decode('utf-8', errors='ignore')[:300])

        # Close socket
        sock.close()

        self.assertTrue(b"200 OK" in response)

if __name__ == '__main__':
    unittest.main()