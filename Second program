# from /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/
#http://stackoverflow.com/questions/34687050/how-can-i-measure-elapsed-time-between-the-press-of-buttons-in-python-with-tkint
import time
import sys, select
import socket

name=raw_input("What's your name?")
student_ID=raw_input("input your student ID")
response= raw_input("Hello " + name + ", are you ready?")
yes = set(['yes','y', 'ye'[0] ])
no = set(['no','n'])
text_file = open("TextFile.txt", "a")

if response== "yes" or response == "y" or response == "ye":
    print ("ready")
    time.sleep(1)
    print (float(3))
    time.sleep(1)
    print (float(2))
    time.sleep(1)
    print (float(1))
    print ("let's go")


    TCP_IP = '192.168.1.106'
    TCP_PORT = 49845
    Sec=0
    Min=0
    Lap=0
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((TCP_IP, TCP_PORT))
    #school address = client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))
    start=time.time()
    end=time.time()

    while True:

        end=time.time()
        print(end-start)
        Sec += 1
        time.sleep(1)
        secClock = (str(Min) + " Mins " + str(Sec) + " Sec ")

        print secClock
        if Sec == 60:
            Sec = 0
            Min += 1
            clock = (str(Min) + " Minute")
            print(clock)

            data = client_socket.recv(1000)

        if ():
            split = data.split(',')
            axisY = split[6]
            client_socket.close()

            break;

        else:

            split = data.split(',')
            split6 = (round(float(split[6]),3))
            #print "RECIEVED:" ,
            print split6

        if  float(split6) >= float(0.3) or float(split6) <= float(-0.3):
            print("Finished");
            #client_socket.close()
            print("Congratulations! You last for" + str(round(end-start),3) + " Seconds long")
            text_file.write("Student Name: " + name + "\n")
            text_file.write("Student ID: " + student_ID + "\n")
            text_file.write("Time: " + str(Sec) + " Seconds" + "\n")
            text_file.close()

            restart = raw_input("Try again? yes or no")
            if restart=="yes":
                client_socket.close()
                client_socket.connect((TCP_IP, TCP_PORT))

                break;
            if restart=="no":
                print 'Thank you for playing'
                break;

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            print ("finish")
            print("Congratulations! You last for" + str(round(end-start),3) + " Second long")
            text_file.write("Student Name: " + name + "\n")
            text_file.write("Student ID: " + student_ID + "\n")
            text_file.write("Time: " + str(Sec) + " Seconds" + "\n" )
            text_file.close()
            restart = raw_input("Try again? yes/no")

            if restart=="yes":
                client_socket.close()
                client_socket.connect((TCP_IP, TCP_PORT))

                break;

            if restart=="no":
                print 'Thank you for playing'
                break;

if response== "no":
    time.sleep(1)
    print("bye.")
quit
#Key information, on the phone go to the settings and deselect all options except DM
#Then change your recording rate to 1 s
