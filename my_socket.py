import pickle
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SOCK_DGRAM


class MySocket(socket):

    def __init__(self, sock=None):
        super().__init__()
        if sock is None:
            self.sock = socket(AF_INET, SOCK_DGRAM)
        else:
            self.sock = sock

    def my_connect(self, host, port):
        self.sock.connect((host, port))

    def my_bind(self, host, port):
        self.sock.bind((host, port))

    def my_listen(self):
        self.sock.listen()

    def my_accept(self):
        client_sock, client_addr = self.sock.accept()
        return MySocket(client_sock), client_addr

    def my_send(self, data):
        serialized_data = pickle.dumps(data)
        self.sock.sendall(serialized_data)

    def my_recv(self, bufsize):
        serialized_data = self.sock.recv(bufsize)
        if len(serialized_data) == 0:
            return
        data = pickle.loads(serialized_data)
        return data

    def my_recvfrom(self, bufsize):
        tmp, t = self.sock.recvfrom(bufsize)
        data = pickle.loads(tmp)
        return data, t

    def my_sendto(self, data, addr):
        serialized_data = pickle.dumps(data)
        self.sock.sendto(serialized_data, addr)

    def my_getsockname(self):
        return self.sock.getsockname()

    def my_close(self):
        self.sock.close()

    # def __del__(self):
    #     self.sock.close
    #     print("Socker was deleted")
