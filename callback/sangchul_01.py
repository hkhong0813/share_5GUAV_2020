import argparse

def printLength(res):    
    print('file Length : ', res)

def fileopen(file):
    f=open(file, 'r')
    lenght = len(f.read())
    f.close()
    printLength(lenght) 

if __name__ == '__main__':
   try:
       fileopen('./textfile.txt')
       
   except Exception as e:
        print("오류 : ", e )
      