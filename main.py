import time

import user
from tkinter import *
from tkinter import ttk

from server_window import ServerWindow
from authentication import Authentication
from authentication import Registration

reg = Registration()
name = reg.get_name()
user1 = user.User(name)

root = Tk()
root.title("MainWindow")
root.geometry("500x500")


def click_became_server_btn():
    a = Authentication()
    a.wait_window()
    host, port = a.return_data()
    user1.became_server(host, int(port), ServerWindow())


def click_became_client_btn():
    pass


def click_request_users_btn():
    pass


username_label = ttk.Label(text=f"Username: {name}", font=20)
became_server_btn = ttk.Button(text="Became a server", command=click_became_server_btn)
became_client_btn = ttk.Button(text="Became a client", command=click_became_client_btn)
request_users_btn = ttk.Button(text="Request users", command=click_request_users_btn)

username_label.place(relx=0.05, rely=0.01, width=200, height=25)
became_server_btn.place(relx=0.05, rely=0.3, width=200, height=25)
became_client_btn.place(relx=0.5, rely=0.3, width=200, height=25)
request_users_btn.place(relx=0.05, rely=0.5, width=200, height=25)

root.mainloop()
