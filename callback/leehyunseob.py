def func():                               
    pass                                  
    return

#file length check
if __name__ == '__main__':
   try:
      f = open('./testfile.txt', 'r')      #1.file read -> open('')
      length = len(f.read())               #2.length 설정
      f.close()                            #3.자원클로즈 
      print(length)
   except Exception as e:
      pass