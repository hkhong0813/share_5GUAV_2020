import argparse

args = argparse.ArgumentParser()

args.add_argument('-x','--first',required=True)
args.add_argument('-y','--second',required=True)
args.add_argument('-z','--third',required=True)

argvar = vars(args.parse_args())


def myname(x,y,z):
    q = x*y*z
    p = x/y/z
    return q,p


pass

if __name__ == '__main__':
    try:
        myname(float(argvar['first']),float(argvar['second']),float(argvar['third']))

    except ZeroDivisionError:
        if float(argvar['third'])== 0:
            (argvar['third'])=1

    finally :
        myname(float(argvar['first']),float(argvar['second']),float(argvar['third']))

        pass
