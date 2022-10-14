"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

if __name__ == "__main__":
    n = 10001
    list_of_primes = [2]

    counter = 2
    while len(list_of_primes) < n:
        counter += 1
        for number in list_of_primes:
            if counter % number == 0:
                # print(counter, "is not prime, it's divisible by:", number)
                break
            if number == list_of_primes[-1]:
                # We made it to the end of the list of primes that are less than this number, so it's prime!
                list_of_primes.append(counter)
                # print("Looks like this number is prime:", counter)
    # print("List of primes:", list_of_primes)
    # print("Prime number", n, "is:", list_of_primes[-1])
    print("Answer:", list_of_primes[-1])
