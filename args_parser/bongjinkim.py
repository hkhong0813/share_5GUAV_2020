import argparse 
#python ~.py -x 10 -y 20
def mul(args):
    return args['x'] * args['y']
def div(args):
    return args['x'] / args['y']
def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-x','--x', type = int, required = True)
    parse.add_argument('-y','--y', type = int, required = True)
    args = vars(parse.parse_args())
    return args

if __name__ == '__main__':
    try:
        args = parser()
        print(mul(args))
        print(div(args))
    except:
        print('division by zero error')

pass

