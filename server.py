#Sockets it's a library for Connections
import socket
#
from _thread import *
import sys

#put your local ip adress
server = "localhost"
#put your local port
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #bind on port
    s.bind((server, port))
except socket.error as e:
    str(e)
#Open the port and start listening for clients, even multiple Connections
#Here it only looks for one connection
s.listen(2) #The number of clients

print("Listening on port", port,", Server started, Waiting for player")

#This is threaded, a new process running in the background
#So we can have a hundred connections going, executing as subprocesses
def threaded_client(conn):
#We'll try to intercept and respond to some type of data
    reply = ""
    while True:
        try:
            #The ammount of bytes we receive (if we get any error try to increase)
            data = conn.recv(2048)
            #The larger the data the longer it's gonna receive information 2048 should be almost instantly you can do i.e(2048*4)
            reply = data.decode("utf-8")

            #No infinite loop, if the conn to the client breaks, we just disconect
            if not data:
                print("Disconnected")
                break
            else:
                print("Received data:", reply)
                print("Sending:", reply)
            #Encode the reply and send
            conn.sendall(atr.encode(reply))
        except:
            break

#if this was sequentially programmed we would have to wait for the threaded_client(conn) function to finish when called
#
#Continiosly looking for connections
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))
