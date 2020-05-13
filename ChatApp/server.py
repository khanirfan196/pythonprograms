import socket
import threading

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = len(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(msg)
            if msg == "DISCONNECT":
                break
            print(f"[CLIENT MESSAGE]:  {msg}")
            print("[YOUR MESSAGE]:")
            msg_server = input()
            if msg_server is None:
                pass
            conn.send(msg_server.encode(FORMAT))
            print("Waiting for Response......")

    print("Connection is closed...")
    server.shutdown(1)
    server.close()



def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
