def reverse(a):
    rev=0
    while a:
        r=a%10
        a=a//10
        rev=rev*10+r
    return rev 
def megaprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    else:
        d=0
        p=0
        while n:
            r=n%10
            n=n//10
            d+=1
            if r==1 or r==2 or r==3 or r==5 or r==7:
                p+=1
        if p==d:
            return 1
        else:
            return 0
def prime(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    for i in range(2,int(n*0.5)+2):
        if n%i==0:
            return 0
    return 1
n=int(input())
rev=reverse(n)
if prime(n)==0:
    print('not prime')
elif megaprime(n) and megaprime(rev):
    print('circular prime')
else:
    print('prime but not a circular prime')