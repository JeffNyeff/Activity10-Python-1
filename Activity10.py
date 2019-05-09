
max =int(input("Enter student Number : "))
def is_prime(n): 
    if n <= 1: 
        return False
    for i in range(2,n): 
        if n % i == 0: 
            return False
        break
    return True
  
 
c = 0 #for counting 
  
for n in  (2,max): 
    x = is_prime(n) 
    c += x
print("0.Your student number is:",max)
print("1.Total prime numbers in your student number :", c) 
  
 

