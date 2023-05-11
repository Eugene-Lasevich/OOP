# from my_socket import *
# import threading
# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText
#
# UDP_MAX_SIZE = 65535
#
# class ServerWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Server Window")
#         self.geometry("400x300")
#
#         self.scrolled_text = ScrolledText(self)
#         self.scrolled_text.pack(fill=tk.BOTH, expand=True)
#
#     def append_text(self, text):
#         self.scrolled_text.insert(tk.END, text)
#         self.scrolled_text.see(tk.END)
#
# class Server:
#     def __init__(self, host: str = '127.0.0.1', port: int = 3000):
#         self.host = host
#         self.port = port
#         self.members = {}
#         self.my_socket = MySocket()
#         self.my_socket.my_bind(host, port)
#         self.return_message = ""
#         self.window = ServerWindow()
#
#     def run(self):
#         self.return_message = f'Listening at {self.host}:{self.port} \n'
#         print(self.return_message)
#         self.window.append_text(self.return_message)
#         while True:
#             msg, addr = self.my_socket.my_recvfrom(1024)
#
#             if addr not in self.members:
#                 self.members.setdefault(msg[1], addr)
#
#             if not msg:
#                 continue
#
#             msg_text = msg[0]
#             if msg_text == '__join':
#                 self.return_message = f'Client: {msg[1]} joined chat'
#                 print(self.return_message)
#                 self.window.append_text(self.return_message)
#
#                 continue
#
#             if msg_text == '__members':
#                 self.return_message = f'Client: {msg[1]} requsted members'
#                 self.window.append_text(self.return_message)
#
#                 print(self.return_message)
#
#                 active_members = [(m, v) for m, v in self.members.items() if m != msg[1]]
#                 self.my_socket.my_sendto(dict(active_members), addr)
#                 continue
#
#             if msg_text == "__exit":
#                 self.return_message = f'Client: {msg[1]} leave chat'
#                 self.window.append_text(self.return_message)
#
#                 print(self.return_message)
#                 self.members.pop(msg[1])
#
#     def start_run(self):
#         self.run_thread = threading.Thread(target=self.run)
#         self.run_thread.start()
#         self.window.mainloop()

from my_socket import *
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

UDP_MAX_SIZE = 65535


class ServerWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Server Window")
        self.geometry("400x300")

        self.scrolled_text = ScrolledText(self)
        self.scrolled_text.pack(fill=tk.BOTH, expand=True)

    def append_text(self, text):
        self.scrolled_text.insert(tk.END, text)
        self.scrolled_text.see(tk.END)


class Server:
    def __init__(self, host: str = '127.0.0.1', port: int = 3000, gui_window=None):
        self.host = host
        self.port = port
        self.members = {}
        self.my_socket = MySocket()
        self.my_socket.my_bind(host, port)
        self.return_message = ""
        self.window = gui_window

    def run(self):
        self.return_message = f'Listening at {self.host}:{self.port} \n'
        print(self.return_message)
        self.window.append_text(self.return_message)
        while True:
            msg, addr = self.my_socket.my_recvfrom(1024)

            if addr not in self.members:
                self.members.setdefault(msg[1], addr)

            if not msg:
                continue

            msg_text = msg[0]
            if msg_text == '__join':
                self.return_message = f'Client: {msg[1]} joined chat'
                print(self.return_message)
                self.window.append_text(self.return_message)

                continue

            if msg_text == '__members':
                self.return_message = f'Client: {msg[1]} requsted members'
                self.window.append_text(self.return_message)

                print(self.return_message)

                active_members = [(m, v) for m, v in self.members.items() if m != msg[1]]
                self.my_socket.my_sendto(dict(active_members), addr)
                continue

            if msg_text == "__exit":
                self.return_message = f'Client: {msg[1]} leave chat'
                self.window.append_text(self.return_message)

                print(self.return_message)
                self.members.pop(msg[1])

    def start_run(self):
        self.run_thread = threading.Thread(target=self.run)
        self.run_thread.start()
        self.window.mainloop()
