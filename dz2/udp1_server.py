import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязываем сокет к адресу и порту
server.bind(("127.0.0.1", 5000))
print("UDP-сервер ждёт сообщения...")

while True:

    data, addr = server.recvfrom(1024)
    name = data.decode("utf-8")
    print(f"Получено от {addr}: {name}")

    response = f"Привет, {name}!"
    server.sendto(response.encode("utf-8"), addr)