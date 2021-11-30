import os
def func(a, b):

   return a*b

def dev(a, b):
   return a/b

if __name__ == '__main__':
   args = argparse.ArgumentParser()
   args.add_argument('-x','--xVal',required=True)
   args.add_argument('-y','--yVal',required=False)
   argvar = vars(args.parse_args())
   try:
      pass
   except Exception as e:
      pass

