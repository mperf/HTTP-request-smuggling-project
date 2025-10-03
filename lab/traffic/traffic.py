import base64
import time
import requests

BASE_URL = "http://proxy:9000"

def run_every_second(*funcs):
    while True:
        for func in funcs:
            time.sleep(0.5)
            func()


def log_response(endpoint, status_code, reason, type):
    with open("request_log.txt", "w") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {endpoint} - {status_code} {reason} - {type}\n")

def admin_request():
    username = "admin"
    password = "admin123"
    auth = f"{username}:{password}"
    auth_b64 = base64.b64encode(auth.encode()).decode()
    # New session for every request
    with requests.Session() as session:
        response = session.get(f"{BASE_URL}/admin", headers={"Authorization": f"Basic {auth_b64}"})
    log_response("/admin", response.status_code, response.reason, "ADMIN")

def user_request():
    username = "user1"
    password = "user123"
    auth = f"{username}:{password}"
    auth_b64 = base64.b64encode(auth.encode()).decode()
    # New session for every request
    with requests.Session() as session:
        response = session.get(f"{BASE_URL}/public", headers={"Authorization": f"Basic {auth_b64}"})
    log_response("/public", response.status_code, response.reason, "USER")

time.sleep(5)  # Wait for services to be up
run_every_second(admin_request, user_request)