n,m=list(map(int,input().split()))
l=[]
for i in trange(n,m):
  if i%2==0 and i!=0:
    l.append(i)
print(*l)
