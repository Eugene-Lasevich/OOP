import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading


class ServerWindow(tk.Tk):
    def __init__(self, text):
        super().__init__()

        self.title(text)
        self.geometry("400x300")

        self.scrolled_text = ScrolledText(self)
        self.scrolled_text.pack(fill=tk.BOTH, expand=True)
        self.scrolled_text.configure(state="disabled")

    def append_text(self, text):
        self.scrolled_text.configure(state="normal")
        self.scrolled_text.insert(tk.END, text)
        self.scrolled_text.see(tk.END)
        self.scrolled_text.configure(state="disabled")


class ChatWindow(tk.Tk):
    def __init__(self, client):
        super().__init__()
        self.title("Chat Window")
        self.geometry("500x500")
        self.text = ""
        self.client = client

        self.scrolled_text = ScrolledText(self)
        # self.scrolled_text.pack(fill=tk.BOTH, expand=True)
        self.scrolled_text.configure(state="disabled")
        self.scrolled_text.place(relx=0.1, rely=0.1, width=400, height=250)
        self.msg_editor = tk.Entry(self)

        self.exit_btn = tk.Button(self, text="exit", command=self.click_exit_btn)
        self.send_btn = tk.Button(self, text="send", command=self.click_send_btn)

        self.exit_btn.place(relx=0, rely=0.85, width=75, height=30)
        self.send_btn.place(relx=0.7, rely=0.85, width=100, height=30)
        self.msg_editor.place(relx=0.2, rely=0.85, width=200, height=30)

        self.update_label()

    def update_label(self):
        if not self.client.my_queue.empty():
            message = self.client.my_queue.get()
            self.append_text(message)
        self.after(100, self.update_label)

        # window_thread = threading.Thread(target=self.mainloop)
        # window_thread.start()
        # self.mainloop()

    def append_text(self, text):
        self.scrolled_text.configure(state="normal")
        self.scrolled_text.insert(tk.END, text + '\n')
        self.scrolled_text.see(tk.END)
        self.scrolled_text.configure(state="disabled")

    def click_exit_btn(self):
        pass

    def click_send_btn(self):
        self.text = self.msg_editor.get()
        self.msg_editor.delete(0, tk.END)
        self.client.send_message(self.text)


        # self.append_text(self.text)

    def return_data(self):
        return self.text





