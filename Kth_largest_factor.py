n=int(input())
k=int(input())
c=0
for i in range(n,0,-1):
    if n%i==0:
        c=c+1 
    if c==k:
        print(i)
        break 
if k>c or c==0:
    print("1")
''' we need print the kth largest factor for a given number'''
