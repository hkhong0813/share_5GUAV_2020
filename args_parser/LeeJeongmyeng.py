#1. -first 49 -second 30 -third 0
#2. 곱셈과 나눗셈-->함수화
#3. basic_sentence.py 사용
#4. 예외처리 --> 중간 중단 없음.
#5. 출력은 print


def func():
    pass
    return

if __name__ == '__main__':
    try:
        pass
    except Exception as e:
        pass

    class calculate:
        def multiple(a,b):
            return a*b
    
        def devide(a,b):
            try:
                a/b
            except ZeroDivisionError as e:
                pass

            return a/b
    

    import argparse

    args = argparse.ArgumentParser()

    # args.add_argument('-q','--quit',required=True)
    args.add_argument('-f','--first',required=True,type=int)
    args.add_argument('-s','--second',required=True,type=int)
    args.add_argument('-t','--third',required=True)

    argvar = vars(args.parse_args())
    # a = args.parse_args('-f')
    # b = args.parse_args('-s')
    a=10
    b=20
    print(calculate.multiple(a,b))
    print(calculate.devide(a,b))
pass