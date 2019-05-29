n,m=list(map(int,input().split()))
l=[]
for i in range(n,m):
  if i%2!=0 and i!=1:
    l.append(i)
print(l)
