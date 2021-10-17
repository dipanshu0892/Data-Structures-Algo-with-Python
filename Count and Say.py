import copy
class Solution(object):
    def countAndSay(self, n):
        s="1"
        if n==1:
            return s
        if n==2:
            return '11'
        if n==3:
            return '21'
        if n==4:
            return '1211'
        
       
        s=list('1211')  
        for i in  range(5,n+1):
            m=0
            n=1
            z=1
            l=[]
            while n<len(s):
                if s[m]==s[n]:
                    z=z+1
                   
                    n=n+1
                    if n==len(s):
                         l=l+[str(z)]+[s[m]]
                else:
                    l=l+[str(z)]+[s[m]]
                    z=1
                    m=n
                    n=m+1
           
            if m+1==len(s):
                l=l+[str(z)]+[s[m]]
            s=copy.copy(l)
        l="".join(l)
        return(l)
                    
                
            
                
                
        
       
        
