import argparse


args = argparse.ArgumentParser()

args.add_argument('-x', '--first', required= True)
args.add_argument('-y', '--second', required=True)
args.add_argument('-z', '--third', required=True)

argvar = vars(args.parse_args())


def mul():
    return argvar['first'] * argvar['second']
    

def div():
    return argvar['second'] / argvar['third']

if __name__=='__main__':
    try:
        print(mul())
        print(div())

    except ZeroDivisionError:
        pass
    except Exception as e:
        pass