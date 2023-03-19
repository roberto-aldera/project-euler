"""
Problem 010
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def sieveOfEratosthenes(upper_limit):
    list_of_primes = []
    prime = [True for i in range(upper_limit+1)]
    p = 2
    while (p * p <= upper_limit):

        # If prime[p] has not yet been ruled out, then it's prime
        if (prime[p] == True):
            # Updating all multiples of p
            for i in range(p * p, upper_limit+1, p):
                prime[i] = False
        p += 1

    for p in range(2, upper_limit+1):
        if prime[p]:
            list_of_primes.append(p)
    return list_of_primes


if __name__ == "__main__":
    print("Answer:", sum(sieveOfEratosthenes(2000000)))
