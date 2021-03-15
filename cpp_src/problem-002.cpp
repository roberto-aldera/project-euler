/* Problem 002
 * Each new term in the Fibonacci sequence is generated by adding the previous
 * two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5,
 * 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence
 * whose values do not exceed four million, find the sum of the even-valued
 * terms.
 */

#include <iostream>
#include <numeric>
#include <vector>

int main() {
  auto a = 1;
  auto b = 2;
  auto fibonacci_values = std::vector<int>();
  auto n = 4e6;

  while (b < n) {
    if (b % 2 == 0) {
      fibonacci_values.push_back(b);
    }
    auto tmp = b;
    b = a + b;
    a = tmp;
  }

  auto sum_of_even_fibonacci =
      std::accumulate(fibonacci_values.begin(), fibonacci_values.end(), 0);

  std::cout << "Answer to problem 002: " << sum_of_even_fibonacci << std::endl;
}
