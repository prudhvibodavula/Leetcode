def sieve_of_eratosthenes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize all entries as True
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Mark multiples of all primes starting from 2
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num**2, limit + 1, num):
                is_prime[multiple] = False

    # Collect all prime numbers into a list
    primes = [num for num, is_prime in enumerate(is_prime) if is_prime]

    return primes
limit = 30
primes = sieve_of_eratosthenes(limit)
print(primes)