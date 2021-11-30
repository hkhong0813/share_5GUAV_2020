import argparse 
#python ~.py --x=10 --y=20
def mul(args):
    return args.x * args.y #차이나는 부분
def div(args):
    return args.x / args.y
def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('--x', type = int, required = True)
    parse.add_argument('--y', type = int, required = True)
    args = parse.parse_args() #vars 라는 함수 때문에 차이가 남
    return args

if __name__ == '__main__':
    try:
        args = parser()
        print(mul(args))
        print(div(args))
    except:
        print('division by zero error')

pass
