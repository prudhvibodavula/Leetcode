limit=100
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

# Mark multiples of all primes starting from 2
print(int(limit**0.5))
for num in range(2, int(limit**0.5) + 1):
    if is_prime[num]:
        for multiple in range(num**2, limit + 1, num):
            print((multiple))
            is_prime[multiple] = False