import time
import subprocess
import server_window
import user
from tkinter import *
from tkinter import ttk
# import almost_p2p_chat.user as user

from server_window import ChatWindow
from authentication import Authentication
from authentication import Registration
from tkinter.messagebox import showerror

server_host = "127.0.0.1"
server_port = 3000

client_host = ""
client_port = 0

reg = Registration()
name = reg.get_name()
# name = "Eugene"
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
    time.sleep(0.1)
    if (user1.check_repeat_username()):
        # user1.disconnect_from_server()
        exit(0)

root = Tk()
root.title("MainWindow")
root.geometry("500x250")


def click_request_users_btn():
    sw = server_window.ServerWindow("Users")
    # sw.clear()
    sw.append_text(user1.request_users())

    def close_window():
        sw.scrolled_text.delete(0, END)
        sw.destroy()
        root.deiconify()

    sw.protocol("WM_DELETE_WINDOW", close_window)

    root.withdraw()

    sw.wait_window(sw)


connect_var = StringVar()
connect_var.set("Connect to Server")


def click_connect_users_btn():
    if not username_editor.get():
        a = Authentication()
        a.host_editor.delete(0, END)
        a.port_editor.delete(0, END)
        a.wait_window()
        host, port = a.return_data()
        if host and port:
            start_chat_btn.place(relx=0.05, rely=0.7, width=425, height=45)
            # user1.disconnect_from_server()
            user1.connect(host, int(port))
            connect_user_btn.configure(state="disabled")

        # start_chat_btn.place(relx=0.05, rely=0.7, width=425, height=45)

    else:
        users: dict = user1.request_users()
        con = username_editor.get()
        if users.get(con):
            connect_var.set(f"connect to {con}")
            # user1.disconnect_from_server()
            user1.connect_to_user_by_name(con)
            connect_user_btn.configure(state="disabled")
            start_chat_btn.place(relx=0.05, rely=0.7, width=425, height=45)
        else:
            print("qwqqqqqqqqqqqqq")


chat_window: ChatWindow


def click_start_chat_btn():
    global chat_window
    chat_window = ChatWindow(user1.client)

    def close_window():
        user1.client.disconect_from_client()
        chat_window.destroy()
        connect_user_btn.configure(state="normal")
        connect_var.set("connect to Server")
        user1.connect("127.0.0.1", 3000)
        username_editor.delete(0, "end")
        root.deiconify()

    chat_window.protocol("WM_DELETE_WINDOW", close_window)
    root.withdraw()

    chat_window.wait_window(chat_window)
    chat_window.mainloop()


username_label = ttk.Label(text=f"Username: {name}", font=25)
connect_label = ttk.Label(text=f"Connect :{connect_var}", font=25, textvariable=connect_var)

request_users_btn = ttk.Button(text="Request users", command=click_request_users_btn)
connect_user_btn = ttk.Button(text="Connect", command=click_connect_users_btn)
username_editor = ttk.Entry(font=30)
# username_editor.insert(0,   "Igor")
start_chat_btn = ttk.Button(text="Start chat", command=click_start_chat_btn)

username_label.place(relx=0.05, rely=0.01, width=200, height=35)
connect_label.place(relx=0.55, rely=0.01, width=200, height=35)

request_users_btn.place(relx=0.05, rely=0.3, width=200, height=45)
connect_user_btn.place(relx=0.05, rely=0.5, width=200, height=45)
username_editor.place(relx=0.5, rely=0.5, width=200, height=45)


# start_chat_btn.place(relx=0.05, rely=0.7, width=425, height=45)


def close_window():
    user1.disconnect_from_server()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_window)

root.mainloop()
