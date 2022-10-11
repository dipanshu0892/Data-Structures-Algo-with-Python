#function for GCD
def GCD(a,b=0):
    if(b==0):
        return a
    return(GCD(b,a%b))


l=list(map(int,input("Enter numbers to find the GCD").split()))
m=GCD(l[0])
for i in range(1,len(l)):
    if(m==1):
        break
    m=GCD(m,l[i])
print(m)
