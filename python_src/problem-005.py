"""
Problem 005
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""

if __name__ == "__main__":
    i = 1
    largest_divisor = 20
    while True:
        for j in range(1, largest_divisor+1):
            if i % j != 0:
                # Division had remainder, so break out and move on
                break
        if j == largest_divisor:
            # We managed to get up to the largest divisor, so we're done!
            break
        i += 1
    print("Answer:", i)
