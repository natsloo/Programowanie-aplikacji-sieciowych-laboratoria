def zad1():
    source = input("Text file to copy:\n> ") # python3 nie ma raw_input()
    dest = "lab1zad1.txt"

    with open(source, 'r') as src, open(dest, 'w') as dst:
        for line in src:
            dst.write(line)
    
    # słowo kluczowe with dba o to, żeby pliki zostały automatycznie zamknięte 
    # po zakończeniu operacji, nawet jeśli po drodze wystąpi błąd

    # r - read (domyślnie)
    # w - write; jeśli plik dest istnieje czyści jego zawartość przed zapisem

def zad2():
    source = input("Image to copy:\n> ")
    dest = "lab1zad1.png"

    with open(source, 'rb') as src, open(dest, 'wb') as dst:
        while True:
            byte = src.read(1)
            if not byte:
                break
            dst.write(byte)
    
    # b - binary mode

def zad3():
    import ipaddress as ipa
    text = input("IP address:\n> ")
    try:
        ip = ipa.ip_address(text)
        print("%s is a correct IPv%s address." % (text, ip.version))
    except ValueError:
        print("%s is not a correct IP address." % (text))

def zad4():
    import socket, sys
    if len(sys.argv) != 2:
        print("Usage: python lab1.py <IP>")
    else:
        ip = sys.argv[1]
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            print("Hostname of %s: %s" % (ip, hostname))
        except socket.herror:
            print("Can't find hostname of %s" % (ip))
        except socket.gaierror:
            print("Incorrect IP address")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # sys.argv to lista, która zawiera przekazane z linii komand argumenty
    # gethostbyaddr() zwraca hostname dla danego adresu IP

def zad5():
    import socket, sys
    if len(sys.argv) != 2:
        print("Usage: python lab1.py <hostname>")
    else:
        hostname = sys.argv[1]
        try:
            _, _, ip = socket.gethostbyname_ex(hostname)
            print("IP of %s:" % (hostname))
            for i in ip:
                print("\t > %s" % (i))
        except socket.herror:
            print("Can't find IP of %s" % (ip))
        except socket.gaierror:
            print("Incorrect hostname")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    # gethostbyname_ex() zwraca wszystkie IPv4 przypisane do danego hosta

def zad6():
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

        # create_connection() tworzy połączenie TCP na adresie z krotki (host, port) i ustawia timeout na 7s
        # host nie musi być IP, może być nazwą
        # with dba tutaj o zamknięcie gniazda po zakończonym połączeniu
        # getpeername() zwraca adres zdalny - dla IPv4 krotka (IP, port) - do którego gniazdo jest podłączone

def zad7():
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
                open_ports.append(port)
            else:
                print(f"Port {port:5} CLOSED")
        print("-" * 10)
        print(f"Scan finished. Open ports found: {len(open_ports)}")

    # zamiana nazwy hosta na IP za pomocą gethostbyname()
    # skanowanie najpopularniejszych portów:
    # dla każdego portu socket(socket.AF_INET, socket.SOCK_STREAM) tworzy gniazdo IPv4 dla protokołu TCP
    # ustawiamy timeout na 1s
    # metoda connect_ex() próbuje nawiązać połączenie z podanym adresem i zwraca 0, jeśli port jest otwarty lub inną liczbę, jeśli nie jest

def main():
    zad7()

if __name__ == '__main__':
    main()