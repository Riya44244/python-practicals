# Practical 2: Prime numbers (using functions)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_till(n):
    result = []
    for num in range(2, n + 1):
        if is_prime(num):
            result.append(num)
    return result


def first_n_primes(n):
    result = []
    num = 2
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result


n = int(input("Enter a number n: "))

# a. Check if n is prime
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# b. All prime numbers till n
print("Prime numbers till", n, ":", primes_till(n))

# c. First n prime numbers
print("First", n, "prime numbers:", first_n_primes(n))
