import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4021


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def check(text):
    parts = text.split(";")
    if len(parts) != 7:
        return "BAD_SYNTAX"

    try:
        if parts[0] == "zad13odp" and parts[1] == "src" and parts[3] == "dst" and parts[5] == "data":
            src_port = int(parts[2])
            dst_port = int(parts[4])
            data_val = parts[6]
            print(src_port, dst_port, data_val)

            if src_port == 60788 and dst_port == 2901 and data_val == "28":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"
    except Exception:
        return "BAD_SYNTAX"


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(
            f"[{get_now()}] UDP Echo Server is waiting for incoming connections on port {PORT}...")
        try:
            while True:
                data, address = s.recvfrom(4096)
                print(f"[{get_now()}] Client {address} connected.")
                if data:
                    sent = data.decode().strip()
                    print(f"[{get_now()}] Client sent: {sent}.")
                    reply = check(sent)
                    s.sendto(reply.encode(), address)
                    print(f"[{get_now()}] Sending client: {reply.encode()}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    server()
