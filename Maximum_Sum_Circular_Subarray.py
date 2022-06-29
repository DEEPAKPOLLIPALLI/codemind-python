a=int(input())
arr=list(map(int,input().split()))
ms=-1000
for i in range(a):
    for j in range(a):
        for k in range(j,a):
            s=sum(arr[j:k+1])
            if ms<s:
                ms=s
    t=arr[0]
    arr[0]=arr[-1]
    for j in range(1,a):
        temp=arr[j]
        arr[j]=t
        t=temp
print(ms)