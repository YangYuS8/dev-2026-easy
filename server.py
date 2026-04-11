import socket
from protocol import handle_message


HOST = "127.0.0.1"
PORT = 9090


def run_server(host: str = HOST, port: int = PORT) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, _addr = server.accept()
            with conn:
                data = conn.recv(1024)
                if not data:
                    continue
                message = data.decode("utf-8").strip()
                response = handle_message(message)
                conn.sendall((response + "\n").encode("utf-8"))


if __name__ == "__main__":
    run_server()
