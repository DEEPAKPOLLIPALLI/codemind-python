n=int(input())
a=list(map(int,input().split()))
s=0
count=0
for i in a:
    s+=i
avg=s//n
for i in a:
    if i>=avg:
        count+=1
print(count)