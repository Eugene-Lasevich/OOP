from my_socket import *
import threading

UDP_MAX_SIZE = 65535


class Server:
    def __init__(self, host: str = '127.0.0.1', port: int = 3000):
        self.host = host
        self.port = port
        self.members = {}
        self.my_socket = MySocket()
        self.my_socket.my_bind(host, port)

    def run(self):
        print(f'Listening at {self.host}:{self.port} \n')
        while True:
            msg, addr = self.my_socket.my_recvfrom(1024)

            if addr not in self.members:
                self.members.setdefault(msg[1], addr)

            if not msg:
                continue

            msg_text = msg[0]
            if msg_text == '__join':
                print(f'Client: {msg[1]} joined chat')
                continue

            if msg_text == '__members':
                print(f'Client: {msg[1]} requsted members')

                active_members = [(m, v) for m, v in self.members.items() if m != msg[1]]
                self.my_socket.my_sendto(dict(active_members), addr)
                continue

            if msg_text == "__exit":
                print(f'Client: {msg[1]} leave chat')
                self.members.pop(msg[1])

    def start_run(self):
        self.run_thread = threading.Thread(target=self.run)
        self.run_thread.start()
