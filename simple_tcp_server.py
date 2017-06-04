import socket

# Inisiasi socket tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding ke ip port
sock.bind(('', 4444))

# Listen 10 3 way handshake
sock.listen(10)

while True:
    # Accept permintaan 3 way handshake
    conn, addr = sock.accept()
    print addr
    # Receive data dari client

    data = conn.recv(10)

    data = "OK " + data
    conn.send(data)

    conn.close()
