import datetime
import pickle


class Message:

    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.date = datetime.datetime.now()

    def __str__(self):
        tmp = str(self.date).split(' ')
        date = tmp[0]
        time = tmp[1].split('.')[0]
        return f"{date} {self.sender} \t {self.text} \n{time} \n"
