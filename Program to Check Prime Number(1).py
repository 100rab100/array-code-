num = 2
# define a flag variable
flag = False

if num > 1:
    # check for factors
    for i in range(2, num//2+1):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
    
#SECOND way 

from math import sqrt
# n is the number to be check whether it is prime or not
n = 1

# this flag maintains status whether the n is prime or not
prime_flag = 0

if(n > 1):
	for i in range(2, int(sqrt(n)) + 1):
		if (n % i == 0):
			prime_flag = 1
			break
	if (prime_flag == 0):
		print("True")
	else:
		print("False")
else:
	print("False")

