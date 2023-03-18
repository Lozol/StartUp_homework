import socket

SERVER_ADDRESS = ("127.0.0.1",50)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(input('Me: ').encode('UTF-8'))
data = client.recv(4096)
print(data.decode("UTF-8"))


