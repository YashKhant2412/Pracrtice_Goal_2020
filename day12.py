n = 17
for i in range(n):
    for j in range(1,n+1):
        if (i<(n+1)/2):
            k = i
        else:
            k = n-i-1
        
        if (j<=((n+1)/2)-k or j>=((n+1)/2)+k):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
