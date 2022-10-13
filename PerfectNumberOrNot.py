l=int(input())
def perfect(n):
    if(n==1):
        return 1
    if(l%n==0):
        return(n+perfect(n-1))
    else:
        return(perfect(n-1))
if(perfect(l)==2*l):
    print("It is a perfect number")
else:
    print("It is not a perfect number")
