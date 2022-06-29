import math
n=int(input())
p=list(map(int,input().split()))
v=0
c=0
r=0
k=0
b=[]
for i in range(n):
    c=1
    if(p[i]!=-1):
        for j in range(n):
            if(p[j]==p[i] and i!=j):
                c+=1
                p[j]=-1
        k+=c//2
print(k)