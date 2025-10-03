#!/usr/bin/env python3
"""
Smuggling Lab Server - Transparent API that forwards requests and auto-sends victim request
"""

import socket
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HAPROXY_HOST = 'haproxy'  # Docker service name
HAPROXY_PORT = 1080       # HAProxy internal port
LISTEN_PORT = 9000

class SmugglingLabHandler(BaseHTTPRequestHandler):
    """HTTP handler that forwards requests and demonstrates smuggling"""
    
    def do_POST(self):
        """Handle POST requests - forward to HAProxy and send victim request"""
        try:
            # Read the request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length) if content_length > 0 else b''
            
            # Build the raw HTTP request to forward
            raw_request = self.build_raw_request('POST', post_data)
            
            # Forward to HAProxy and get responses
            responses = self.forward_with_victim_request(raw_request)
            
            # Return all responses as JSON
            self.send_json_response(responses)
            
        except Exception as e:
            self.send_error_response(f"Error: {e}")
    
    def do_GET(self):
        """Handle GET requests - forward to HAProxy and send victim request"""
        try:
            # Build the raw HTTP request to forward
            raw_request = self.build_raw_request('GET')
            
            # Forward to HAProxy and get responses
            responses = self.forward_with_victim_request(raw_request)
            
            # Return all responses as JSON
            self.send_json_response(responses)
            
        except Exception as e:
            self.send_error_response(f"Error: {e}")
    
    def build_raw_request(self, method, body=b''):
        """Build raw HTTP request from incoming request"""
        # Start with request line
        raw = f"{method} {self.path} HTTP/1.1\r\n".encode()
        
        # Add headers
        for header, value in self.headers.items():
            if header.lower() not in ['host']:  # Skip host, we'll set our own
                raw += f"{header}: {value}\r\n".encode()
        
        # Set correct host for HAProxy
        raw += f"Host: {HAPROXY_HOST}:{HAPROXY_PORT}\r\n".encode()
        raw += b"\r\n"
        
        # Add body if present
        if body:
            raw += body
        
        return raw
    
    def forward_with_victim_request(self, attack_request):
        """Forward attack request, wait, then send victim request"""
        responses = {}
        
        try:
            # Connect to HAProxy
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HAPROXY_HOST, HAPROXY_PORT))
            
            print(f"[LAB] Forwarding attack request ({len(attack_request)} bytes)")
            print(f"[LAB] Request: {attack_request[:200]}...")
            
            # Send attack request
            sock.sendall(attack_request)
            
            # Get first response
            response1 = sock.recv(4096)
            responses['attack_response'] = {
                'data': response1.decode('utf-8', errors='ignore'),
                'length': len(response1),
                'raw_bytes': response1.hex()
            }
            print(f"[LAB] Attack response: {len(response1)} bytes")
            
            # Wait 0.2 seconds (like exploit.py)
            time.sleep(0.2)
            
            # Send victim request
            victim_request = (
                b"GET /public HTTP/1.1\r\n"
                b"Host: " + f"{HAPROXY_HOST}:{HAPROXY_PORT}".encode() + b"\r\n"
                b"Authorization: Basic YWRtaW46YWRtaW4xMjM=\r\n"
                b"User-Agent: VictimBrowser/1.0\r\n"
                b"\r\n"
            )
            
            print(f"[LAB] Sending victim request ({len(victim_request)} bytes)")
            sock.sendall(victim_request)
            
            # Get victim response
            response2 = sock.recv(4096)
            responses['victim_response'] = {
                'data': response2.decode('utf-8', errors='ignore'),
                'length': len(response2),
                'raw_bytes': response2.hex()
            }
            print(f"[LAB] Victim response: {len(response2)} bytes")
            
            sock.close()
            
        except Exception as e:
            responses['error'] = str(e)
            print(f"[LAB] Error: {e}")
        
        return responses
    
    def send_json_response(self, data):
        """Send JSON response back to client"""
        response_json = json.dumps(data, indent=2)
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_json)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(response_json.encode())
    
    def send_error_response(self, error_msg):
        """Send error response"""
        error_data = {'error': error_msg}
        self.send_json_response(error_data)
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        print(f"[LAB] {self.address_string()} - {format % args}")

def main():
    print("=" * 60)
    print("HTTP Request Smuggling Lab Server")
    print("=" * 60)
    print(f"Listening on port {LISTEN_PORT}")
    print(f"Forwarding to {HAPROXY_HOST}:{HAPROXY_PORT}")
    print("Send POST/GET requests to test smuggling attacks!")
    print("=" * 60)
    
    # Create HTTP server
    server = HTTPServer(('0.0.0.0', LISTEN_PORT), SmugglingLabHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[LAB] Shutting down...")
        server.server_close()

if __name__ == "__main__":
    main()
