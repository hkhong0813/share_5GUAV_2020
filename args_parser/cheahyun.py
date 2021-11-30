import argparse


args = argparse.ArgumentParser()
args.add_argument('-x', '--first', required= True)
args.add_argument('-y', '--second', required=True)
args.add_argument('-z', '--third', required=True)

argvar = vars(args.parse_args())


def mul():
    multi = int(argvar['first']) * int(argvar['second'])
    return multi
    

def div():
    division = int(argvar['second']) / int(argvar['third'])
    return division

if __name__=='__main__':
    try:
        multi = mul()
        division = div()

    except ZeroDivisionError:
        if int(argvar['third']) == 0:
            argvar['third']= 1
            division = div()
        pass
    except Exception as e:
        pass