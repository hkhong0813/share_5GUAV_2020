import argparse

def multi(first,second,thrid=1):
    mult = first*second*thrid
    return mult

def devision(first,second,third=1):
    dev = first/second/third
    return dev

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('-x',required=True)
    args.add_argument('-y',required=True)
    args.add_argument('-z',required=True)

    argvar = vars(args.parse_args())

    first = float(argvar['x'])
    second = float(argvar['y'])
    third = float(argvar['z'])

    
    try:
        mult_dd = multi(first,second)
        mult_tp = multi(first,second,third)
        dev21 = devision(second,first)
        dev123 = devision(first,second,third)
    except TypeError:
        print('put num')
        pass
    except ZeroDivisionError:
        dev123 = devision(first,second)
        pass
    except:
        print('error')
        pass
    finally:
        print('first*second = ',mult_dd)
        print('first*second*third = ',mult_tp)
        print('second/first = ',dev21)
        print('zerodevision error | third:0 > third :1')
        print('first/second/third = ',dev123)
        pass

    pass