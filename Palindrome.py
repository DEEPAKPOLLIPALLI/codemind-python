n=int(input())
v=n
rev=0
while(n!=0) :
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==v :
    print('True')
else :
    print('False')