import argparse
from itertools import permutations 

args = argparse.ArgumentParser()
args.add_argument('-first', '--xVal', required=True)
args.add_argument('-second', '--yVal', required=True)
args.add_argument('-third', '--zVal', required=True)

argvar = vars(args.parse_args())

def mul_div(argvar):
    x,y,z = argvar.values()
    arg_list = [x,y,z]
    combilist = list(permutations(arg_list, 2))

    for x,y in combilist:
        mul = x*y
        try:
            div = x/y
            return print(f'{x}x{y}={mul} , {x}/{y}={div}')
        except:
            return print(f'{x}/{y}={div} : ZeroDivisionError')
    
    pass

mul_div(argvar)

