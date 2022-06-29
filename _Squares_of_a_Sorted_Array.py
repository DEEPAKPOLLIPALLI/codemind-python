n=int(input())
p=list(map(int,input().split()))
k=0
v=0
c=0
b=[]
for i in range(n):
    v=p[i]*p[i]
    b.append(v)
for i in range(n):
    for j in range(i+1,n):
        if(b[i]>b[j]):
            k=b[i]
            b[i]=b[j]
            b[j]=k
for i in range(n):
    print(b[i],end=" ")
        