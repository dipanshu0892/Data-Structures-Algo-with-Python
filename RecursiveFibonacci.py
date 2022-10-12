l=[0,1]
#recursive Fibonacci
def Fibonacci(n):
    if(n<=0):
        return(l[0])
    if(n==1):
        return(l[1])
    if(len(l)>n):
        return(l[n])
    l.append(Fibonacci(n-1)+Fibonacci(n-2))
    return(l[len(l)-1])

#main code
Fibonacci(int(input()))
print(l[len(l)-1])
