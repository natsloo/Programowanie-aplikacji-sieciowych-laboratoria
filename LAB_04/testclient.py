import socket


def clientTCP():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 4014))
            s.send("hello :)".encode())
            time = s.recv(4096)
            print("Server replied:", time.decode('utf-8').strip())
        except Exception as e:
            print(f'Error connecting: {e}')


def clientUDP():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            address = ('127.0.0.1', 4019)
            s.sendto("1234".encode(), address)
            time = s.recv(4096)
            print("Server replied:", time.decode('utf-8').strip())
        except Exception as e:
                print(f'Error connecting: {e}')


def TCP2():
    MAX_LEN = 20
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 4020))
            msg = "hello :)".ljust(MAX_LEN).encode()
            s.sendall(msg)
            response = b""
            while len(response) < MAX_LEN:
                chunk = s.recv(MAX_LEN - len(response))
                if not chunk:
                    break
                response += chunk
            print("Server replied:", response.decode('utf-8').strip())
        except Exception as e:
            print(f'Error connecting: {e}')


def syntax_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            address = ('127.0.0.1', 4022)
            #s.sendto("zad13odp;src;60788;dst;2901;data;28".encode(), address)
            #s.sendto("zad14odp;src;60788;dst;2901;data;programming in python is fun".encode(), address)
            s.sendto("zad15odpA;ver;4;srcip;212.182.24.27;dstip;192.168.0.2;type;6".encode(), address)
            s.sendto("zad15odpA;srcport;2009;dstport;47526;data;network programming is fun".encode(), address)
            reply = s.recv(4096)
            print("Server replied:", reply.decode('utf-8').strip())
        except Exception as e:
                print(f'Error connecting: {e}')

if __name__ == "__main__":
    syntax_client()
