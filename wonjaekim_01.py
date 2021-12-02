import argparse

args=argparse.ArgumentParser()

args.add_argument('-x','--xVal', '-y', '--yVal', '-z', '--zVal' required=True)


argvar=vars(args.parse_args())

pass


def num():
    a=int(input('input a : '))
    b=int(input('input b : '))
    return a, b

def func(a,b):
    multi = a*b
    devi = a/b
    return multi, devi

if __name__=='__main__':
    try:
        a, b=num()
        multi,_=func(a,b)
        _,devi=func(a,b)

    except ZeroDivisionError:
        print('can not devide by zero')
        devi=func(a,1)
        pass
    finally:
        try:
        print(multi, devi)
        break
    pass
pass


