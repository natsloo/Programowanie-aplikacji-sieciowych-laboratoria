import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4020
MAX_LEN = 20

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((HOST, PORT))
            s.listen(5)
            print(f"[{get_now()}] TCP Echo Server is waiting for incoming connections on port {PORT}...")
            while True:
                client, address = s.accept()
                print(f"[{get_now()}] Client {address} connected.")
                full_msg = b""
                while len(full_msg) < MAX_LEN:
                    chunk = client.recv(MAX_LEN - len(full_msg))
                    if not chunk:
                        break
                    full_msg += chunk
                if len(full_msg) == MAX_LEN:
                    sent = full_msg.decode().strip()
                    print(f"[{get_now()}] Client sent: {sent}.")
                    response = sent.ljust(MAX_LEN).encode()
                    client.sendall(response)
                    print(f"[{get_now()}] Sending client: {sent.encode()}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    server()