def zad1():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect(('time.nist.gov', 13)) # serwer z zadania nie działa
                time = s.recv(1024)
                print(time.decode('utf-8').strip())
            except Exception as e:
                print(f'Error connecting: {e}')
    
    # AF_INET = IPv4
    # AF_INET6 = IPv6
    # SOCK_STREAM = TCP
    # SOCK_DGRAM = UDP

def zad2():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect(('127.0.0.1', 2900)) 
                s.send('hello'.encode())
                data = s.recv(4096)
                if data:
                    print(f'The server has replied: {data.decode('utf-8').strip()}')
            except Exception as e:
                print(f'Error connecting: {e}')

def zad3():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2900))
            while ((data := input('Enter data to send: ')) != "end"):
                s.send(data.encode())
                response = s.recv(4096)
                if response:
                    print(f'The server has replied: {response.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad4():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2901))
            s.send('hi'.encode())
            data = s.recv(4096)
            if data:
                    print(f'The server has replied: {data.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad5():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2901))
            while ((data := input('Enter data to send: ')) != "end"):
                s.send(data.encode())
                response = s.recv(4096)
                if response:
                    print(f'The server has replied: {response.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad6():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2902))
            num1 = input('Enter a number: ')
            s.send(num1.encode())
            operator = input('Enter an operator: ')
            s.send(operator.encode())
            num2 = input('Enter another number: ')
            s.send(num2.encode())
            data = s.recv(4096)
            if data:
                    print(f'The server has replied: {data.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad7():
    import socket, sys
    if len(sys.argv) != 3:
        print("Usage: python lab1.py <IP/hostname> <port>")
    else:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            with socket.create_connection((host, port), timeout=7) as s:
                print("Connected with %s on port %s successfully!" % (host, port))
                peername = s.getpeername()
                print(f"Peer name: {peername}")
                print("Service on port %s: %s." % (port, socket.getservbyport(port, 'tcp'))) 
        except ValueError:
            print("Port must be a number.")
        except socket.timeout:
            print("Connection timed out.")
        except ConnectionRefusedError:
            print("Host refused the connection.")
        except socket.gaierror:
            print("Incorrect hostname/IP.")
        except Exception as e:
            print(f"Unexpected error: {e}")

def zad8():
    import socket, sys
    if len(sys.argv) != 2:
        print("Usage: python lab1.py <hostname/IP>")
    else:
        hostname = sys.argv[1]
        try:
            ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            print("Incorrect hostname")
            return
        print("-" * 10)
        print(f"Scanning host {hostname}.")
        print("-" * 10)
        popular_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]
        open_ports = []
        for port in popular_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port:5} OPEN")
                print(f'Service: {socket.getservbyport(port, 'tcp')}')
                open_ports.append(port)
            else:
                print(f"Port {port:5} CLOSED")
        print("-" * 10)
        print(f"Scan finished. Open ports found: {len(open_ports)}")

def zad9():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2906))
            ip = input('Enter an IP adress: ')
            s.send(ip.encode())
            data = s.recv(4096)
            if data:
                    print(f'The server has replied: {data.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad10():
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2907))
            ip = input('Enter a hostname adress: ')
            s.send(ip.encode())
            data = s.recv(4096)
            if data:
                    print(f'The server has replied: {data.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad11():
    import socket
    MAX_LEN = 20
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect(('127.0.0.1', 2908))
                message = input('Enter a message: ')
                formatted = message[:MAX_LEN].ljust(MAX_LEN)
                print(f'Sending message: "{formatted}".')
                s.send(formatted.encode())
                data = s.recv(4096)
                if data:
                    print(f'The server has replied: "{data.decode('utf-8')}"')
            except Exception as e:
                print(f'Error connecting: {e}')

    # najpierw slicing - bierzemy wszystko od początku do MAX_LEN
    # jeśli jest mniej znaków - wejdą wszystkie, które są
    # jeśli jest więcej - wejdzie pierwsze MAX_LEN (20) znaków
    # potem ljust() - left justify
    # ljust() sprawdza, ile znaków brakuje do MAX_LEN i wstawia tyle spacji

def zad12():
    import socket
    MAX_LEN = 20
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect(('127.0.0.1', 2908))
                message = input('Enter a message: ')
                formatted = message[:MAX_LEN].ljust(MAX_LEN)
                print(f'Sending message: "{formatted}".')
                data_to_send = formatted.encode()

                total_sent = 0
                while total_sent < MAX_LEN:
                    sent = s.send(data_to_send[total_sent:])
                    if sent == 0:
                        raise RuntimeError('Connection is broken.')
                    total_sent += sent

                full_message = []
                total_received = 0
                while total_received < MAX_LEN:
                    message = s.recv(MAX_LEN - total_received)
                    if message == b'':
                        raise RuntimeError('Connection is broken.')
                    full_message.append(message)
                    total_received += len(message)

                print(f'The server has replied: "{b''.join(full_message).decode('utf-8')}"')

            except Exception as e:
                print(f'Error connecting: {e}')
            

def main():
    zad1()

if __name__ == '__main__':
    main()
