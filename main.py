import time

import server_window
import user
from tkinter import *
from tkinter import ttk
import threading

from server_window import ServerWindow
from server_window import ChatWindow
from authentication import Authentication
from authentication import Registration
from tkinter.messagebox import showerror

server_host = ""
server_port = 0

client_host = ""
client_port = 0

reg = Registration()
name = reg.get_name()
if name:
    user1 = user.User(name)
else:
    exit(0)

a = Authentication("Enter your address")
a.wait_window()
client_host, client_port = a.return_data()
if (client_host != server_host or client_port != server_port) and not user1.is_client():
    user1.became_client(client_host, int(client_port))
    user1.connect("127.0.0.1", 3000)

root = Tk()
root.title("MainWindow")
root.geometry("500x500")


# def click_became_server_btn():
#     a = Authentication()
#     a.wait_window()
#     host, port = a.return_data()
#     global server_host
#     global server_port
#     server_host = host
#     server_port = port
#     if server_port and server_host and not user1.is_server():
#         user1.became_server(host, int(port), ServerWindow("Server Window"))
#     else:
#         print("EEEEEEEEEEr")


def click_became_client_btn():
    a = Authentication("Enter your address")
    a.wait_window()
    client_host, client_port = a.return_data()
    if (client_host != server_host or client_port != server_port) and not user1.is_client():
        user1.became_client(client_host, int(client_port))
        a = Authentication("Enter address of server")
        a.wait_window()
        host, port = a.return_data()
        user1.connect(host, int(port))
        request_users_btn.place(relx=0.05, rely=0.5, width=200, height=25)
    else:
        showerror(title="Mistake", message="Client and server address must not match")


def click_request_users_btn():
    sw = server_window.ServerWindow("Users")
    sw.append_text(user1.request_users())


def click_connect_users_btn():
    if not username_editor.get():
        a = Authentication()
        a.host_editor.delete(0, END)
        a.port_editor.delete(0, END)
        a.wait_window()
        host, port = a.return_data()
        user1.connect(host, int(port))
    else:
        users: dict = user1.request_users()
        if users.get(username_editor.get()):
            host, port = users.get(username_editor.get())
            user1.connect(host, int(port))
        else:
            print("qwqqqqqqqqqqqqq")


chat_window: ChatWindow


def click_start_chat_btn():
    global chat_window
    chat_window = ChatWindow(user1.client)
    chat_window.mainloop()
    print(chat_window)




username_label = ttk.Label(text=f"Username: {name}", font=20)
# became_server_btn = ttk.Button(text="Became a server", command=click_became_server_btn)
became_client_btn = ttk.Button(text="Became a client", command=click_became_client_btn)
request_users_btn = ttk.Button(text="Request users", command=click_request_users_btn)
connect_user_btn = ttk.Button(text="Connect", command=click_connect_users_btn)
username_editor = ttk.Entry(font=30)
start_chat_btn = ttk.Button(text="Start chat", command=click_start_chat_btn)

username_label.place(relx=0.05, rely=0.01, width=200, height=25)
# became_server_btn.place(relx=0.05, rely=0.3, width=200, height=25)
became_client_btn.place(relx=0.5, rely=0.3, width=200, height=25)
request_users_btn.place(relx=0.05, rely=0.5, width=200, height=25)
connect_user_btn.place(relx=0.05, rely=0.7, width=200, height=25)
username_editor.place(relx=0.5, rely=0.7, width=200, height=25)
start_chat_btn.place(relx=0.05, rely=0.9, width=200, height=25)


root.mainloop()
