import socket
sites = ["google.com", "yandex.ru", "github.com"]

for site in sites:
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} — {ip}")
    except socket.gaierror:
        print(f"{site} — не найден (ошибка разрешения имени)")