import socket

keyword = "I'am server!!"
print(keyword)

server_ip = '192.168.1.29'  # Standard loopback interface address (localhost)
port = 65432        # Port to listen on (non-privileged ports are > 1023)

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.bind((server_ip, port))
    server.listen()
    print('Waiting for client...')

    client, addr = server.accept()
    print('Connect from: ',str(addr))

    data = client.recv(1024).decode('utf-8')
    print('Message from client: ', data)

    if data == '500':
        resp_text = "Sowar Lungto Team"
    elif data == '250':
        resp_text = "Anacotmai"
    else:
        resp_text = "Who are you?"

    client.send(resp_text.encode('utf-8'))
    client.close()