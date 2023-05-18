import client
import server
import time


class User():
    def __init__(self, username):
        self.username = username
        self._is_server = False
        self._is_client = False
        # self.host = host
        # self.port = port

    # def became_server(self, host, port, window=None):
    #     self.server = server.Server(host, port, window)
    #     self._is_server = True
    #     self.server.start_run()
    #     print(f"{self.username} is now a server")

    def became_client(self, host, port):
        self.client = client.Client(self.username, host, port)
        self._is_client = True
        print(f"{self.username} is now a client")

    def request_users(self):
        self.client.get_members()
        print(self.client.data_from_server)
        if self.client.data_from_server:
            return self.client.data_from_server
        else:
            return

    def connect_to_user_by_name(self, username: str):
        self.client.connect_by_name(username)

    def connect(self, host, port):
        self.client.connect(host, port)

    def disconnect(self):
        pass

    def disconnect_from_server(self):
        pass

    def is_server(self):
        return self._is_server

    def is_client(self):
        return self._is_client
