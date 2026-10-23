import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)

name = input("Введите имя: ")
client.sendto(name.encode("utf-8"), ("127.0.0.1", 5000))

try:
    data, addr = client.recvfrom(1024)
    print("Ответ сервера:", data.decode("utf-8"))
except (socket.timeout, ConnectionResetError):
    print("Сервер не отвечает")
finally:
    client.close()