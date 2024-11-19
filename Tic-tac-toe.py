'''To declare the winner of tic-tac-toe game between Abhinav and Anjali'''
def checkrow(n,c=0):
    for i in n:
        if i==["X","X","X"]:
            c=0
            print("Anjali Wins")
            return 0
        elif i==["O","O","O"]:
            c=0
            print("Abhinav Wins")
            return 0
        else:
            c=1 
    if c==1:
        return 1
def checkcol(n,c):
    if c==0:
        return 0
    s=[]
    for i in range(0,3):
        y=[]
        for j in range(0,3):
            y.append(n[j][i])
        s.append(y)
    for i in s:
        if i==["X","X","X"]:
            print("Anjali Wins")
            c=0
            return 0 
        elif i==["O","O","O"]:
            c=0
            print("Abhinav Wins")
            return 0
        else:
            c=1 
    if c==1:
        return 1
def checkdiag(n,c):
    if c==0:
        return 0
    k=[]
    l=[n[0][2],n[1][1],n[2][0]]
    for i in range(0,3):
        k.append(n[i][i])
    if k==["X","X","X"] or l==["X","X","X"] :
        c=0
        print("Anjali Wins")
        return 0
    elif k==["O","O","O"] or l==["O","O","O"]:
        c=0
        print("Abhinav Wins")
        return 0
    if c==1:
        print("Tie")
        return 0
p=[]
c=0
for i in range(0,3):
    a=input().split(" ")
    p.append(a)
b=checkrow(p,c)
m=checkcol(p,b)
checkdiag(p,m)
