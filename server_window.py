import tkinter as tk
from tkinter.scrolledtext import ScrolledText


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
