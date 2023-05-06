import user



name = input("Enter username ")
host = input("Enter host ")
port = input("Enter port ")

user = user.User(name, host, port)
user.became_client()
user.connect('127.0.0.1', 3002)
user.se