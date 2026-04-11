import socket

HOST = "127.0.0.1"
PORT = 9090


def send_message(message: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall((message + "\n").encode("utf-8"))
        return client.recv(1024).decode("utf-8").strip()


if __name__ == "__main__":
    print(send_message("PING"))
