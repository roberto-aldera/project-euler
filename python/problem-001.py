"""
Problem 001
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import numpy as np
import time

if __name__ == "__main__":
    start_time = time.time()

    qualifying_multiples = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            qualifying_multiples.append(i)
    answer = np.sum(qualifying_multiples)
    elapsed_time = time.time() - start_time
    
    print("Time elapsed:", elapsed_time)
    print("Answer to problem 001: ", answer)
