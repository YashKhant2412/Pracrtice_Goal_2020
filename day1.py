n = int(input())
for i in range(n):
    for j in range(1,2*n):
        cm1 = n-i
        cm2 = n+i

        if(i== (n-1)):
            if(j%2==0):
                print(" ",end="")
            else:
                print("*",end="")
        elif (j == cm1 or j == cm2):
            print("*",end="")
        else:
            print(" ",end="")
    print("")