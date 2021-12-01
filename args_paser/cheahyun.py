import argparse


args = argparse.ArgumentParser()

args.add_argument('-first', '--first', required= True)
args.add_argument('-second', '--second', required=True)
args.add_argument('-third', '--third', required=True)

argvar = vars(args.parse_args())


def mul():
    return argvar['first'] * argvar['second']
    

def div():
    return argvar['second'] / argvar['third']

if __name__=='__main__':
    try:
        print(mul())
        print(div())

    except ZeroDivisionError as e:
        print(e)
        
        pass
    except Exception as e:
        print(e)
        pass