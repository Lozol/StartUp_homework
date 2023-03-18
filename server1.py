import socket

SERVER_ADDRESS = ("127.0.0.1",50)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Чекаємо на клієнта...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    message = data.decode("UTF-8")
    print("Отримай віл клієнта питання:", message)
    if message == 'stop' or message == 'Stop':
        print("Ззвершення")
        break
    elif message == "Who?" or message == "Who" or message == "who":
        data = "You"
    elif message == "Where?" or message == "Where" or message == "where":
        data = 'There'
    elif message == "When?" or message == "When" or message == "when":
        data = 'Always'
    else:
        data = 'I dont know'
    data=bytes(data, "ascii" )
    c.send(data)
    c.close()





