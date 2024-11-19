'''Given a string, Mirror the characters of a string in alphabetical order replacing 'a' with 'z' , 'b' with 'y' ......, 'z' with 'a' to createa secrete message'''
n=input()
k=n.lower()
s=""
for i in k:
    if ord(i)>=97 and ord(i)<=122:
        a=ord(i)
        x=109-a 
        y=110+x 
        s=s+chr(y)
    else:
        s=s+i
print(s)
