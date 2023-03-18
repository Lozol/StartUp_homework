import socket

new_socket=socket.socket()
new_socket.bind(("127.0.0.1",50))
new_socket.listen(10)
print('Server launched. ')
name= input('Input your name: ')

conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()
print(client+'connected')

while True:
    message = input('Me: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message=message.decode()
    print(client,':',message)



# import socket
#
# new_socket=socket.socket()
# new_socket.bind(("127.0.0.1",50))
# new_socket.listen()
# print('Server launched.')
# name= input('Input your name: ')
#
# client, add = new_socket.accept()
#
# flag = True
# while flag:
#     message=client.recv(1024).decode('UTF-8')
#     if message==quit:
#         flag = False
#     else:
#         print(message)
#     client.send(input('Server: ').encode('UTF-8'))

