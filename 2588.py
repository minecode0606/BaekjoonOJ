A=int(input())

B=int(input())


if ((A>=100) &(A<1000)) & ((B>=100) &(B<1000)) | ((A<=-100) &(A>-1000)) & ((B<=-100) &(B>-1000)) :

      b1=int(B/100)

      b2=int(B/10)-(b1*10)

      b3=B-(b1*100)-(b2*10 )

      print(A*b3)

      print(A*b2)

      print(A*b1)

      print(A*B)