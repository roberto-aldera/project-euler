"""
Problem 004
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""


def checkIfPalindrome(num_to_check: str) -> bool:
    # Slicing here makes reversing really simple
    if num_to_check == num_to_check[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    largest_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            num_to_check = i*j
            # Convert to string so reversing is easy
            if checkIfPalindrome(str(num_to_check)) and (num_to_check > largest_palindrome):
                largest_palindrome = num_to_check
    print("Answer:", largest_palindrome)
