n = int(input("Enter a number: "))

# Check if n is prime
if n < 2:
    print(n, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

# Print all primes up to n
print("Prime numbers up to", n, ":")
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()
