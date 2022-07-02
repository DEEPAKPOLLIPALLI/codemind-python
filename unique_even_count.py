n=int(input())
c=0
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
for j in range(len(b)):
    if(b[j]%2==0):
        c+=1
print(c)