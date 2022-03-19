import threading
import socket

host = '127.0.0.1'
port = 55555 # do not choose ports from 1-10000 as they are reserved

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host, port))
server.listen()

clients = []
nicknames = []

#broadcasts from server to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

#when client connects to server, then broadcasts it to the other clients.
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# if method recieves something then server will accept the client connection
def recieve():
    while True:
        # accepts clients all the time
        client, address = server.accept()
        print(f"connected with {str(address)}")

        #send client codeword Nick to get the client.recv or the nickname from client.
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # prints nickname and then broadcasts all clients that this client joined the chat.
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start() #python threads uses start

print("Server is listening...")
recieve()

# Future edits -> Adds admin where you detect nickname admin and adds if statements to check if they're able to send commands