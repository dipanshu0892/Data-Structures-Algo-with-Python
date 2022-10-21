# Program to find the L.C.M. of two input number

def lcm(x, y):
   # choosing the greater number
   if x > y:
       greater = x
   else:
       greater = y
       
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater = greater + 1
   return lcm
   
print("__Program to find LCM of 2 numbers__")
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))

print("L.C.M. ->", lcm(a, b))
