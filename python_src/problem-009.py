"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import numpy as np


if __name__ == "__main__":
    list_of_perfect_squares = []

    # Let's make a list of all the perfect squares of some sensible length
    for i in range(1, 500):
        list_of_perfect_squares.append(pow(i, 2))

    # Then iterate through it to check if the sum of any of them is in this same list
    # (not super efficient but it gets the job done)
    for i in range(len(list_of_perfect_squares)):
        for j in range(len(list_of_perfect_squares)):
            query = list_of_perfect_squares[i] + list_of_perfect_squares[j]
            if query in list_of_perfect_squares:
                if (np.sqrt(list_of_perfect_squares[i]) + np.sqrt(list_of_perfect_squares[j]) + np.sqrt(query)) == 1000:
                    print("Answer:", np.sqrt(list_of_perfect_squares[i]) * np.sqrt(
                        list_of_perfect_squares[j]) * np.sqrt(query))
                    break
