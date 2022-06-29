a=int(input())
arr=list(map(int,input().split()))
m=c=ma=0
x=0
for i in range(a):
    c=1
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                c+=1
    if c==ma:
        #print(mc)
        mc=c
        x+=1
        if arr[i]<m:
            m=arr[i]
    elif c>ma:
        ma=c
        m=arr[i]
print(m)
#print(x)

