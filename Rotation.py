t=int(input())
for k in range(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(b):
        temp1=arr[0]
        arr[0]=arr[-1]
        for j in range(1,a):
            temp2=arr[j]
            arr[j]=temp1
            temp1=temp2
    print(*arr)
