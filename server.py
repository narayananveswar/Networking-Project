import socket
import threading
import threading

PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
DISCONNECT_MESSAGE = "!QUIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        msg = conn.recv(1024)
        if msg:
            msg = msg.decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}], {msg}")

    conn.close()
        

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        t1 = threading.Thread(target=handleClient, args=(conn, addr))
        t1.start()
        print(f"[ACTIVE CLIENTS] {threading.active_count()-1}")


print("[STARTING].....")
start()
