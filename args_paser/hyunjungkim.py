import argparse

args = argparse.ArgumentParser()

args.add_argument('--first', type = int, required=True) 
args.add_argument('-second', type = int, required=True) 
args.add_argument('-third', type = int, required=True) 

# argvar = vars(args.parse_args())
argvar = vars(args.parse_args())


pass


first = argvar.first
second = argvar.second
third = argvar.third

def multiple(first, second, third):
    try:
        fsm = first * second
        stm = second * third
        ftm = third * first
        return fsm, stm, ftm 
    except ZeroDivisionError:
        pass

def division(first, second, third):
    try:
        fsm = first / second
        stm = second / third
        ftm = third / first
        return fsm, stm, ftm 
    except ZeroDivisionError:
        pass

if __name__ == '__main__':
    try:
        pass
    except Exception as e:
        pass


pass #print 쓰면 안된다.
