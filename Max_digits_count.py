n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    while(i):
        x=i%10
        i=i//10
        c+=1
    b.append(c)
k=max(b)
m=0
for j in a:
    d=0
    while(j):
        y=j%10
        j=j//10
        d+=1
    if(d==k):
        m+=1
print(m)
        
        