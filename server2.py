import socket

SERVER_ADDRESS = ('', 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Weiting conect client...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    b = data.decode("UTF-8")
    print("Get from client:", b)
    if b == 'stop':
        print("Stop")
        break
    data = bytes(str(len(data.split())), "ascii")
    c.send(data)
    c.close()
