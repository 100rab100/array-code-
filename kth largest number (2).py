
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
