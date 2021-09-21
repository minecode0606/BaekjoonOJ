memo_dict = {1:1, 2:1}

# def fib(n):
#     try:
#         if n in memo_dict:
#             return memo_dict[n]
#         else:
#             output = fib(n - 1) + fib(n - 2)
#             memo_dict[n] = output
#             return output
#     except:
#         pass

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    input01 = int(input(""))
    print(fib(input01))