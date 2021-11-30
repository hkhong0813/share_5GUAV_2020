# 3개의 값을 갖는다
# 여러분 마음
# -first 49 -second 30 -third 0
# 곱샘과 나눗샘 --> function 처리
# basic sentence 틀에서 벗어나지 말것
# exception 처리 --> 중간 중단 없음.

# 최종 결과는 print()

# launch.json ##########################################333
# {
#     // Use IntelliSense to learn about possible attributes.
#     // Hover to view descriptions of existing attributes.
#     // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python: Current File",
#             "type": "python",
#             "request": "launch",
#             "program": "${file}",
#             "console": "integratedTerminal",
#             "args": ["-first", "49", "-second", "30", "third", "0"]
#         }
#     ]
# }


import argparse

args = argparse.ArgumentParser()
# '-'는 shortcut, '--'는 longcut
# required = True 는 뒤에 분명하게 값이 들어가지 않으면 에러가 난다.
args.add_argument('-first', type=int, default=49, required='True')
args.add_argument('-second', type=int, default=30,  required='True')
args.add_argument('-third', type=int, default=0, required='True')

def multi(a,b):
    val = a * b
    return val

def div(a,b):
    val = a / b
    return val


if __name__ == '__main__':
    try:
        arg_var = vars(args.parse_args())
        print(arg_var)
        a = arg_var.get('first')
        b = arg_var.get('second')
        c = arg_var.get('third')

        print("first * second = " + multi(a,b))
        print("second * third = " + multi(b,c))
        print("first / second = " + div(a,b))
        print("second / third = " + div(b,c))
        

    except Exception as e: 
        print("뭔가 오류가 있어요!!!")
    
    finally:
        pass

pass