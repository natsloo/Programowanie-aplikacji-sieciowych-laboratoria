import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4014

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            s.bind((HOST, PORT))
            s.listen()
            print(f"[{get_now()}] TCP Echo Server is waiting for incoming connections on port {PORT}...")
            while True:
                client, address = s.accept()
                with client:
                    print(f"[{get_now()}] Client {address} connected.")
                    data = client.recv(4096)
                    if data:
                        print(f"[{get_now()}] Client sent: {data.decode().strip()}.")
                        client.sendall(data)
                        print(f"[{get_now()}] Sending client: {data}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    server()