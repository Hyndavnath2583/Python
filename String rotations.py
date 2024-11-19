''' To check whether if a string if it is a rotation of other string. If yes, print the number of rotations'''
n=input()
x=input()
c=0
if len(n)==len(x):
    for i in range(0,len(x)):
        if x[i]==n[0]:
            c=1
            print(i)
            break
if c==0:
    print("No Match")
