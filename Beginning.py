import time
import socket


text_file = open("TextFile.txt", "a")
Restart=True
Session=True

while Session:
    name=raw_input("Hello, what's your name?")
    student_ID=raw_input("Please input your student ID: ")
    response= raw_input("Hello " + name + ", are you ready?")

    if response== "yes" or response == "y" or response == "ye":
        while Restart:
            print ("ready")
            time.sleep(1)
            print (float(3))
            time.sleep(1)
            print (float(2))
            time.sleep(1)
            print (float(1))
            print ("let's go")
