TCP_IP = '192.168.1.106'
TCP_PORT = 49845
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))
data = client_socket.recv(1000)

if float(split6) >= float(0.3):
print("Finished");
#client_socket.close()
time.sleep(0.75)
print ("Congratulations! You lasted for " + str(Sec) + " seconds long")
break;

if float(split6) <= float(-0.3):
print("Finished");
#client_socket.close()
time.sleep(0.75)
print ("Congratulations! You lasted for " + str(Sec) + " seconds long")

