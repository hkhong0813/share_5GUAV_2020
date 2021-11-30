import argparse

parser = argparse.ArgumentParser()

# 파일명 뒤에 숫자만 입력해도 된다.
parser.add_argument(nargs="*", type=int, dest="lst_1")

lst = parser.parse_args().lst_1

print(lst)

def multi(lst):
    
    ret = f""
    for i in range(len(lst)):
        now = i
        nxt = (i+1) % len(lst)
        ret += f"arg[{now}] x arg[{nxt}] = {lst[now]*lst[nxt]}\n"
    return ret

def divide(lst):
    
    if 0 in lst:
        try:
            any = 1/0
        except Exception as e:
            return f"{e}"
    else:
        ret = f""
        for i in range(len(lst)):
            now = i
            nxt = (i+1) % len(lst)
            ret += f"arg[{now}] / arg[{nxt}] = {float(lst[now]/lst[nxt])}\n"
        return ret

if __name__ == '__main__':
    print(multi(lst))
    print(divide(lst))