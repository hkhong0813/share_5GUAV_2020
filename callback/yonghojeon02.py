def fun_callback(input):
    print('fun_callback :',input)
    return

def fun_call(text, f_callback):
    f = text
    length = len(f.read())
    f.close()
    print(length)
    f_callback(length)
    return

if __name__ == '__main__':

    try:
        call_text = open('./textfile.txt','r')
        fun_call(call_text,fun_callback)
    except Exception as e:
        pass

