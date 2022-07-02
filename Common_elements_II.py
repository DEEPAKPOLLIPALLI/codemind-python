a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
b=[]
d=[]
c=[]
for i in x:
    if i not in y:
        b.append(i)
for j in y:
    if j not in x:
        d.append(j)
for k in b:
    if k not in c:
        c.append(k)
for l in d:
    if l not in c:
        c.append(l)
print(*c)