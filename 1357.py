#1357
def rev(n):
    num=list(reversed(str(n)))
    num=''.join(num)
    num=int(num)
    return num
X,Y=map(int, input().split())
print(rev(rev(X)+rev(Y)))