import socket

SERVER_ADDRESS = ('localhost', 15253)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(input('Me: ').encode('UTF-8'))
data = client.recv(4096)
print(data.decode("UTF-8"))