def rev(n):
    rev=0
    while n:
        r=n%10
        n//=10
        rev+=r
    return rev
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=rev(i)
print(s)