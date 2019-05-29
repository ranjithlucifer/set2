n=int(input())
a=len(str(n))
c=0
b=n
while b!=0:
    c=c+((b%10)**a)
    b=b//10
if c==n:
    print("yes")
else:
    print("no")
