#1. Створіть функцію, яка обчислює факторіал числа. Запустіть декілька задач, що
# використовуватимуть
# ThreadPoolExecutor. Виміряти швидкість обчислень. Зробіть теж саме, використовуючи ProcessPoolExecutor.
# Додайте у програму код, який порівнює швидкість обчислень і виводить на друк найоптимальніший метод.

import concurrent.futures
import time
import math

def factorial_number(x):
   print(math.factorial(x))


if __name__ == '__main__':
    start_time = time.process_time()
    x=20000
    factorial_number(x)
    print('Sequential Execution in %s seconds' % (time.process_time() - start_time))

    start_time = time.process_time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
         x=20000
         executor.submit(factorial_number, x)
    print('Thread Pool Execution in %s seconds' % (time.process_time() - start_time))
    start_time = time.process_time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        x = 20000
        executor.submit(factorial_number, x)
    print('Process Pool Execution in %s seconds' % (time.process_time() - start_time))

#2.РОзробіть сокет сервер з використанням бібіліотеки asyncio. Сервер повинен приймати два числа і
# проводити над ними прості арифметичні функції - додавання, віднімання, множення - з використанням
# користувацьких функцій, які працюватимуть у асинхронному режимі

# Code for server
import asyncio


async def fun1(a, b):
    print(a + b)
    await asyncio.sleep(3)
    print('fun1 додавання')


async def fun2(a, b):
    print(a - b)
    await asyncio.sleep(3)
    print('fun2 віднімання')


async def fun3(a, b):
    print(a * b)
    await asyncio.sleep(3)
    print('fun2 множення')


async def task(a,b):
    task1 = asyncio.create_task(fun1(a, b))
    task2 = asyncio.create_task(fun2(a, b))
    task3 = asyncio.create_task(fun3(a, b))

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")
    a,b=map(int,message.split())

    # data1 = await task(a, b)
    writer.write(await task(a, b))
    await writer.drain()

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)


    async with server:
        await server.serve_forever()

asyncio.run(main())

#Code for client
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()