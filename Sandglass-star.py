n=int(input())
r="*"+" "
s=0
for i in range(n,0,-1):
    print(" "*s+r*i)
    s=s+1 
s=s-2
for j in range(2,n+1):
    print(" "*s+r*j)
    s=s-1
