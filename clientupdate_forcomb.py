import socket

# Connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

# Receive server's question
question = client_socket.recv(1024).decode()
print("Server:", question)

# Send mode choice
mode_choice = input("Your choice (y/n): ")
client_socket.sendall(mode_choice.encode())

while True:
    message = input("Client: ")
    client_socket.sendall(message.encode())

    if message.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()

    if reply.lower() == "exit":
        print("Server has exited the chat.")
        break

    print("Server:", reply)

client_socket.close()
print("Chat closed.")
