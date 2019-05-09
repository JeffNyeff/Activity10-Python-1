
prime = []
my_number = 12345678
num_str = list(map(int, str(my_number)))


for num in num_str:
    if num <= 1:
        return false
        for i in range(2, num // 2):
            if (num % i) == 0:
                return false
            break
       
        
            count = 0
            prime.append(num)
for p in prime:
    while p > 0:
        count += count

        print('The prime numbers found in the students number is ', count)
