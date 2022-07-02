a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
b=[]
d=[]
for i in x:
    if i in y:
        b.append(i)
for j in b:
    if j not in d:
        d.append(j)
print(*d)