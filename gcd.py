# method to compute gcd ( Euclidean algo )
 
 
def computeGCD(x, y):
 
   while(y):
       x, x = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60, 48))
