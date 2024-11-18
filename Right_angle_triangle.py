n=int(input())
for i in range(1,n+1):
    s=""
    a=1
    for k in range(a,a+i-1):
        s=s+str(k)
    for j in range(i,0,-1):
        s=s+str(j)
    print(s)
'''Sample Input 
9
Sample Output 
1
121
12321
1234321
123454321
12345654321
1234567654321
123456787654321
12345678987654321'''
