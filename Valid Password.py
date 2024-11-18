'''Write a program to check whether the given password is valid or not.
Consider the password to be valid if it contains at least one uppercase letter, one lowercase letter, and one digit.'''
n=input()
u=l=c=0
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        u=1 
    elif ord(i)>=97 and ord(i)<=122:
        l=1 
    elif i.isdigit():
        c=1 
if c==1 and l==1 and u==1:
    print("Valid Password")
else:
    print("Invalid Password")
