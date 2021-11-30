import argparse
args = argparse.ArgumentParser()

args.add_argumnet('-first', '--firstVal', required=True)
args.add_argumnet('-second', '--secondVal', required=True)
args.add_argumnet('-third', '--thirdVal', required=True)

argvar = vars(args.parse_args())

pass