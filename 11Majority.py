a=input()
b=a
count=0
c=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i]==b[j]):
            count=count+1
        if(count>1):
            if(a[i] not in c):
                c.append(a[i])
print(*c)
