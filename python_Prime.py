import math
import random
from itertools import islice
import string
prime =[]
my_number = 15282687
num_str = list(map(int, str(my_number)))
count = 0

for num in num_str:
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
               break  
            
        else:
            prime.append(num)
            count +=1
    
x = random.randint(25,50)

r=x/count


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
      
     
print('0.Your student number is:' ,my_number)
print('1.Number of Primes in your student number:' ,count)
print('2. The random number is: ', x)
print('3.The number of strings to be generated: ',round(r,0))
print('4.Random String List: ******')
print('###############################')
for i in range(0,r):
    if i%2 ==0:
        print(i,randomString(5))
    else:
        print(i,randomString(7))
print('##############################')
print('5.Sorted List:')
for i in range(0,r):
    if i%2 ==0:
        print(i,randomString(5))
    else:
        print(i,randomString(7))





    





      
            
            
