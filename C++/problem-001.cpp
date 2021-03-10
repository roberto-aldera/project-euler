// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <iostream>

int main() {
	int sum_of_multiples = 0;

	for (auto i = 0; i < 1000; ++i) {
		if(i % 3 == 0 || i % 5 == 0) {
			sum_of_multiples += i;
		}
	}
	std::cout << "Answer to problem 001: " << sum_of_multiples << std::endl;
}