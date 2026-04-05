import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4013

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def time_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            s.bind((HOST, PORT))
            s.listen()
            print(f"[{get_now()}] TCP Time Server is waiting for incoming connections on port {PORT}...")
            while True:
                client, address = s.accept()
                with client:
                    print(f"[{get_now()}] Client {address} connected.")
                    data = client.recv(4096)
                    if data:
                        print(f"[{get_now()}] Client sent: {data.decode().strip()}.")
                        current_time = get_now()
                        client.sendall(current_time.encode())
                        print(f"[{get_now()}] Sending client: {current_time}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    time_server()