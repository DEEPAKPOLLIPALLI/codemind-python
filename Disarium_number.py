n=int(input())
rev=s=a=temp=r=v=i=0
temp=n
while temp>0:
    r=temp%10
    rev=rev*10+r
    temp=temp//10
while rev>0:
    i+=1
    a=rev%10
    s+=pow(a,i)
    rev=rev//10
if(s==n):
    print(True)
else:
    print(False)
    
