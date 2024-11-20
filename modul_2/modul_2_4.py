numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for delitel in primes:
        if i % delitel == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True and i != 1:
        primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)