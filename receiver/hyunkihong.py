import socket
def receive():

    receiver = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)

    receiver.bind('192.168.16.25',7778)
    bytepair = receiver.recvfrom(1024)

    while True:
        message = bytepair[0]
        address = bytepair[1]

        print('message:', message)
        print('address:', address)
    return 
if __name__ == '__main__':
    try:
        receive()
    except Exception as e:
        pass
