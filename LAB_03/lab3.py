def zad13():
    import socket
    DATAGRAM = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e".replace(" ", "")
    
    src_port = int(DATAGRAM[:4], 16)
    dst_port = int(DATAGRAM[4:8], 16)
    total_len_bytes = int(DATAGRAM[8:12], 16)
    data_len = total_len_bytes - 8 # 8 = 4 x 2 bajty - src_port, dst_port, len, sum
    data = bytes.fromhex(DATAGRAM[16:]).decode('ascii')
    print(src_port, dst_port, data_len, data)

    result = f"zad14odp;src;{src_port};dst;{dst_port};data;{data_len}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2909))
            s.send(result.encode())
            received = s.recv(4096)
            if received:
                print(f'The server has replied: {received.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad14():
    import socket
    SEGMENT = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29".replace(" ", "")

    src_port = int(SEGMENT[:4], 16)
    dst_port = int(SEGMENT[4:8], 16)
    header_length = int(SEGMENT[24], 16) * 4
    seg_bytes = bytes.fromhex(SEGMENT)
    total_len = len(seg_bytes)
    data_len = total_len - header_length
    data = (seg_bytes[header_length:]).decode('ascii')
    print(src_port, dst_port, data_len, data)

    result = f"zad13odp;src;{src_port};dst;{dst_port};data;{data_len}"

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2909))
            s.send(result.encode())
            received = s.recv(4096)
            if received:
                print(f'The server has replied: {received.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')

def zad15():
    import socket
    PACKET = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b" + \
            "c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1" + \
            "80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01" + \
            "00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67" \
            "72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
    PACKET = PACKET.replace(" ", "")
    ip_protocol_ver = int(PACKET[0], 16)
    ip_header_len = int(PACKET[1], 16) * 4 
    int_protocol = int(PACKET[18:20], 16)
    if int_protocol == 6:
        protocol = socket.AF_INET
    else:
        protocol = socket.AF_INET6 
    src_ip = socket.inet_ntop(protocol, bytes.fromhex(PACKET[24:32]))
    dst_ip = socket.inet_ntop(protocol, bytes.fromhex(PACKET[32:40]))

    src_port = int(PACKET[40:44], 16)
    dst_port = int(PACKET[44:48], 16)
    header_length = int(PACKET[64], 16) * 4
    packet_bytes = bytes.fromhex(PACKET)
    total_len = len(packet_bytes)
    data_len = total_len - header_length
    data = (packet_bytes[ip_header_len + header_length:]).decode('ascii')
    print(src_port, dst_port, data_len, data)

    resultA = f"zad15odpA;ver;{ip_protocol_ver};srcip;{src_ip};dstip;{dst_ip};type;{int_protocol}"
    resultB = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        try:
            s.connect(('127.0.0.1', 2911))
            s.send(resultA.encode())
            received = s.recv(4096)
            if received:
                print(f'The server has replied: {received.decode('utf-8').strip()}')
            s.send(resultB.encode())
            received = s.recv(4096)
            if received:
                print(f'The server has replied: {received.decode('utf-8').strip()}')
        except Exception as e:
            print(f'Error connecting: {e}')



def main():
    zad15()

if __name__ == '__main__':
    main()
