import argparse
import sys

def func01():
    parser = argparse.ArgumentParser(description='multiplier')
    parser.add_argument('A', type=int, 
                help="What is the first number?")
    parser.add_argument('B', type=int,
                help="What is the second number?")
    args = parser.parse_args()
    A = args.A
    B = args.B
    print("%d * %d = %d" % (A, B, A*B))

def func02():
    parser = argparse.ArgumentParser(description='divider')
    parser.add_argument('A', type=int, 
                help="What is the first number?")
    parser.add_argument('B', type=int,
                help="What is the second number?")
    args = parser.parse_args()
    A = args.A
    B = args.B
    print("%d / %d = %d" % (A, B, A/B))

if __name__ == '__main__':
    try:      
        func01()
        func02()

    except ZeroDivisionError:
        B = 1
        pass
    except  SystemExit:
        sys.exit()
    except Exception as e:
        pass