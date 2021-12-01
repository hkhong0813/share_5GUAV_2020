import argparse

def multi(a, b):    
    return a*b

def devide(a, b):
    return a/b

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('-first', '--firstVal', required=True)
    args.add_argument('-second', '--secondVal', required=True)
    args.add_argument('-third', '--thirdVal', required=True)

    argvar = vars(args.parse_args())
    x = int(argvar['firstVal'])
    y = int(argvar['secondVal'])
    z = int(argvar['thirdVal'])
    ret_mul = multi(x, y)
    try:
        ret_dev = devide(y,z)
    except ZeroDivisionError as e:
        print('z값 수정 필요', e)
    print('곱: ', ret_mul)

pass