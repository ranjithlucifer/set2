n,m=list(map(int,input().split()))
for i in range(n,m+1):
    a=len(str(i))
    c=0
    b=i
    while b>0:
        c=c+((b%10)**a)
        b=b//10
    if c==i:
        print(i,end=" ")
        
