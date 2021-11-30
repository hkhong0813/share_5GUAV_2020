import argparse

def multi(num1, num2):
    num3 = num1*num2
    return num3

def divide(num1, num2):
    num3 = num1/num2
    return num3

if __name__ == '__main__':

    args = argparse.ArgumentParser()

    args.add_argument('-first','--firstVal',required=True)
    args.add_argument('-second','--secondVal',required=True)
    args.add_argument('-third','--thirdVal',required=True)
    # args.add_argument('-y','--yVal',required=False)

    argvar = vars(args.parse_args())

    n1 = int(input("input num2"))
    n2 = int(input("input num2"))

    n3 = int(input("multi or divide"))

    if n3 == 1:
        n4 = multi(n1, n2)
    elif n3 == 2:
        n4 = divide(n1, n2)
    else:
        n4 = None
    
    print(n4)

    try:
        pass
    except ZeroDivisionError:
        pass
    except NameError:
        pass
    except TypeError:
        pass
