import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4016

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def math_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[{get_now()}] UDP Math Server is waiting for incoming connections on port {PORT}...")
        try:
            while True:
                data1, address = s.recvfrom(4096)
                op, _ = s.recvfrom(4096)
                data2, _ = s.recvfrom(4096)
                print(f"[{get_now()}] Client {address} connected.")
                if data1 and data2 and op:
                    num1 = float(data1.decode().strip())
                    opp = op.decode().strip()
                    num2 = float(data2.decode().strip())
                    print(f"[{get_now()}] Client sent: {num1, opp, num2}.")
                    match opp:
                        case '+':
                            result = num1 + num2
                        case '-':
                            result = num1 - num2
                        case '*':
                            result = num1 * num2
                        case '/':
                            result = num1 / num2
                        case _:
                            result = "Unknown operator, can't calculate."
                    s.sendto(str(result).encode(), address)
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    math_server()