n=int(input())
t=0
if(n==1):
    print("No")
else:
    for i in range(2,n):
        if(n%i==0):
            t=1
    if t==1:
        print("No")
    else:
        print("Yes")
