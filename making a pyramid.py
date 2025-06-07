# making a pyramid

n=5
i=0
while(i<n):
    j=0
    while (j<=n-1-i):
        print(" ",end="")
        j=j+1
    k=0
    while (k<=i):
        print("* ",end="")
        k=k+1
    print("")
    i=i+1

