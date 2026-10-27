#!/usr/bin/env python3
import http.server
import socket
import socketserver
import os
import sys

PORT = 8080

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_ip()
    url = f"http://{local_ip}:{PORT}"
    
    print("\n" + "="*56)
    print(" 🥑 7 KUNLIK PARHEZ - MOBIL SERVER ISHGA TUSHDI")
    print("="*56)
    print(f"\n📱 Telefoningiz brauzerida quyidagi manzilni oching:")
    print(f"👉 \033[1;32m{url}\033[0m")
    print(f"\n💻 Kompyuterda ochish uchun:")
    print(f"👉 \033[1;34mhttp://localhost:{PORT}\033[0m")
    print("\n💡 Eslatma: Telefoningiz ham shu Wi-Fi tarmog'iga ulangan bo'lishi kerak.")
    print("To'xtatish uchun: Ctrl + C bosing.\n" + "="*56 + "\n")

    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer to'xtatildi.")
            sys.exit(0)

if __name__ == "__main__":
    main()
