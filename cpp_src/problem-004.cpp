/* Problem 004
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
 * palindrome made from the product of two 3-digit numbers.
 */

#include <chrono>
#include <iostream>

bool CheckIfPalindrome(int candidate) {
  auto forward_reading = std::to_string(candidate);
  auto backward_reading =
      std::string(forward_reading.rbegin(), forward_reading.rend());
  return forward_reading == backward_reading;
}

int GetLargestPalindromeBruteForce() {
  auto p1 = 999;
  auto p2 = 999;
  auto largest_palindrome = 0;

  while (p2 > 0) {
    if (CheckIfPalindrome(p1 * p2)) {
      std::cout << "New palindrome for " << p1 << " x " << p2 << " = "
                << p1 * p2 << std::endl;
      if (p1 * p2 > largest_palindrome) {
        largest_palindrome = p1 * p2;
      }
      p2 = p1;
      p1--;
    } else {
      p2--;
      if (p2 == 0) {
        p2 = p1;
        p1--;
      }
    }
  }
  return largest_palindrome;
}

// Palindrome should be in the form abccba
// So expand to 100000a + 10000b + 1000c + 100c + 10b + 1a
// Becomes 100001a + 10010b + 1100c, which is divisible by 11, so palindrome
// must be too 11 is prime, so one of the two 3-digit factors must be too, so we
// need only check those cases
int GetLargestPalindromeWithTricks() {
  auto p1 = 999;
  auto p2 = 990;
  auto largest_palindrome = 0;

  while (p1 > 100) {
    p2 = 990;
    while (p2 > 100) {
      auto candidate = p1 * p2;
      if (CheckIfPalindrome(candidate)) {
        std::cout << "New palindrome for " << p1 << " x " << p2 << " = "
                  << p1 * p2 << std::endl;
        if (candidate > largest_palindrome) {
          largest_palindrome = candidate;
        }
      }
      p2 -= 11;
    }
    p1--;
  }
  return largest_palindrome;
}

int main() {
  auto t1 = std::chrono::high_resolution_clock::now();
  auto largest_palindrome = GetLargestPalindromeBruteForce();
  auto t2 = std::chrono::high_resolution_clock::now();

  // Time the brute force approach
  auto time_ms_1 =
      std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);

  auto t3 = std::chrono::high_resolution_clock::now();
  largest_palindrome = GetLargestPalindromeWithTricks();
  auto t4 = std::chrono::high_resolution_clock::now();

  // Time the more efficient force approach
  auto time_ms_2 =
      std::chrono::duration_cast<std::chrono::milliseconds>(t4 - t3);

  std::cout << "GetLargestPalindromeBruteForce took: " << time_ms_1.count()
            << " ms" << std::endl;
  std::cout << "GetLargestPalindromeBruteForce took: " << time_ms_2.count()
            << " ms" << std::endl;

  std::cout << "Answer to problem 004: " << largest_palindrome << std::endl;
}
