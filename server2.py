import socket

SERVER_ADDRESS = ('', 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Ждём подключения клиента...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    b = data.decode("UTF-8")
    print("Получили от клиента:", b)
    if b == 'stop':
        print("Заверешение")
        break
    data = bytes(str(len(data.split())), "ascii")
    c.send(data)
    c.close()