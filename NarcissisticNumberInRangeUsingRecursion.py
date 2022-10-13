def narci(num,len):
    if(num==0):
        return 0
    return((num%10)**len+narci(num//10,len))

[m,n]=list(map(int,input("Enter range: ").split()))
l=[]
for i in range(m,n+1):
    if(i==narci(i,len(str(i)))):
        l.append(str(i))
print(" ".join(l))
