def fun_callback(c):
    print('file length: ', c)
    return 

def fun_call(p, t, file_len):
    f = open(p, t)
    length = len(f.read())
    file_len(length)
    f.close()
    return
    # /home/ubuntu/Develops/share_5GUAV_2020/callback/quest.txt

if __name__ == '__main__':
   try:
       file_path = './callback/quest.txt'
       file_type = 'r'
       fun_call(file_path, file_type,fun_callback)
       pass
   except Exception as e:
      pass
