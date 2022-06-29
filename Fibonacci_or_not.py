n=int(input())
fa=c=0
fb=1
fn=0
fib=[]
for i in range(100):
    fib.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
for i in range(100):
    if(n==fib[i]):
        c=1
        break
if(c==1):
    print(True)
else:
    print(False)