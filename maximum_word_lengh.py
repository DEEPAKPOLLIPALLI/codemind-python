n=input()
b=[]
c=0
for i in n:
    if(i==' '):
        b.append(c)
        c=0
        continue
    else:
        c+=1
b.append(c)
print(max(b))