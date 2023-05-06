from tkinter import *
from tkinter import ttk
import re
from tkinter.messagebox import showerror, showwarning, showinfo


class Authentication(Tk):
    def __init__(self):
        super().__init__()

        self.username = ""
        self.host = ""
        self.port = ""
        self.repeat = True

        self.title("Authentication")
        self.geometry("300x150")

        self.username_label = ttk.Label(self, text="Username:", font=20)
        self.host_label = ttk.Label(self, text="Host:", font=20)
        self.port_label = ttk.Label(self, text="Port:", font=20)

        self.username_editor = ttk.Entry(self, font=20)
        self.host_editor = ttk.Entry(self, font=20)
        self.port_editor = ttk.Entry(self, font=20)

        self.auth_button = ttk.Button(self, text="AUTHENTICATION", command=self.click_button)

        self.username_label.place(relx=0.05, rely=0.1, width=200, height=25)
        self.host_label.place(relx=0.05, rely=0.3, width=200, height=25)
        self.port_label.place(relx=0.05, rely=0.5, width=200, height=25)

        self.username_editor.place(relx=0.4, rely=0.1, width=175, height=25)
        self.host_editor.place(relx=0.4, rely=0.3, width=175, height=25)
        self.port_editor.place(relx=0.4, rely=0.5, width=175, height=25)

        self.auth_button.place(relx=0.2, rely=0.7, width=200, height=30)
        self.mainloop()

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

    def check_username(self):
        self.username = self.username_editor.get()
        if (len(self.username) < 20 and not re.findall(r'\s', self.username)):
            return True
        else:
            showwarning(message="Name longer than 20 characters or exists spaces")
            return False

    def check_port(self):
        self.port = self.port_editor.get()
        if (len(self.port) and 2000 < int(self.port) < 65536):
            return True
        else:
            showerror(message="Incorerct port")
            return False

    def click_button(self):
        if (self.check_username() and self.check_host() and self.check_port()):
            self.repeat = False
            self.destroy()
        else:
            self.repeat = True

    def return_data(self):
        return self.username, self.host, self.port


    # def pass_authorization(self):



# root = Tk()
# root.title("authentication")
# root.geometry("300x150")
