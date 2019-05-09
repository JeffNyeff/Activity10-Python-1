def countDigit(n): 
    count = 0
    while n != 0: 
        n //= 10

        if (n % 2) == 0:
               break
    else:
        count+= 1
    return count 
  
# Driver Code     
n = 15282687
print ("Number of digits : % d"%(count))
