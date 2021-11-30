import argparse

parser = argparse.ArgumentParser(description="Argparse Tutorial")

# args.add_argument('-q','--quit',required=True)
parser.add_argument('-x', type=int)
parser.add_argument('-y', type=int)
parser.add_argument('-z', type=int)

args = parser.parse_args()

def multi(x,y,z):
    return f"x * y = {x*y}\ny * z = {y*z}\nz * x = {z*x}\nx * y * z = {x * y * z}"

def divide(x,y,z):
    if x == 0 or y == 0 or z == 0:
        return ZeroDivisionError
    else:
        return f"x // y = {x//y}\ny // z = {y//z}\nz // x = {z//x}"

if __name__ == '__main__':
    print(multi(args.x,args.y,args.z))
    print(divide(args.x,args.y,args.z))