a=int(input())
c=0
b=str(a)
for i in range(len(b)):
    c=c+int(b[i])**len(b)
if c==a:
    print("Yes")
else:
    print("No")
    
