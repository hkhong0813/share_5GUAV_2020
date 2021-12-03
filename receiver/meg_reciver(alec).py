
import socket

receiver=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
receiver.bind(('192.168.16.34',7778))

while True:
    bytepair=receiver.recvfrom(1024)
    
    
    message=bytepair[0]
    address=bytepair[1]
    
    
    print(message,',', address)
