

# making a diamond shape

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

n=4
i=0
while(i<n):
    j=0
    while (j<=i+1):
        print(" ",end="")
        j=j+1
    k=0
    while (k<=n-1-i):
        print("* ",end="")
        k=k+1
    print("")
    i=i+1





