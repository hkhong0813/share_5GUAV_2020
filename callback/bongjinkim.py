def callback(length):
    print(length)
    return

def openFile(textfile, call_back):
    f = open(textfile, "r")
    length = len(f.read())
    f.close()
    call_back(length)
    return

if __name__ == '__main__':
    try:
        textfile = './textfile.txt'
        openFile(textfile, callback)
    except Exception as e:
        pass

pass

