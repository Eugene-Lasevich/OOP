import user
from tkinter import *
from tkinter import ttk

from server_window import ServerWindow
from authentication import Authentication
from authentication import Registration
from tkinter.messagebox import showerror

server_host = ""
server_port = 0

client_host = ""
client_port = 0

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
    global server_host
    global server_port
    server_host = host
    server_port = port
    user1.became_server(host, int(port), ServerWindow())


def click_became_client_btn():
    a = Authentication("Enter your address")
    a.wait_window()
    client_host, client_port = a.return_data()
    if client_host != server_host or client_port != server_port:
        user1.became_client(client_host, int(client_port))
        a = Authentication("Enter address of server")
        a.wait_window()
        host, port = a.return_data()
        user1.connect(host, int(port))
    else:
        showerror(title="Mistake", message="Client and server address must not match")


def click_request_users_btn():
    pass


username_label = ttk.Label(text=f"Username: {name}", font=20)
became_server_btn = ttk.Button(text="Became a server", command=click_became_server_btn)
became_client_btn = ttk.Button(text="Became a client", command=click_became_client_btn)
request_users_btn = ttk.Button(text="Request users", command=click_request_users_btn)

username_label.place(relx=0.05, rely=0.01, width=200, height=25)
became_server_btn.place(relx=0.05, rely=0.3, width=200, height=25)
became_client_btn.place(relx=0.5, rely=0.3, width=200, height=25)
# request_users_btn.place(relx=0.05, rely=0.5, width=200, height=25)

root.mainloop()
