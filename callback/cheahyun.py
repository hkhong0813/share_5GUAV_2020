def func_callback(input):
    print('file length: ', input)
    return

def fun_call(one, two, f_callback):
    f = open(one, two)
    length = len(f.read())
    f_callback(length)
    f.close()
    return

if __name__=='__main__':
    try:
        file = './quest.txt'
        r = 'r'
        fun_call(file, r, func_callback)

    except Exception as e:
        pass