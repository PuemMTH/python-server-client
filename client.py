import socket

keyword = "I'am client!!"
print(keyword)

server_ip = '192.168.1.29'  # The server's hostname or IP address
port = 65432        # The port used by the server

while True:
    data = input("Send Message: ")
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((server_ip, port))

    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')

    print("Data from Server: ", data_server)
    server.close()