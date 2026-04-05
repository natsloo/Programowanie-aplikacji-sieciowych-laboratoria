import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4015

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[{get_now()}] UDP Echo Server is waiting for incoming connections on port {PORT}...")
        try:
            while True:
                data, address = s.recvfrom(4096)
                print(f"[{get_now()}] Client {address} connected.")
                if data:
                    print(f"[{get_now()}] Client sent: {data.decode().strip()}.")
                    s.sendto(data, address)
                    print(f"[{get_now()}] Sending client: {data}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    server()