import socket

# Setup server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 65432))
server_socket.listen(1)

print("Server is waiting for connection on port 65432...")

client_socket, client_address = server_socket.accept()
print("Connected to", client_address)

# Ask client for mode
client_socket.sendall("Do you want echo mode? (y/n): ".encode())
echo = client_socket.recv(1024).decode().strip().lower()

while True:
    message = client_socket.recv(1024).decode()

    if message.lower() == "exit":
        print("Client has exited the chat.")
        break

    print("Client:", message)

    if echo == 'y':
        client_socket.sendall(message.encode())
    else:
        reply = input("Server: ")
        client_socket.sendall(reply.encode())
        if reply.lower() == "exit":
            break

client_socket.close()
server_socket.close()
print("Chat closed.")
