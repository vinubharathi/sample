n=str(input())
list=[]
for i in range(int(len(n))):
    list.append(n[i])
a=list.count("(")
b=list.count(")")
if a==b:
    print("Yes")
else:
    print("No")
                
                
 
