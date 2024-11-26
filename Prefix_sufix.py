'''Tocheck if the suffix of the given word is prefix of the next word. If yes print the word else print no overlapping'''
n=input()
k=input().split(n[-1])
x=k[0]+n[-1]
n=n.split(x[0])
y=x[0]+n[-1]
if x==y:
    print(x)
else:
    print("No overlapping")
