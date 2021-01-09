import datetime
import os 
import time
name = input("What is your Name?")

now = datetime.datetime.now()
fmt = "%Y-%m-%d-%H"
while True:
    ch = input("Chat Message: ")
    chtx = open("chat.txt","a")
    chtx.write(now.strftime(fmt) + " "+ name + ": " + str(ch)+ " \n")
    print (now.strftime(fmt) + " "+ name + ": " + str(ch))
    os.system("python3 main.py")