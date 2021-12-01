def call(x,fun):
    y = len(x.read())

    fun(x,y)
    return

def call_back(x,y):
    x.close()
    print('lengh :',y)
    return


# f = open('./test_file.txt', 'r')
# length = len(f.read())
# f.close()
# print(length)


x = open('./callback/textfile.txt', 'r')
# call(x,call_back)
if __name__ == '__main__':
    try:
        call(x,call_back)
    except Exception as e:
        pass