import threading
import time
from my_socket import *
import message
import queue


class Client:
    UDP_MAX_SIZE = 65535

    def __init__(self, username: str, host: str = '127.0.0.1', port: int = 3000):
        self.host = host
        self.port = port
        self.username = username
        self.my_socket = MySocket()
        self.my_socket.my_bind(host, port)
        # self.own_port = self.my_socket.my_getsockname()[1]
        self.listen_thread = None
        self.sendto = None
        self.allowed_ports = [port]
        self.data_from_server = None
        self.window = None
        self.my_queue = queue.Queue()

    def listen(self):
        while True:
            msg, addr = self.my_socket.my_recvfrom(self.UDP_MAX_SIZE)
            self.data_from_server = msg
            self.my_queue.put(str(msg))

            msg_port = addr[-1]
            allowed_ports = self.listen_thread.allowed_ports
            if msg_port not in allowed_ports:
                continue

            if not msg:
                continue

            else:
                self.my_queue.put(str(msg))
                print('\r\r' + str(msg) + '\n' + f'you: ', end='')

    def start_listen(self):
        self.listen_thread = threading.Thread(target=self.listen, daemon=True)
        self.listen_thread.allowed_ports = self.allowed_ports
        self.listen_thread.start()

    def connect(self, host: str, port: int):
        self.start_listen()
        self.my_socket.my_sendto(('__join', self.username), (host, port))
        self.sendto = (host, port)

    def get_members(self):
        self.my_socket.my_sendto(('__members', self.username), self.sendto)
        time.sleep(0.01)
        return dict(self.data_from_server)

    def send_message(self, text):
        self.my_queue.put(f"you: {text}")
        msg = message.Message(self.username, text)
        self.my_socket.my_sendto(msg, self.sendto)

    def connect_by_name(self, username: str):

        self.get_members()
        time.sleep(0.001)
        if dict(self.data_from_server).get(username):
            addr = dict(self.data_from_server).get(username)
            host = addr[0]
            port = addr[1]
            peer_port = port
            self.allowed_ports.append(peer_port)
            self.sendto = (host, peer_port)
            print(f'Connect to client: {username}')
        else:
            print(f'Failed to connect')



    def find_username_port(self, port: int):
        b = self.get_members()
        a = dict(self.data_from_server)
        for key, val in a.items():
            if val[1] == port:
                return key

    def disconect_from_client(self):

        # peer_port = self.sendto[-1]
        # self.find_username_port(peer_port)
        # self.allowed_ports.remove(peer_port)
        self.sendto = ("127.0.0.1", 3000)
        # self.listen_thread.join()
        # print(f'Disconnect from client:{self.find_username_port(peer_port)}')
