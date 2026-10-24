import socket
import threading
 
def handle_client(conn, addr):
    print("Подключился клиент:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data.decode("utf-8").upper().encode("utf-8"))
    conn.close()
    print("Клиент отключился:", addr)
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Сервер запущен...")
 
while True:
    conn, addr = server.accept()
    handle_client(conn, addr)