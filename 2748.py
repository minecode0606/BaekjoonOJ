memo_dict = {1:1, 2:1}

def fib(n):
    if n in memo_dict:
        return memo_dict[n]
    else:
        output = fib(n - 1) + fib(n - 2)
        memo_dict[n] = output
        return output


if __name__ == '__main__':
    input01 = int(input(""))
    print(fib(input01))