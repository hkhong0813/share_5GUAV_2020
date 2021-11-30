import argparse

args = argparse.ArgumentParser()

def multi(a,b):
    return a*b

def devide(a, b):
    return a/b    

args.add_argument('-first', '--FirstVal', required=True)
args.add_argument('-second', '--SecondVal', required=True)
args.add_argument('-third', '--ThirdVal', required=True)
argvar = vars(args.parse_args())

if __name__ == '__main__':
   try:
      print(multi)
      print(devide)
      pass
   except Exception as e:
      pass

