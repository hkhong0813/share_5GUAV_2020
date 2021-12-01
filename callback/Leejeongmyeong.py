def f_print(input):
    print("func_call file length : ",input)
    return

def func_call(f_name,f_type,f_func):
    f = open(f_name,f_type)
    f_len = len(f.read())
    f_print(f_len)
    f .close()
    return

if __name__ == '__main__':
   try:
      name = "./callback/quest.txt"
      read_type ="r"
      func_call(name,read_type,f_print)
   except Exception as e:
      pass
