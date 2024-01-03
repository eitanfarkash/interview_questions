# import math


# lower = 0
# upper = 101

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# l1 =[i for i in range(lower, upper+1)]
# print(l1)

# for i in range(2, int(math.sqrt(upper))+1):
#     for j in range(2, int(upper/2)+1):
#         try:
#             l1.remove(i*j)
#         except ValueError:
#             print(f"i = {i} j={j} i*j={i*j}")
# print(f"l1 = {l1}")
# for j in range(2, int(upper/2)+1):
#     x = l1[j] 

# def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     primes[0] = primes[1] = False
#     for num in range(2, int(limit**0.5) + 1):
#         if primes[num]:
#             for multiple in range(num * num, limit + 1, num):
#                 primes[multiple] = False

#     return [num for num in range(2, limit + 1) if  primes[num]]

# # Find primes in the range 0 to 100
# result = sieve_of_eratosthenes(100)
# print(result)

def prime_numbers(max) ->list:
    primes = [True for i in range(max+1)]
    primes[0] = primes[1] = False
    for num in range(2, int(max/2)+1):
        if primes[num]:
            for i in range(num**2, max+1, num):
                primes[i] = False
    return [i for i in range(0,max+1) if primes[i]]


if __name__ == "__main__":
    Max_num = 101
    print(f"List of prime numbers in range of O to {Max_num}:\n {prime_numbers(Max_num)}")