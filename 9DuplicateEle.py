str=input()
s=set(str)
for i in s:
    c=str.count(i)
    if(c>1):
        print(i,end=' ')
