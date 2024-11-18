'''Rotate a list n times'''
def lst(a):
    x=[]
    for i in a:
        x.append(int(i))
    return x 
n=input().split(",")
z=lst(n)
k=int(input())
if k>len(z):
    k=k%(len(z))
print(z[k:]+z[:k])
