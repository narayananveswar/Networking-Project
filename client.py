import socket
from test import COST, ITEM_NAME

PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
DISCONNECT_MESSAGE = "!QUIT"
ITEM_NAME = ['coffee', 'tea']

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def sendMessage():
    for i in ITEM_NAME:
        print(f"{i} cost : {COST[i]}")
    
    connected = True
    total = 0
    while connected:
        message = input("enter the item u want : ")
        if message in ITEM_NAME:
            msg = message.encode('utf-8')
            client.send(msg)
            total += COST[message]
        elif(message == DISCONNECT_MESSAGE):
            print(f"Your total cost is {total}")
            connected = False
        else:
            print("enter the items listed")



sendMessage()
client.close()

