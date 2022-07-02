n=int(input())
sum=0
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for j in range(len(b)):
    if(b[j]%2==0):
        sum=sum+b[j]
print(sum)