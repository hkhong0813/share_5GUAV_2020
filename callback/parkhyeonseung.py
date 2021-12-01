def func(a,b,fun_c):
    f = open(a,b)
    length = len(f.read())
    fun_c(length)
    f.close
    return

def func_callback(input):
    print(input)
    return

if __name__ == '__main__':
    try:
        filename = './callback/quest.txt'
        open_type = 'r'
        func(filename,open_type,func_callback)
        pass
    except Exception as e:
        print(e)
        pass