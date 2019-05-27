a=int(input())
cont=0
c=0
for i in range(2,a):
    if(a%i==0):
        cont=cont+1
if(cont==0):
    a=str(a)
    a=a[::-1]
    a=int(a)
    for j in range(2,a):
        if(a%j==0):
            c=c+1
    if(c==0): 
        print("twisted")
    else:
        print("not twist")
else:
    print("not twist")
