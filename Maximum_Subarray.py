n=int(input())
b=list(map(int,input().split()))
lar=-100
for i in range(n):
    s=0
    for j in range(i,n):
        s+=b[j]
        if(s>lar):
            lar=s
print(lar)


