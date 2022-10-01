"""
Problem 003
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def verbose_get_largest_prime_factor(n):
    prime_factors = []
    p = 2
    while n > p * p:
        if n % p == 0:
            print("p = ", p)
            prime_factors.append(p)
            n = n / p
        else:
            # p won't always be prime, but it'll give a non-zero remainder in that case,
            # and be incremented until it divides in to n
            p += 1
        print("n = ", n)
    prime_factors.append(int(n))
    print(prime_factors)
    return max(prime_factors)


def get_largest_prime_factor(n):
    p = 2
    while n > p * p:
        if n % p == 0:
            n = n / p
        else:
            p += 1
    return int(n)


if __name__ == "__main__":
    answer = get_largest_prime_factor(n=600851475143)
    print("Answer:", answer)
