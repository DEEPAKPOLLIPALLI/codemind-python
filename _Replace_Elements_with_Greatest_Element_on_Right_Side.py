n=int(input())
arr=list(map(int,input().split()))
b=[]
z=n
v=0
j=1
for i in range(n-1):
    ma=arr[i+1]
    for j in range(i+1,n):
        if arr[j]>ma:
            ma=arr[j]
    print(ma,end=" ")
print(-1)