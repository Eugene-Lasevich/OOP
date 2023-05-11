from tkinter import *
from tkinter import ttk
import re
from tkinter.messagebox import showerror, showwarning, showinfo
import threading


class Authentication(Tk):
    def __init__(self):
        super().__init__()

        self.host = ""
        self.port = ""
        self.repeat = True

        self.title("Authentication")
        self.geometry("300x150")

        self.host_label = ttk.Label(self, text="Host:", font=20)
        self.port_label = ttk.Label(self, text="Port:", font=20)

        self.host_editor = ttk.Entry(self, font=20)
        self.port_editor = ttk.Entry(self, font=20)

        self.auth_button = ttk.Button(self, text="AUTHENTICATION", command=self.click_button)

        self.host_label.place(relx=0.05, rely=0.3, width=200, height=25)
        self.port_label.place(relx=0.05, rely=0.5, width=200, height=25)

        self.host_editor.place(relx=0.4, rely=0.3, width=175, height=25)
        self.port_editor.place(relx=0.4, rely=0.5, width=175, height=25)

        self.host_editor.insert(0, "127.0.0.1")
        self.port_editor.insert(0, "3002")

        self.auth_button.place(relx=0.2, rely=0.7, width=200, height=30)
        window_thread = threading.Thread(target=self.mainloop)
        window_thread.start()

    def check_host(self):
        self.host = self.host_editor.get()
        if re.search(r'^(?:\d{1,3}\.){3}\d{1,3}$', self.host):
            if (all(map(lambda x: int(x) <= 255, self.host.split('.')))):
                return True
            else:
                showerror(title="Incorect host", message="Value greater than 255")
                return False
        else:
            showerror(title="Incorect host", message="Address does not match pattern")
            return False

    def check_port(self):
        self.port = self.port_editor.get()
        if (len(self.port) and 2000 < int(self.port) < 65536):
            return True
        else:
            showerror(message="Incorerct port")
            return False

    def click_button(self):
        if self.check_host() and self.check_port():
            self.destroy()

    def return_data(self):
        return self.host, self.port


class Registration(Tk):
    def __init__(self):
        super().__init__()

        self.name = ""

        self.title("Registration")
        self.geometry("300x150")

        self.user_lbl = ttk.Label(self, text="Enter you username", font=20)
        self.user_editor = ttk.Entry(self, font=40)
        self.enter_btn = ttk.Button(text="ENTER", command=self.click_reg_btn)

        self.user_lbl.place(relx=0.2, rely=0.1, width=200, height=30)
        self.user_editor.place(relx=0.2, rely=0.3, width=200, height=40)
        self.enter_btn.place(relx=0.2, rely=0.6, width=200, height=30)

        self.mainloop()

    def check_name(self):
        self.name = self.user_editor.get()
        if not len(self.name):
            showerror(title="Empty name", message="Can't be an empty name")
            return False
        if len(self.name) > 20:
            showerror(title="Very big name", message="Name can't be more than 20 characters")
            return False
        if " " in self.name:
            showerror(title="Space in name", message="Name can't contain spaces")
            return False
        return True

    def click_reg_btn(self):
        if self.check_name():
            self.destroy()

    def get_name(self):
        return self.name

