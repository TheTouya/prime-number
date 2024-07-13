num1 = int(input())
num2 = int(input())
def isprime(n):
    sum = 0
    if n <= 1:
        return False
    else:
     for x in range(2, n + 1):
        if n % x == 0:
         sum += 1
     if sum == 1:
        return True
     else:
        return False
def prime_range(start, end):
    the_list = []
    for x in range(start, end + 1):
        if isprime(x):
            the_list.append(x)
    for x in the_list:
        print(x)
prime_range(num1,num2)