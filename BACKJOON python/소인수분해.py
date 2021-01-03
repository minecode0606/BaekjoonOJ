a = int(input(""))
x = 2
 
while x<=a:
    if a%x==0:
        print(x)
        a=a/x
    else:
        x=x+1