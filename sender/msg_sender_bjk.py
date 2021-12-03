import socket

if __name__ == '__main__':
    try:
        sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        n = 0
        while True:
            messageToSend = 'Hello'+str(n + 1)
            sender.sendto(str.encode(messageToSend), ('192.168.16.34', 7778))
            bytepair = sender.recvfrom(1024)
            messageReceived = bytepair[0]
            print(messageToSend,', ', messageReceived)
    except:
        print("network error")


pass