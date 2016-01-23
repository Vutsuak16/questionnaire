__name__ = "vutsuak"

n = 600851475143

prime_factors = []
for i in range(1, int((n + 1)**.5+1)):
    if n % i == 0:
        ct = 0
        if i > 1:
            sqrt_factor = i ** .5
            for j in range(1, int(sqrt_factor)+1):
                if i % j == 0:
                    ct += 1
            if ct == 1:
                prime_factors.append(i)

print max(prime_factors)
