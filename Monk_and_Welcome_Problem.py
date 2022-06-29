n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
c=[]
v=0
for i in range(n):
    v=p[i]+q[i]
    c.append(v)
for i in range(n):
    print(c[i],end=" ")

