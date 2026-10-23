# import socket
 
# name = socket.gethostname()
# ip = socket.gethostbyname(name)
# print("Компьютер:", name)
# print("IP-адрес:", ip)
# #Вот результат 
# # Компьютер: DESKTOP-0FLCGPM
# # IP-адрес: 192.168.1.158

# import socket
 
# sites = ["python.org", "yandex.ru","","sql-academy.org","skillbox.ru"]
# for site in sites:
#     print(site, "-", socket.gethostbyname(site))

# Вот результат 
# python.org - 151.101.128.223
# yandex.ru - 77.88.44.55
#  - 0.0.0.0
# sql-academy.org - 31.129.44.124
# skillbox.ru - 185.65.148.253

import socket
 
host = "python.org"
port = 81
 
try:
    with socket.create_connection((host, port), timeout=3):
        print(f"Порт {port} на {host} открыт")
except OSError:
    print(f"Порт {port} на {host} недоступен")

# Вот результат:
# Порт 443 на python.org открыт

# Вот результат если port = 80:
# Порт 80 на python.org открыт

# Вот результат если port = 81:
# Порт 81 на python.org недоступен
