import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.220.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(conn):
    print(f"Connection Established with Server..{SERVER}")
    while True:
        print("[YOUR MESSAGE]: ")
        msg_input = str(input().casefold())
        if msg_input is "":
            pass
        message = msg_input.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        if msg_input == 'quit':
            message = DISCONNECT_MESSAGE.encode(FORMAT)
            conn.send(send_length)
            conn.send(message)
            print("message sent to server "+ DISCONNECT_MESSAGE)
            break
        conn.send(send_length)
        conn.send(message)
        print("Waiting for Response......")
        print(f"[SERVER MESSAGE] :", conn.recv(2048).decode(FORMAT))

    conn.close()


def connect_server():
    thread = threading.Thread(target=send(client))
    thread.start()


connect_server()

# send(DISCONNECT_MESSAGE)
