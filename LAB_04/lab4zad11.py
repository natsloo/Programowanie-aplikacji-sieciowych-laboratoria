import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4022

def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def checkA(text):
    parts = text.split(";")
    if len(parts) != 9:
        return "BAD_SYNTAX"
    
    try:
        if parts[0] == "zad15odpA" and parts[1] == "ver" and parts[3] == "srcip" and parts[5] == "dstip" and parts[7] == "type":
            ver = int(parts[2])
            srcip = parts[4]
            dstip = parts[6]
            proto_type = int(parts[8])
            
            if ver == 4 and proto_type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"
    except Exception:
        return "BAD_SYNTAX"

def checkB(text):
    parts = text.split(";")
    if len(parts) != 7:
        return "BAD_SYNTAX"
    
    try:
        if parts[0] == "zad15odpB" and parts[1] == "srcport" and parts[3] == "dstport" and parts[5] == "data":
            srcport = int(parts[2])
            dstport = int(parts[4])
            data_content = parts[6]

            if srcport == 2900 and dstport == 47526 and data_content == "network programming is fun":
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
        print(f"[{get_now()}] UDP Echo Server is waiting for incoming connections on port {PORT}...")
        try:
            while True:
                data, address = s.recvfrom(4096)
                print(f"[{get_now()}] Client {address} connected.")
                if data:
                    sent = data.decode().strip()
                    print(f"[{get_now()}] Client sent: {sent}.")
                    parts = sent.split(";")
                    if parts[0] == "zad15odpA":
                        reply = checkA(sent)
                    elif parts[0] == "zad15odpB":
                        reply = checkB(";")
                    else:
                        reply = "BAD_SYNTAX"
                    s.sendto(reply.encode(), address)
                    print(f"[{get_now()}] Sending client: {reply.encode()}.")
                print(f"[{get_now()}] Client disconnected.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    server()