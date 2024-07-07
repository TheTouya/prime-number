def is_prime(num):
    numbers = [i for i in range(2,num + 1)]
    zero = 0
    for x in numbers:
        if num % x == 0:
            zero += 1
    if zero == 1:
        print("Yes, it's a prime number")
    else:
        print("No, it's not a prime number") 

number = int(input())
is_prime(number)