/* Problem 003
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143?
 */

#include <iostream>

int main() {
  auto p = 2;
  auto n = 600851475143;

  while (n > p * p) {
    if (n % p == 0) {
      n /= p;
    } else {
      // p won't always be prime, but it'll give a non-zero remainder in that
      // case, and be incremented until it divides in to n
      p++;
    }
  }

  std::cout << "Answer to problem 003: " << n << std::endl;
}
