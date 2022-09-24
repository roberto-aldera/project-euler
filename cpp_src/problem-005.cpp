/* Problem 005
 * 2520 is the smallest number that can be divided by each of the numbers from 1
 * to 10 without any remainder. What is the smallest positive number that is
 * evenly divisible by all of the numbers from 1 to 20?
 */

#include <iostream>

size_t get_number(const size_t highest_divisor,
                  const size_t max_number_to_check) {
  for (size_t the_number = 1; the_number < max_number_to_check; ++the_number) {
    for (size_t divisor = 1; divisor < highest_divisor + 1; ++divisor) {
      if (the_number % divisor != 0) {
        // then we must disqualify it and move on
        break;
      }

      if (divisor == highest_divisor) {
        // we've made it!
        return the_number;
      }
    }
  }
  return -1;
}

int main() {
  const size_t highest_divisor = 20;

  auto the_number = get_number(highest_divisor, SIZE_T_MAX);
  std::cout << "Answer to problem 005: " << the_number << std::endl;
}