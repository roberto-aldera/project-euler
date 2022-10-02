"""
The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025-385=2640.
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

if __name__ == "__main__":
    n = 100
    sum_of_squares = 0
    accumulation = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i
        accumulation += i
    square_of_sum = accumulation * accumulation

    print("Answer:", square_of_sum - sum_of_squares)
