n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    if i+1<n:
        v=a[i]
        for j in range(v):
            print(a[i+1],end=" ")