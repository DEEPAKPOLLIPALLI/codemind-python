a=int(input())
fa=0
fb=1
fn=0
fib=[]
for i in range(a):
    fib.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
for i in range(a):
    print(fib[i],end=" ")