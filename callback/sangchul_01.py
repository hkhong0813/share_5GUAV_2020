import argparse

def printLength(res):
    
    print('file Length : ', res)
 

if __name__ == '__main__':
   try:
        f=open('./testfile.txt', 'r')
        lenght = len(f.read())

        f.close()
        printLength(lenght)
   except Exception as e:
        print("오류 : ", e )
      