def this(i,a,j):
    while i < a:
        op.append(j)
        i+=1
        j+=2
a=int(input("input number:"))
i=0
j=1
op=[]
if a%2 == 0:
    this(i,a-1,j)
else:
    this(i,a,j)

print(op)
