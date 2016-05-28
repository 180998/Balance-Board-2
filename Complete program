
# from /System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/
#http://stackoverflow.com/questions/34687050/how-can-i-measure-elapsed-time-between-the-press-of-buttons-in-python-with-tkint
import time
import sys, select
import socket


text_file = open("TextFile.txt", "a")
Again=True
Session=True

while Session:
    name=raw_input("Hello, what's your name?")
    student_ID=raw_input("Please input your student ID: ")
    response= raw_input("Hello " + name + ", are you ready?")

    if response== "yes" or response == "y" or response == "ye":
        while Again:
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

            start=time.time()
            end=time.time()

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((TCP_IP, TCP_PORT))
        #school address = client_socket.connect((SCHOOL_TCP_IP, SCHOOL_IP_PORT))

            while True:
                time.sleep(1)
                end=time.time()
                print(round(end-start,6))

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
                    print("Congratulations! You last for " + str(round(end-start,3)) + " Seconds long")
                    text_file.write("Student Name: " + name + "\n")
                    text_file.write("Student ID: " + student_ID + "\n")
                    text_file.write("Time: " + str(Sec) + " Second(s)" + "\n")
                    text_file.close()

                    restart = raw_input('Try again? yes or no')

                    if restart=="yes":
                        client_socket.close()
                        client_socket.connect((TCP_IP, TCP_PORT))
                        break

                    if restart=="no":
                        print 'Thank you for playing'
                        text_file.close()
                        break;

                    break;

                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    print("Finished");
                #client_socket.close()
                    print("Congratulations! You last for " + str(Sec) + " Seconds long")
                    text_file.write("Student Name: " + name + "\n")
                    text_file.write("Student ID: " + student_ID + "\n")
                    text_file.write("Time: " + str(round(end-start,3)) + " Second(s)" + "\n")
                    text_file.close()

                    restart = raw_input('Try again? yes or no')

                    if restart=="yes":
                        client_socket.close()
                        client_socket.connect((TCP_IP, TCP_PORT))
                        break

                    if restart=="no":
                        print 'Thank you for playing'
                        text_file.close()
                        break;


    if response== "no":
        time.sleep(1)
        print("bye.")





#Key information, on the phone go to the settings and deselect all options except DM
#Then change your recording rate to 1 s
