n,m=list(map(int,input().split()))
for i in range(n,m+1):
    if i>1:
        for a in range(2,i):
            if i%a==0:
                break
        else:
            print(i,end=" ")
